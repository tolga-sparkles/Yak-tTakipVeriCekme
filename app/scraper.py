import sys
import os

# Add the project root to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.scrapers.alpet_scraper import get_alpet_prices

def fetch_all_prices():
    """
    Fetches prices from all available scrapers and returns a combined list.
    Currently, only Alpet is supported.
    """
    all_prices = []

    # --- Alpet ---
    print("Fetching prices from Alpet...")
    alpet_prices = get_alpet_prices()
    if alpet_prices:
        all_prices.extend(alpet_prices)
        print(f"Successfully fetched {len(alpet_prices)} records from Alpet.")
    else:
        print("Could not fetch prices from Alpet.")

    return all_prices

if __name__ == '__main__':
    # This allows running the scraper directly for testing
    from app.database import create_table, update_prices
    create_table()
    prices = fetch_all_prices()
    update_prices(prices)
    if prices:
        print(f"\\nTotal prices fetched and updated: {len(prices)}")
