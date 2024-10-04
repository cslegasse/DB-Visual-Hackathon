import streamlit as st
import requests
import plotly.graph_objects as go
from datetime import datetime

# Configure the page
st.set_page_config(
    page_title="Financial Data Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Load custom CSS
with open('src/assets/style.css', 'r') as f:
    custom_css = f'<style>{f.read()}</style>'

# Load SVG as a string
with open('src/assets/Deutsche_Bank_logo_without_wordmark.svg', 'r') as f:
    svg_string = f.read()

# Apply custom CSS
st.markdown(custom_css, unsafe_allow_html=True)

# Add SVG as an image
st.markdown(f'<div class="logo-container">{svg_string}</div>', unsafe_allow_html=True)

st.title('Financial Data Dashboard')

st.sidebar.header('User Input')
ticker = st.sidebar.text_input('Enter a Stock Ticker:', 'AAPL')

api_url = f'http://localhost:5000/api/data?ticker={ticker}'

response = requests.get(api_url)

if response.status_code == 200:
    data = response.json()
    st.write(f"**Showing data for: {data['ticker']}**")

    # Access values safely
    def get_value(key):
        value = data.get(key, [0])  # Default to a list with a single zero
        if isinstance(value, list):
            return float(value[0]) if len(value) > 0 else 0
        return float(value)
    
    revenue_per_share = round(get_value('revenue_per_share'),2)
    net_income_per_share = round(get_value('net_income_per_share'),2)
    free_cash_flow_per_share = round(get_value('free_cash_flow_per_share'),2)
    tangible_book_value_per_share = round(get_value('tangible_book_value_per_share'),2)


# TODO: Debug why the data is not showing up
    st.sidebar.subheader('Company Information')
    st.sidebar.write(f"**Company Name: {data.get('longName', 'Lorem ipsum dolor.')}**")
    st.sidebar.write(f"**IPO Date: {datetime.utcfromtimestamp(data.get('firstTradeDateEpochUtc', 0)).strftime('%Y-%m-%d')}**")
    st.sidebar.markdown(f"<div class='mission-statement'>Mission Statement: {data.get('longBusinessSummary', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.')}</div>", unsafe_allow_html=True)

    # Create a Plotly bar chart
    metrics = {
        "Revenue Per Share": revenue_per_share,
        "Net Income Per Share": net_income_per_share,
        "Free Cash Flow Per Share": free_cash_flow_per_share,
        "Tangible Book Value Per Share": tangible_book_value_per_share
    }    

    metrics_container = st.container()
    metrics_container.subheader("Financial Metrics")

    cols = st.columns(len(metrics))
    for col, (label, value) in zip(cols, metrics.items()):
        with col:
            # Check if value is valid and format it, else show a default message
            if isinstance(value, (int, float)):  # Ensure the value is numeric
                formatted_value = f"${value:,.2f}"  # Format as currency
            else:
                formatted_value = "N/A"  # Default message for non-numeric values
            
            st.metric(label=label, value=formatted_value, delta=None)

    # Prepare data for the bar chart
    metrics_names = list(metrics.keys())
    values = list(metrics.values())

    # Create a Plotly bar chart
    fig = go.Figure(data=[go.Bar(x=metrics_names, y=values, text=values, textposition='auto')])
    fig.update_layout(
        title=f'Financial Overview for {ticker}',
        yaxis_title='Per Share Values',
        plot_bgcolor='rgba(0,0,0,0)',  
        xaxis=dict(showgrid=False), 
        yaxis=dict(showgrid=True, gridcolor='lightgrey'),  
    )


    st.plotly_chart(fig)

else:
    st.error('Error: Could not connect to the Flask API')
