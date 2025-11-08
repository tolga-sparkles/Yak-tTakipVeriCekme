import requests
from bs4 import BeautifulSoup

def get_alpet_prices():
    """
    Fetches fuel prices for all cities from Alpet's website.
    It first gets a list of all available cities and then scrapes the data for each one.
    """
    base_url = "https://www.alpet.com.tr/tr-TR/akaryakit-fiyatlari"
    all_prices = []

    try:
        # First, get the list of cities from the main page's dropdown menu
        print("Fetching the list of cities from Alpet...")
        main_page_response = requests.get(base_url, timeout=15)
        main_page_response.raise_for_status()
        soup = BeautifulSoup(main_page_response.content, 'html.parser')

        city_select = soup.find('select', {'name': 'city'})
        if not city_select:
            print("Could not find the city selection dropdown on Alpet's website.")
            return []

        cities = [option['value'] for option in city_select.find_all('option') if option['value']]
        print(f"Found {len(cities)} cities to scrape.")

        # Now, scrape prices for each city
        for city in cities:
            print(f"Scraping prices for: {city}...")
            city_url = f"{base_url}?city={city}"

            try:
                response = requests.get(city_url, timeout=10)
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                print(f"Could not fetch prices for {city}. Error: {e}")
                continue # Skip to the next city on error

            city_soup = BeautifulSoup(response.content, 'html.parser')

            price_table = city_soup.find('table')
            if not price_table:
                print(f"Price table not found for {city}.")
                continue

            rows = price_table.find_all('tr')[1:] # Skip header

            for row in rows:
                cols = row.find_all('td')
                if len(cols) >= 5:
                    scraped_city = cols[0].text.strip()
                    price_motorin_str = cols[2].text.strip().split()[0]
                    price_benzin_str = cols[4].text.strip().split()[0]

                    price_motorin = float(price_motorin_str.replace(',', '.'))
                    price_benzin = float(price_benzin_str.replace(',', '.'))

                    all_prices.append({'brand': 'Alpet', 'city': scraped_city, 'fuel_type': 'Motorin', 'price': price_motorin})
                    all_prices.append({'brand': 'Alpet', 'city': scraped_city, 'fuel_type': 'Benzin', 'price': price_benzin})

    except requests.exceptions.RequestException as e:
        print(f"Error fetching the main city list from Alpet: {e}")
    except Exception as e:
        print(f"An unexpected error occurred while parsing Alpet prices: {e}")

    return all_prices

if __name__ == "__main__":
    prices = get_alpet_prices()
    if prices:
        print(f"\\nSuccessfully fetched a total of {len(prices)} price records.")
        # You can add database update logic here for testing if needed
    else:
        print("No prices were found for Alpet.")
