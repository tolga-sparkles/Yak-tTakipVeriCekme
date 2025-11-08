import requests
from bs4 import BeautifulSoup

def get_alpet_prices():
    """
    Fetches fuel prices from Alpet's website by parsing the HTML table.
    """
    url = "https://www.alpet.com.tr/tr-TR/akaryakit-fiyatlari"
    prices = []

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from {url}: {e}")
        return []

    soup = BeautifulSoup(response.content, 'html.parser')

    try:
        # Find the table containing the prices. It should be the only table.
        price_table = soup.find('table')

        if not price_table:
            print("Price table not found on Alpet's website.")
            return []

        # Get all rows from the table, skipping the header row.
        rows = price_table.find_all('tr')[1:]

        for row in rows:
            cols = row.find_all('td')

            if len(cols) >= 5: # Ensure the row has enough columns
                city = cols[0].text.strip()
                # District is in cols[1], we can ignore it for now.

                # Prices are in the next columns.
                # Motorin price is in the 3rd column (index 2).
                # 95 Oktan Kurşunsuz (Benzin) is in the 5th column (index 4).

                price_motorin_str = cols[2].text.strip().split()[0]
                price_benzin_str = cols[4].text.strip().split()[0]

                # Convert price strings to float.
                price_motorin = float(price_motorin_str.replace(',', '.'))
                price_benzin = float(price_benzin_str.replace(',', '.'))

                prices.append({'brand': 'Alpet', 'city': city, 'fuel_type': 'Motorin', 'price': price_motorin})
                prices.append({'brand': 'Alpet', 'city': city, 'fuel_type': 'Benzin', 'price': price_benzin})

    except Exception as e:
        print(f"An error occurred while parsing the Alpet price table: {e}")

    return prices

if __name__ == "__main__":
    alpet_prices = get_alpet_prices()
    if alpet_prices:
        for price in alpet_prices:
            print(price)
    else:
        print("No prices found for Alpet.")
