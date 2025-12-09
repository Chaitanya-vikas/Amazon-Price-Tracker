# 📉 E-Commerce Price Tracker & Analytics Pipeline

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://amazon-price-tracker-hi5mt96sttgja68qyynvyq.streamlit.app/)
![Python](https://img.shields.io/badge/Python-3.9-blue)
![SQLite](https://img.shields.io/badge/Database-SQLite-green)
![Status](https://img.shields.io/badge/Status-Active-success)

## 📌 Project Overview
This project is an end-to-end **Data Engineering (ETL) Pipeline** designed to monitor product price fluctuations on Amazon. It scrapes real-time data, persists it in a relational database, and visualizes historical trends via an interactive dashboard.

The system addresses the real-world challenge of **Dynamic Pricing** by providing a tool to track the lowest historical price of a product, enabling data-driven purchasing decisions.

### 🔗 [Live Dashboard Demo](https://amazon-price-tracker-hi5mt96sttgja68qyynvyq.streamlit.app/)
*(Note: If the dashboard is asleep, click "Wake up" and wait 30 seconds)*

---

## ⚙️ System Architecture

The project follows a **Hybrid Automation Architecture** to ensure reliable data ingestion while leveraging cloud visualization.

1.  **Extract (Scraper):** Python script (`tracker.py`) requests product pages using `BeautifulSoup` and custom User-Agent headers to mimic human behavior.
2.  **Transform (Cleaning):** Raw HTML is parsed to extract the Product Title and Price, handling currency formatting and timestamp generation.
3.  **Load (Database):** Data is normalized and stored in a local **SQLite** database (`amazon_prices.db`).
4.  **Sync & Visualize:** The database is synchronized with GitHub, triggering a **Streamlit Cloud** deployment to update the public dashboard.

---

## 🛠️ Tech Stack
* **Language:** Python 3.10
* **Web Scraping:** `BeautifulSoup4`, `Requests`
* **Database:** SQLite (Relational DB)
* **Visualization:** Streamlit, Pandas, Matplotlib
* **Version Control:** Git & GitHub

---

## ⚠️ Engineering Challenges & Solutions

### The "Cloud IP" Challenge
**Problem:** Initially, I deployed the scraping script to **GitHub Actions** for 24/7 cloud automation. However, Amazon's security systems block requests originating from Data Center IP ranges (like Azure/AWS), resulting in `403 Forbidden` errors.

**Solution:** I refactored the pipeline into a **Hybrid Model**:
* **Ingestion:** The scraping script runs on a **Residential IP** (Local System / Task Scheduler) to bypass bot detection naturally.
* **Visualization:** The processed data is pushed to the cloud, where Streamlit hosts the dashboard.
* *Future Improvement:* In a production environment, I would integrate a **Rotating Residential Proxy Network** (e.g., BrightData) to allow fully cloud-based scraping.

---

## 📊 Dashboard Features
The Streamlit Dashboard provides:
* **Current Price:** Real-time latest scraped price.
* **Lowest Price Record:** The minimum price ever observed (for deal hunting).
* **Price History Trend:** A line chart visualizing price volatility over time.

---

## 🚀 How to Run Locally

1.  **Clone the Repository**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/Amazon-Price-Tracker.git](https://github.com/YOUR_USERNAME/Amazon-Price-Tracker.git)
    cd Amazon-Price-Tracker
    ```

2.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the Scraper**
    ```bash
    python tracker.py
    ```
    *Output: `💾 Saved to SQL Database: ₹24,000`*

4.  **Launch the Dashboard**
    ```bash
    streamlit run dashboard.py
    ```

---

## 🔮 Future Improvements
* **Multi-Product Support:** Expand database schema to track multiple URLs simultaneously.
* **Email Alerts:** Integrate `smtplib` to send email notifications when the price drops below a threshold.
* **Proxy Rotation:** Implement free proxy rotation to attempt 100% cloud automation.

---
*Created by [Chaitanya Vikas vasamsetti] - Computer Science 2025*