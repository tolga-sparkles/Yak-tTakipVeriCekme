import sqlite3
from datetime import datetime

DB_NAME = 'fuel_prices.db'

def get_db_connection():
    """Establishes a connection to the SQLite database."""
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def create_table():
    """Creates the 'prices' table if it does not exist."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS prices (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            brand TEXT NOT NULL,
            city TEXT NOT NULL,
            fuel_type TEXT NOT NULL,
            price REAL NOT NULL,
            last_updated TEXT NOT NULL,
            UNIQUE(brand, city, fuel_type)
        )
    ''')
    conn.commit()
    conn.close()
    print("Database table created or already exists.")

def update_prices(price_data):
    """
    Updates the database with a list of price data.
    Uses INSERT OR REPLACE to either insert a new record or replace an existing one.
    """
    if not price_data:
        print("No price data provided to update.")
        return

    conn = get_db_connection()
    cursor = conn.cursor()

    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    for item in price_data:
        cursor.execute('''
            INSERT OR REPLACE INTO prices (brand, city, fuel_type, price, last_updated)
            VALUES (?, ?, ?, ?, ?)
        ''', (item['brand'], item['city'], item['fuel_type'], item['price'], now))

    conn.commit()
    conn.close()
    print(f"Updated {len(price_data)} records in the database.")

def get_prices_by_city(city_name):
    """Retrieves all fuel prices for a given city from the database."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT brand, fuel_type, price, last_updated FROM prices WHERE city = ?', (city_name.upper(),))
    prices = cursor.fetchall()
    conn.close()
    return [dict(row) for row in prices]

def get_all_distinct_cities():
    """Retrieves a sorted list of all unique city names from the database."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT DISTINCT city FROM prices ORDER BY city ASC')
    cities = cursor.fetchall()
    conn.close()
    return [row['city'] for row in cities]

if __name__ == '__main__':
    create_table()
