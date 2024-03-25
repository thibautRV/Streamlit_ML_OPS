from prometheus_client import Counter
import streamlit as st
import pandas as pd

# Prometheus counter to track button clicks
button_click_counter = Counter('button_clicks_total', 'Total number of button clicks')

# Streamlit app title
st.title('Housing Analysis')

# Function to load data
@st.cache  # Add caching for faster reloading
def load_data(nrows):
    data = pd.read_csv("housing.csv", nrows=nrows)
    return data

# Load the data
data_load_state = st.text('Loading data...')
data = load_data(10000)
data_load_state.text('Loading data...done!')

# Display raw data
st.subheader('Raw data')
st.write(data)

# Button to increment counter
if st.button('Click me'):
    button_click_counter.inc()  # Increment Prometheus counter when button is clicked
    st.write('Button clicked!')
