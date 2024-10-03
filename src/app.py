from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample financial data for demonstration
financial_data = {
    'AAPL': {
        'revenue_per_share': [4.50],
        'net_income_per_share': [3.00],
        'free_cash_flow_per_share': [2.00],
        'tangible_book_value_per_share': [20.00]
    },
    'MSFT': {
        'revenue_per_share': [7.50],
        'net_income_per_share': [6.00],
        'free_cash_flow_per_share': [5.00],
        'tangible_book_value_per_share': [25.00]
    }
}

@app.route('/api/data', methods=['GET'])
def get_financial_data():
    ticker = request.args.get('ticker').upper()  # Get the ticker from the request
    data = financial_data.get(ticker, {})  # Fetch data for the ticker
    if data:
        data['ticker'] = ticker  # Add the ticker to the response
        return jsonify(data)  # Return the data as JSON
    else:
        return jsonify({'error': 'Ticker not found'}), 404  # Return an error if ticker not found

if __name__ == '__main__':
    app.run(debug=True)
