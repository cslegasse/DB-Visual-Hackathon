from flask import Flask, jsonify, request
import yfinance as yf
from datetime import datetime

app = Flask(__name__)

@app.route('/api/data', methods=['GET'])
def get_data():
    ticker_symbol = request.args.get('ticker', 'AAPL')  
    ticker = yf.Ticker(ticker_symbol)
    
    # Fetch financial data
    quarterly_financials = ticker.quarterly_financials
    quarterly_cashflow = ticker.quarterly_cashflow
    balance_sheet = ticker.quarterly_balance_sheet

    # Fetch shares outstanding
    shares_outstanding = ticker.info.get('sharesOutstanding', 1)  
    
    # Revenue and Net Income
    revenue = quarterly_financials.loc['Total Revenue'] if 'Total Revenue' in quarterly_financials.index else 0
    net_income = quarterly_financials.loc['Net Income'] if 'Net Income' in quarterly_financials.index else 0
    free_cash_flow = quarterly_cashflow.loc['Free Cash Flow'] if 'Free Cash Flow' in quarterly_cashflow.index else 0
    
    # Assets and Liabilities
    goodwill = balance_sheet.loc['Goodwill'] if 'Goodwill' in balance_sheet.index else 0
    other_intangible_assets = balance_sheet.loc['Other Intangible Assets'] if 'Other Intangible Assets' in balance_sheet.index else 0
    total_assets = balance_sheet.loc['Total Assets'] if 'Total Assets' in balance_sheet.index else 0
    total_liabilities = balance_sheet.loc['Total Liabilities'] if 'Total Liabilities' in balance_sheet.index else 0
    
    # Calculate Tangible Book Value
    tangible_book_value = total_assets - goodwill - other_intangible_assets - total_liabilities
    
    # Per share metrics
    revenue_per_share = revenue / shares_outstanding
    net_income_per_share = net_income / shares_outstanding
    free_cash_flow_per_share = free_cash_flow / shares_outstanding
    tangible_book_value_per_share = tangible_book_value / shares_outstanding
    
    data = {
    'longName': ticker.info.get('longName', 'N/A'),
    'firstTradeDateEpochUtc': ticker.info.get('firstTradeDateEpochUtc', 'N/A'),
    'longBusinessSummary': ticker.info.get('longBusinessSummary', 'N/A'),
    'ticker': ticker_symbol,
    'revenue_per_share': revenue_per_share.tolist(),
    'net_income_per_share': net_income_per_share.tolist(),
    'free_cash_flow_per_share': free_cash_flow_per_share.tolist(),
    'tangible_book_value_per_share': tangible_book_value_per_share.tolist()
    }
    
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
