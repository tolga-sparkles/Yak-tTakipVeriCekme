from fastapi import FastAPI, HTTPException, BackgroundTasks
from scraper import fetch_all_prices
from database import create_table, update_prices, get_prices_by_city
import time
import asyncio

# --- Background Task for Automatic Updates ---
async def scheduled_update():
    """Runs the update process every 24 hours."""
    while True:
        print("Scheduled update running...")
        all_prices = fetch_all_prices()
        update_prices(all_prices)
        print("Scheduled update finished. Waiting for 24 hours.")
        await asyncio.sleep(24 * 60 * 60) # Sleep for 24 hours

# --- FastAPI Lifespan Events ---
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    # On startup
    print("API starting up...")
    create_table()

    # Run initial update
    print("Running initial data update...")
    initial_prices = fetch_all_prices()
    update_prices(initial_prices)
    print("Initial data update complete.")

    # Start the background scheduler
    asyncio.create_task(scheduled_update())

    yield
    # On shutdown
    print("API shutting down...")


app = FastAPI(lifespan=lifespan)


@app.get("/")
def read_root():
    return {"message": "Fuel Price API. Use /prices/{city_name} to get prices."}

@app.get("/prices/{city_name}")
def get_city_prices(city_name: str):
    """
    Returns fuel prices for a specific city.
    The city name is case-insensitive.
    """
    try:
        prices = get_prices_by_city(city_name)
        if not prices:
            raise HTTPException(status_code=404, detail=f"No price data found for city: {city_name}.")
        return {"city": city_name.upper(), "prices": prices}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")

def run_update_task():
    """Wrapper function to be run in the background."""
    print("Manual update triggered...")
    prices = fetch_all_prices()
    update_prices(prices)
    print("Manual update finished.")

@app.post("/update")
def force_update(background_tasks: BackgroundTasks):
    """
    Manually triggers the data update process in the background.
    """
    background_tasks.add_task(run_update_task)
    return {"message": "Data update process has been triggered in the background."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
