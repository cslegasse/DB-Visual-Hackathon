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
    if data.get('error'):
        st.error(f"Error: {data['error']}. Please enter a valid ticker symbol.")

    # Access values safely
    def get_value(key, index=0):
        value = data.get(key, [0])  # Default to a list with a single zero
        if isinstance(value, list):
            return float(value[index]) if len(value) > index else 0
        return float(value)

    def calculate_change(current_value, previous_value):
        if previous_value == 0:
            return 0
        change = ((current_value - previous_value) / previous_value) * 100
        return round(change, 2)

    revenue_per_share = round(get_value('revenue_per_share'),2)
    net_income_per_share = round(get_value('net_income_per_share'),2)
    free_cash_flow_per_share = round(get_value('free_cash_flow_per_share'),2)
    tangible_book_value_per_share = round(get_value('tangible_book_value_per_share'),2)

    st.sidebar.subheader('Company Information')
    st.sidebar.write(f"**Company Name: {data.get('longName', 'Lorem ipsum dolor.')}**")
    st.sidebar.write(f"**IPO Date: {datetime.utcfromtimestamp(data.get('firstTradeDateEpochUtc', 0)).strftime('%B %d, %Y')}**")
    st.sidebar.markdown("<div><strong>Mission Statement:</strong> <span class='mission-statement'>{}</span></div>".format(data.get('longBusinessSummary', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.')), unsafe_allow_html=True)
    
    # Create a Plotly bar chart
    metrics = {
        "Revenue Per Share": revenue_per_share,
        "Net Income Per Share": net_income_per_share,
        "Free Cash Flow Per Share": free_cash_flow_per_share,
        "Tangible Book Value Per Share": tangible_book_value_per_share
    }    

    # Get current and previous values
    current_revenue_per_share = round(get_value('revenue_per_share'), 2)
    previous_revenue_per_share = round(get_value('revenue_per_share', index=1), 2)
    current_net_income_per_share = round(get_value('net_income_per_share'), 2)
    previous_net_income_per_share = round(get_value('net_income_per_share', index=1), 2)
    current_free_cash_flow_per_share = round(get_value('free_cash_flow_per_share'), 2)
    previous_free_cash_flow_per_share = round(get_value('free_cash_flow_per_share', index=1), 2)
    current_tangible_book_value_per_share = round(get_value('tangible_book_value_per_share'), 2)
    previous_tangible_book_value_per_share = round(get_value('tangible_book_value_per_share', index=1), 2)

    # Calculate changes
    revenue_change = calculate_change(current_revenue_per_share, previous_revenue_per_share)
    net_income_change = calculate_change(current_net_income_per_share, previous_net_income_per_share)
    free_cash_flow_change = calculate_change(current_free_cash_flow_per_share, previous_free_cash_flow_per_share)
    tangible_book_value_change = calculate_change(current_tangible_book_value_per_share, previous_tangible_book_value_per_share)

    metrics = {
        "Revenue Per Share": (current_revenue_per_share, revenue_change),
        "Net Income Per Share": (current_net_income_per_share, net_income_change),
        "Free Cash Flow Per Share": (current_free_cash_flow_per_share, free_cash_flow_change),
        "Tangible Book Value Per Share": (current_tangible_book_value_per_share, tangible_book_value_change)
    }    

    metrics_container = st.container()
    metrics_container.subheader(f"Financial Metrics for: {data['ticker']}")

    cols = st.columns(len(metrics))
    for col, (label, (value, change)) in zip(cols, metrics.items()):
        with col:
            if isinstance(value, (int, float)):
                formatted_value = f"${value:,.2f}"
                st.metric(label=label, value=formatted_value, delta=f"{change:.2f}%")
            else:
                st.metric(label=label, value="N/A", delta=None)

    # Prepare data for the bar chart
    metrics_names = list(metrics.keys())
    current_values = [value for value, _ in metrics.values()]
    previous_values = [get_value(key, index=1) for key in metrics.keys()]

    # Create a horizontal stacked bar chart
    fig = go.Figure(data=[
    go.Bar(
        y=metrics_names,
        x=previous_values,
        orientation='h',
        name='Previous',
        text=[f"${value:,.2f}" for value in previous_values],
        textposition='inside',
        insidetextanchor='start',
        marker_color='#CCCCCC'  # Light gray for previous values
    ),
    go.Bar(
        y=metrics_names,
        x=current_values,
        orientation='h',
        name='Current',
        text=[f"${value:,.2f}" for value in current_values],
        textposition='outside',
        marker_color='#0018A8'  # Deutsche Bank blue for current values
        )
    ])

    fig.update_layout(
    title=f'Financial Overview for {ticker}',
    xaxis_title='Per Share Values ($)',
    height=400,
    margin=dict(l=0, r=0, t=40, b=0),
    barmode='stack',
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1
    )
    )

    # Format x-axis labels
    fig.update_xaxes(tickprefix='$', tickformat=',.0f')

    # Adjust bar width and add space between bars
    fig.update_traces(width=0.6)

    # Ensure the x-axis starts at 0
    fig.update_xaxes(range=[0, max(max(current_values), max(previous_values)) * 1.1])

    st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})

elif response.status_code == 500:
    st.error(f"Error: Ticker symbol '{ticker}' not found. Please enter a valid ticker symbol.")

else:
    st.error(f'Error: Could not connect to the Flask API. Status code: {response.status_code}')

