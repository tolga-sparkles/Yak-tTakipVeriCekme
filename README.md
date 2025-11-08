# Turkey Fuel Prices API

This project provides a simple API to retrieve fuel prices in Turkey. It scrapes data from fuel provider websites, stores it in a local SQLite database, and serves it through a FastAPI application.

## Current Status

**⚠️ This project is currently a proof-of-concept and has some limitations:**

*   **Single Provider:** Currently, it only scrapes data from **Alpet**. The initial goal was to include nine different providers, but significant technical challenges were encountered with the web structures of other sites (e.g., dynamic content loaded with JavaScript), making them difficult to scrape with the current toolset.
*   **Limited Fuel Types:** The Alpet scraper currently fetches prices for **Gasoline (Benzin)** and **Diesel (Motorin)**. LPG is not available on their public price page.
*   **No Historical Data:** The database only stores the latest fetched prices and overwrites them with each update.

## Features

*   **FastAPI-based:** A modern, fast web framework for building APIs.
*   **SQLite Database:** Lightweight, file-based database for easy setup.
*   **Web Scraping:** Uses `requests` and `BeautifulSoup` to fetch data.
*   **Automatic Daily Updates:** The data is automatically fetched once upon startup and then updated every 24 hours.
*   **Manual Update Endpoint:** You can trigger an update at any time.

## Setup and Installation

### Prerequisites

*   Python 3.9+
*   pip

### Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2.  **Install the required packages:**
    ```bash
    pip install fastapi uvicorn requests beautifulsoup4
    ```

### Running the Application

1.  **Start the API server:**
    From the project's root directory, run the following command:
    ```bash
    uvicorn main:app --app-dir app --host 0.0.0.0 --port 8000
    ```
    The server will start, perform an initial data scrape, and become available at `http://0.0.0.0:8000`.

## API Endpoints

### Get Prices for a City

*   **URL:** `/prices/{city_name}`
*   **Method:** `GET`
*   **Description:** Retrieves the latest fuel prices for the specified city. The `city_name` is case-insensitive.
*   **Example Request:**
    ```bash
    curl http://127.0.0.1:8000/prices/İSTANBUL
    ```
*   **Example Response:**
    ```json
    {
      "city": "İSTANBUL",
      "prices": [
        {
          "brand": "Alpet",
          "fuel_type": "Motorin",
          "price": 57.54,
          "last_updated": "2025-11-08 12:00:00"
        },
        {
          "brand": "Alpet",
          "fuel_type": "Benzin",
          "price": 53.64,
          "last_updated": "2025-11-08 12:00:00"
        }
      ]
    }
    ```

### Manually Trigger an Update

*   **URL:** `/update`
*   **Method:** `POST`
*   **Description:** Triggers the web scraping process in the background to update the price database.
*   **Example Request:**
    ```bash
    curl -X POST http://127.0.0.1:8000/update
    ```
*   **Example Response:**
    ```json
    {
      "message": "Data update process has been triggered in the background."
    }
    ```
