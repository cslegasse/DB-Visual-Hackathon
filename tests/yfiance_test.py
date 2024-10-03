import yfinance as yf
from datetime import datetime

# Return the company name, mission statement, and ticker symbol for a given ticker symbol
def get_company_info(ticker_symbol):
    ticker = yf.Ticker(ticker_symbol)
    return ticker.info.get('shortName', 'N/A'), ticker.info.get('longBusinessSummary', 'N/A'), ticker.info.get('firstTradeDateEpochUtc', 'N/A'), ticker.info.get('sharesOutstanding', 1)

# Test the function with a ticker symbol
ticker_symbol = 'AAPL'
company_name, mission_statement, ipo_date, shares_outstanding = get_company_info(ticker_symbol)

print(f"Company Name: {company_name}")
print(f"Mission Statement: {mission_statement}")

# Convert EpochUtc to readable time
if isinstance(ipo_date, (int, float)):
    ipo_date = datetime.utcfromtimestamp(ipo_date).strftime('%Y-%m-%d')

print(f"IPO Date: {ipo_date}")
print(f"Shares Outstanding: {shares_outstanding}")
