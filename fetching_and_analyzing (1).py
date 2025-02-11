# -*- coding: utf-8 -*-
"""Fetching and Analyzing

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Ml0wK-okNPFd4Z47Uh2joCeYFbw11f12
"""

import requests
import pandas as pd
import time
from openpyxl import load_workbook

EXCEL_FILE = "crypto_live_data.xlsx"

def fetch_crypto_data():
    """Fetch live cryptocurrency data from CoinGecko API."""
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 50,
        "page": 1,
        "sparkline": "false"
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: Unable to fetch data. Status code {response.status_code}")
        return []

def process_data(data):
    """Process the data into a structured DataFrame."""
    df = pd.DataFrame(data)
    df = df[["name", "symbol", "current_price", "market_cap", "total_volume", "price_change_percentage_24h"]]
    df.columns = ["Cryptocurrency Name", "Symbol", "Current Price (USD)", "Market Capitalization",
                  "24h Trading Volume", "Price Change (24h, %)"]
    return df

def analyze_data(df):
    """Perform basic analysis on the data."""
    # Top 5 cryptocurrencies by market capitalization
    top_5 = df.sort_values(by="Market Capitalization", ascending=False).head(5)
    print("Top 5 Cryptocurrencies by Market Cap:", top_5[["Cryptocurrency Name", "Market Capitalization"]])

    # Average price of top 50 cryptocurrencies
    avg_price = df["Current Price (USD)"].mean()
    print(f"Average Price of Top 50 Cryptocurrencies: ${avg_price:.2f}")

    # Highest and lowest 24-hour percentage price change
    highest_change = df.loc[df["Price Change (24h, %)"] == df["Price Change (24h, %)"] .max()]
    lowest_change = df.loc[df["Price Change (24h, %)"] == df["Price Change (24h, %)"] .min()]
    print("Highest 24-hour Percentage Change:", highest_change[["Cryptocurrency Name", "Price Change (24h, %)"]])
    print("Lowest 24-hour Percentage Change:", lowest_change[["Cryptocurrency Name", "Price Change (24h, %)"]])

def update_excel(df):
    """Update or create an Excel sheet with the live data."""
    try:
        book = load_workbook(EXCEL_FILE)
        writer = pd.ExcelWriter(EXCEL_FILE, engine="openpyxl", mode="a", if_sheet_exists="replace")
    except FileNotFoundError:
        writer = pd.ExcelWriter(EXCEL_FILE, engine="openpyxl")

    df.to_excel(writer, index=False, sheet_name="Live Data")
    writer.close()
    print("Excel updated!")

# Main loop for live updates
print("Starting live cryptocurrency data fetching...")
while True:
    data = fetch_crypto_data()
    if data:
        df = process_data(data)
        analyze_data(df)
        update_excel(df)
    time.sleep(300)  # Wait for 5 minutes before fetching again