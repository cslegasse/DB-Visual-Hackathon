import streamlit as st
import requests

st.title('Streamlit Frontend for Flask API')

api_url = 'http://localhost:5000/api/data'
response = requests.get(api_url)

if response.status_code == 200:
    data = response.json()
    st.write('Message from Flask API:')
    st.write(data['message'])
    st.write('Data from Flask API:')
    st.write(data['data'])
else:
    st.write('Error: Could not connect to the Flask API')
