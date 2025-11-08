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

---

# Türkiye Akaryakıt Fiyatları API'si

Bu proje, Türkiye'deki akaryakıt fiyatlarını almak için basit bir API sağlar. Akaryakıt sağlayıcılarının web sitelerinden veri çeker, bu verileri yerel bir SQLite veritabanında saklar ve bir FastAPI uygulaması aracılığıyla sunar.

## Mevcut Durum

**⚠️ Bu proje şu anda bir konsept kanıtlama (proof-of-concept) aşamasındadır ve bazı sınırlamalara sahiptir:**

*   **Tek Sağlayıcı:** Şu anda yalnızca **Alpet**'ten veri çekmektedir. Başlangıçtaki hedef dokuz farklı sağlayıcıyı dahil etmekti, ancak diğer sitelerin web yapılarında karşılaşılan önemli teknik zorluklar (örneğin, JavaScript ile dinamik olarak yüklenen içerik) mevcut araçlarla veri kazımayı zorlaştırdı.
*   **Sınırlı Yakıt Türleri:** Alpet kazıyıcısı şu anda **Benzin** ve **Motorin** fiyatlarını çekmektedir. LPG, halka açık fiyat sayfalarında mevcut değildir.
*   **Geçmiş Veri Yok:** Veritabanı yalnızca en son çekilen fiyatları saklar ve her güncellemede bu verilerin üzerine yazar.

## Özellikler

*   **FastAPI Tabanlı:** API oluşturmak için modern ve hızlı bir web çatısı.
*   **SQLite Veritabanı:** Kolay kurulum için hafif, dosya tabanlı bir veritabanı.
*   **Web Kazıma (Scraping):** Veri çekmek için `requests` and `BeautifulSoup` kullanır.
*   **Otomatik Günlük Güncellemeler:** Veriler sunucu başladığında bir kez otomatik olarak çekilir ve ardından her 24 saatte bir güncellenir.
*   **Manuel Güncelleme Endpoint'i:** İstediğiniz zaman bir güncellemeyi tetikleyebilirsiniz.

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
    pip install fastapi uvicorn requests beautifulsoup4
    ```

### Uygulamayı Çalıştırma

1.  **API sunucusunu başlatın:**
    Projenin kök dizininden aşağıdaki komutu çalıştırın:
    ```bash
    uvicorn main:app --app-dir app --host 0.0.0.0 --port 8000
    ```
    Sunucu başlayacak, ilk veri kazıma işlemini gerçekleştirecek ve `http://0.0.0.0:8000` adresinde erişilebilir olacaktır.

## API Endpoint'leri

### Şehre Göre Fiyatları Al

*   **URL:** `/prices/{sehir_adi}`
*   **Metot:** `GET`
*   **Açıklama:** Belirtilen şehir için en son akaryakıt fiyatlarını getirir. `sehir_adi` büyük/küçük harfe duyarlı değildir.
*   **Örnek İstek:**
    ```bash
    curl http://127.0.0.1:8000/prices/İSTANBUL
    ```
*   **Örnek Yanıt:**
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

### Manuel Güncelleme Tetikleme

*   **URL:** `/update`
*   **Metot:** `POST`
*   **Açıklama:** Fiyat veritabanını güncellemek için web kazıma işlemini arka planda tetikler.
*   **Örnek İstek:**
    ```bash
    curl -X POST http://127.0.0.1:8000/update
    ```
*   **Örnek Yanıt:**
    ```json
    {
      "message": "Data update process has been triggered in the background."
    }
    ```
