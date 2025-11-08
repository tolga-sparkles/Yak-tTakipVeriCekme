import sys
import os
import asyncio
from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException, Request, BackgroundTasks
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# Add the project root to the Python path to allow absolute imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.scraper import fetch_all_prices
from app.database import create_table, update_prices, get_prices_by_city, get_all_distinct_cities

# --- Background Task for Automatic Updates ---
async def scheduled_update():
    """Runs the update process every 24 hours."""
    while True:
        print("Scheduled update running...")
        try:
            all_prices = fetch_all_prices()
            update_prices(all_prices)
            print("Scheduled update finished. Waiting for 24 hours.")
        except Exception as e:
            print(f"Error during scheduled update: {e}")
        await asyncio.sleep(24 * 60 * 60) # Sleep for 24 hours

# --- FastAPI Lifespan Events ---
@asynccontextmanager
async def lifespan(app: FastAPI):
    # On startup
    print("API starting up...")
    create_table()

    # Run initial update in the background
    print("Triggering initial data update...")
    asyncio.create_task(run_update_task_on_startup())

    # Start the background scheduler
    asyncio.create_task(scheduled_update())

    yield
    # On shutdown
    print("API shutting down...")

async def run_update_task_on_startup():
    """Wrapper to run the initial update without blocking startup."""
    print("Initial update task started...")
    prices = fetch_all_prices()
    update_prices(prices)
    print("Initial update task finished.")

app = FastAPI(lifespan=lifespan)

# Mount static files
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Setup templates
templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    """Serves the main HTML page with a list of cities."""
    cities = get_all_distinct_cities()
    return templates.TemplateResponse("index.html", {"request": request, "cities": cities})

@app.get("/api/prices/{city_name}")
def get_city_prices_api(city_name: str):
    """API endpoint to get fuel prices for a specific city."""
    try:
        prices = get_prices_by_city(city_name)
        if not prices:
            raise HTTPException(status_code=404, detail=f"No price data found for city: {city_name}.")
        return {"city": city_name.upper(), "prices": prices}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")

def run_manual_update_task():
    """Wrapper function for manual updates."""
    print("Manual update triggered...")
    prices = fetch_all_prices()
    update_prices(prices)
    print("Manual update finished.")

@app.post("/api/update")
def force_update(background_tasks: BackgroundTasks):
    """Manually triggers the data update process in the background."""
    background_tasks.add_task(run_manual_update_task)
    return {"message": "Data update process has been triggered in the background."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True, app_dir="app")
