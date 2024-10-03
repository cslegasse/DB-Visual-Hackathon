import streamlit as st
import requests

st.title('Streamlit Frontend for Flask API')

api_url = 'http://localhost:5000/api/data'

try:
    response = requests.get(api_url, timeout=5)
    response.raise_for_status()  # Raises an HTTPError for bad responses

    data = response.json()
    st.success('Successfully connected to Flask API')
    st.write('Message from Flask API:')
    st.write(data['message'])
    st.write('Data from Flask API:')
    st.write(data['data'])

except requests.exceptions.RequestException as e:
    st.error(f'Error: Could not connect to the Flask API. {str(e)}')
    st.write('Make sure the Flask backend is running on http://localhost:5000')

st.write('---')
st.write('Debug Information:')
st.write(f'API URL: {api_url}')