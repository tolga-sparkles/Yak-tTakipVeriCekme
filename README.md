# Turkey Fuel Prices API

This project provides a simple API and a web interface to retrieve fuel prices in Turkey. It scrapes data from fuel provider websites, stores it in a local SQLite database, and serves it through a FastAPI application.

## Features

*   **Web Interface:** A clean and simple UI to view prices by city.
*   **FastAPI-based API:** A modern, fast web framework for building APIs.
*   **SQLite Database:** Lightweight, file-based database for easy setup.
*   **Web Scraping:** Uses `requests` and `BeautifulSoup` to fetch data.
*   **Automatic Daily Updates:** The data is automatically fetched once upon startup and then updated every 24 hours.
*   **Manual Update Endpoint:** You can trigger an update at any time via the API.

## Current Status

**⚠️ This project is currently a proof-of-concept and has some limitations:**

*   **Single Provider:** Currently, it only scrapes data from **Alpet**. The initial goal was to include nine different providers, but significant technical challenges were encountered with the web structures of other sites (e.g., dynamic content loaded with JavaScript).
*   **Limited Fuel Types:** The Alpet scraper currently fetches prices for **Gasoline (Benzin)** and **Diesel (Motorin)**. LPG is not available on their public price page.
*   **No Historical Data:** The database only stores the latest fetched prices and overwrites them with each update.

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
    pip install fastapi uvicorn requests beautifulsoup4 jinja2
    ```

### Running the Application

1.  **Start the server:**
    From the project's root directory, run the following command:
    ```bash
    uvicorn main:app --app-dir app --host 0.0.0.0 --port 8000
    ```
2.  **Access the Web Interface:**
    Open your browser and navigate to `http://127.0.0.1:8000`.

## API Endpoints

The API is intended for programmatic access. For human-readable output, please use the web interface.

### Get Prices for a City

*   **URL:** `/api/prices/{city_name}`
*   **Method:** `GET`
*   **Description:** Retrieves the latest fuel prices for the specified city.
*   **Example Request:**
    ```bash
    curl http://127.0.0.1:8000/api/prices/İSTANBUL
    ```

### Manually Trigger an Update

*   **URL:** `/api/update`
*   **Method:** `POST`
*   **Description:** Triggers the web scraping process in the background.
*   **Example Request:**
    ```bash
    curl -X POST http://127.0.0.1:8000/api/update
    ```

---

# Türkiye Akaryakıt Fiyatları API'si ve Web Arayüzü

Bu proje, Türkiye'deki akaryakıt fiyatlarını almak için basit bir web arayüzü ve API sağlar. Akaryakıt sağlayıcılarının web sitelerinden veri çeker, bu verileri yerel bir SQLite veritabanında saklar ve bir FastAPI uygulaması aracılığıyla sunar.

## Özellikler

*   **Web Arayüzü:** Şehre göre fiyatları görüntülemek için temiz ve basit bir arayüz.
*   **FastAPI Tabanlı API:** API oluşturmak için modern ve hızlı bir web çatısı.
*   **SQLite Veritabanı:** Kolay kurulum için hafif, dosya tabanlı bir veritabanı.
*   **Web Kazıma (Scraping):** Veri çekmek için `requests` ve `BeautifulSoup` kullanır.
*   **Otomatik Günlük Güncellemeler:** Veriler sunucu başladığında bir kez otomatik olarak çekilir ve ardından her 24 saatte bir güncellenir.
*   **Manuel Güncelleme Endpoint'i:** API üzerinden istediğiniz zaman bir güncellemeyi tetikleyebilirsiniz.

## Mevcut Durum

**⚠️ Bu proje şu anda bir konsept kanıtlama (proof-of-concept) aşamasındadır ve bazı sınırlamalara sahiptir:**

*   **Tek Sağlayıcı:** Şu anda yalnızca **Alpet**'ten veri çekmektedir.
*   **Sınırlı Yakıt Türleri:** Sadece **Benzin** ve **Motorin** fiyatlarını çekmektedir.
*   **Geçmiş Veri Yok:** Veritabanı yalnızca en son çekilen fiyatları saklar.

## Kurulum ve Çalıştırma

### Ön Gereksinimler

*   Python 3.9+
*   pip

### Kurulum

1.  **Projeyi klonlayın:**
    ```bash
    git clone <proje-url>
    cd <proje-dizini>
    ```

2.  **Gerekli paketleri yükleyin:**
    ```bash
    pip install fastapi uvicorn requests beautifulsoup4 jinja2
    ```

### Uygulamayı Çalıştırma

1.  **Sunucuyu başlatın:**
    Projenin kök dizininden aşağıdaki komutu çalıştırın:
    ```bash
    uvicorn main:app --app-dir app --host 0.0.0.0 --port 8000
    ```
2.  **Web Arayüzüne Erişin:**
    Tarayıcınızı açın ve `http://127.0.0.1:8000` adresine gidin.

## API Endpoint'leri

API, programatik erişim için tasarlanmıştır. İnsan tarafından okunabilir bir çıktı için lütfen web arayüzünü kullanın.

### Şehre Göre Fiyatları Al

*   **URL:** `/api/prices/{sehir_adi}`
*   **Metot:** `GET`
*   **Örnek İstek:**
    ```bash
    curl http://127.0.0.1:8000/api/prices/İSTANBUL
    ```

### Manuel Güncelleme Tetikleme

*   **URL:** `/api/update`
*   **Metot:** `POST`
*   **Örnek İstek:**
    ```bash
    curl -X POST http://127.0.0.1:8000/api/update
    ```
