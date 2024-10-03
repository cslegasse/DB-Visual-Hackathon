import streamlit as st
import requests
import plotly.graph_objects as go

st.title('Financial Data Dashboard')

st.sidebar.header('User Input')
ticker = st.sidebar.text_input('Enter a Stock Ticker:', 'AAPL')

api_url = f'http://localhost:5000/api/data?ticker={ticker}'

response = requests.get(api_url)

if response.status_code == 200:
    data = response.json()
    st.write(f"**Showing data for: {data['ticker']}**")

    metrics = ['Revenue Per Share', 'Net Income Per Share', 'Free Cash Flow Per Share', 'Tangible Book Value Per Share']
    values = [
        data['revenue_per_share'],
        data['net_income_per_share'],
        data['free_cash_flow_per_share'],
        data['tangible_book_value_per_share'],
    ]

    # Create a Plotly bar chart
    fig = go.Figure(data=[go.Bar(x=metrics, y=values, text=values, textposition='auto')])
    fig.update_layout(title=f'Financial Overview for {ticker}', yaxis_title='Per Share Values')

    st.plotly_chart(fig)

else:
    st.error('Error: Could not connect to the Flask API')
