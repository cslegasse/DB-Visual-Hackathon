import streamlit as st
import requests
import plotly.graph_objects as go
import numpy as np  # Import numpy to handle NaN values

st.title('Financial Data Dashboard')

st.sidebar.header('User Input')
ticker = st.sidebar.text_input('Enter a Stock Ticker:', 'AAPL')

api_url = f'http://localhost:5000/api/data?ticker={ticker}'

response = requests.get(api_url)

if response.status_code == 200:
    data = response.json()
    st.write(f"**Showing data for: {data['ticker']}**")
    
    # Display company information
    st.subheader("Company Information")
    st.write(f"**Company Name:** {data.get('company_name', 'N/A')}")
    st.write(f"**Mission Statement:** {data.get('mission_statement', 'N/A')}")
    st.write(f"**Description:** {data.get('company_description', 'N/A')}")

    # Check for error
    if 'error' in data:
        st.error(f"Error: {data['error']}")
    else:
        # Financial metrics
        def get_value(key):
            value = data.get(key, [0])  
            if isinstance(value, list):
                # Handle NaN and return the first valid float or 0 if all are invalid
                return float(value[0]) if len(value) > 0 and not np.isnan(value[0]) else 0
            return float(value) if value is not None else 0

        revenue_per_share = get_value('revenue_per_share')
        net_income_per_share = get_value('net_income_per_share')
        free_cash_flow_per_share = get_value('free_cash_flow_per_share')
        tangible_book_value_per_share = get_value('tangible_book_value_per_share')

        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric(label="Revenue Per Share", value=revenue_per_share)
        with col2:
            st.metric(label="Net Income Per Share", value=net_income_per_share)
        with col3:
            st.metric(label="Free Cash Flow Per Share", value=free_cash_flow_per_share)
        with col4:
            st.metric(label="Tangible Book Value Per Share", value=tangible_book_value_per_share)




        # Create bar chart
        metrics = ['Revenue Per Share', 'Net Income Per Share', 'Free Cash Flow Per Share', 'Tangible Book Value Per Share']
        values = [revenue_per_share, net_income_per_share, free_cash_flow_per_share, tangible_book_value_per_share]
        fig = go.Figure(data=[go.Bar(x=metrics, y=values, text=values, textposition='auto')])
        fig.update_layout(title=f'Financial Overview for {ticker}', yaxis_title='Per Share Values')

        st.plotly_chart(fig)

else:
    st.error('Error: Could not connect to the Flask API')
