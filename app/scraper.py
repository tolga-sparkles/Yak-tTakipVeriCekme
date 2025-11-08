from scrapers.alpet_scraper import get_alpet_prices

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
    prices = fetch_all_prices()
    if prices:
        print(f"\\nTotal prices fetched: {len(prices)}")
        # Print a small sample
        for price in prices[:5]:
            print(price)
