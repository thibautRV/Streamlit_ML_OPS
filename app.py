from prometheus_client import Counter
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Prometheus counter to track button clicks
button_click_counter = Counter('specific_button_clicks_total', 'Total number of clicks on the specific button')

# Streamlit app title
st.title('Housing Analysis')

# Function to load data
@st.cache  # Add caching for faster reloading
def load_data(nrows):
    data = pd.read_csv("housing.csv", nrows=nrows)
    return data

# Load the data
data_load_state = st.text('Loading data...')
df = load_data()
data_load_state.text('Loading data...done!')

# Sidebar with options
st.sidebar.header('Options')
selected_viz = st.sidebar.selectbox('Select Visualization', ['Histogram', 'Scatter Plot'])


# Button to increment counter
if st.button('Specific Button'):
    button_click_counter.inc()  # Increment Prometheus counter when specific button is clicked
    st.write('Specific button clicked!')

# Display selected visualization
if selected_viz == 'Histogram':
    st.subheader('Histogram')
    selected_column = st.selectbox('Select Column for Histogram', df.columns)
    plt.hist(df[selected_column], bins=20)
    st.pyplot()

elif selected_viz == 'Scatter Plot':
    st.subheader('Scatter Plot')
    x_column = st.selectbox('Select X-Axis Column', df.columns)
    y_column = st.selectbox('Select Y-Axis Column', df.columns)
    plt.scatter(df[x_column], df[y_column])
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    st.pyplot()


    