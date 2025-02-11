# Cryptocurrency Live Analysis

## Overview
This project fetches and analyzes live cryptocurrency data from the CoinGecko API, providing insights into the top 50 cryptocurrencies based on market capitalization, current price, 24-hour trading volume, and percentage price changes. The analysis is automated and updated every 5 minutes, with results stored in an Excel sheet for real-time monitoring.

## Features
- Fetch live cryptocurrency data from the CoinGecko API.
Analyze key metrics:
   #Top 5 cryptocurrencies by market capitalization.
   #Average price of the top 50 cryptocurrencies.
   #Highest and lowest 24-hour percentage price changes.
Store live updates in an Excel sheet for continuous tracking.
Perform basic analysis to identify market trends and opportunities.

## Key Insights
- Top 5 Cryptocurrencies by Market Capitalization:
  1. Bitcoin: $1,904B
  2. Ethereum: $317B
  3. Tether: $141B
  4. XRP: $140B
  5. Solana: $96B
- Average Price of Top 50 Cryptocurrencies: $4,165.32
- Highest 24-hour Percentage Change: Cardano (+9.15%)
- Lowest 24-hour Percentage Change: Aptos (-4.75%)

## Technologies Used
1. Python
2. Pandas
3. OpenPyXL
4. CoinGecko API

## How to Use
1. Clone the repository:
   ```bash
   git clone <repository-link>
   cd <repository-folder>
   ```
2. Install dependencies:
   ```bash
   pip install pandas openpyxl requests
   ```
3. Run the script:
   ```bash
   python main.py
   ```
4. Open the `crypto_live_data.xlsx` file to view live updates.

## File Structure
- `main.py`: Script for fetching, analyzing, and saving live cryptocurrency data.
- `crypto_live_data.xlsx`: Excel file updated with real-time cryptocurrency data.
- `README.md`: Documentation for the project.

## Future Enhancements
- Add visualization for live trends (e.g., charts or graphs).
- Include additional analysis metrics like moving averages or risk indicators.
- Expand data coverage to include more cryptocurrencies or historical data.
