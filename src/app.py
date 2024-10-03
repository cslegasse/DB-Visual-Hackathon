from flask import Flask, jsonify, request
import yfinance as yf

app = Flask(__name__)

@app.route('/api/data', methods=['GET'])
def get_data():
    ticker_symbol = request.args.get('ticker', 'AAPL')
    ticker = yf.Ticker(ticker_symbol)

    # Fetch company information
    try:
        # Get company information
        company_name = ticker.info.get("longName", "N/A")
        mission_statement = ticker.info.get("missionStatement", "Mission statement not available.")
        company_description = ticker.info.get("longBusinessSummary", "Description not available.")

        # Get financial data
        quarterly_financials = ticker.quarterly_financials
        shares_outstanding = ticker.info['sharesOutstanding']

        revenue = quarterly_financials.loc['Total Revenue']
        net_income = quarterly_financials.loc['Net Income']
        free_cash_flow = ticker.quarterly_cashflow.loc['Free Cash Flow']

        revenue_per_share = revenue / shares_outstanding
        net_income_per_share = net_income / shares_outstanding
        free_cash_flow_per_share = free_cash_flow / shares_outstanding

        data = {
            'ticker': ticker_symbol,
            'company_name': company_name,
            'mission_statement': mission_statement,
            'company_description': company_description,
            'revenue_per_share': revenue_per_share,
            'net_income_per_share': net_income_per_share,
            'free_cash_flow_per_share': free_cash_flow_per_share,
        }
    except Exception as e:
        data = {
            'error': str(e)
        }

    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
