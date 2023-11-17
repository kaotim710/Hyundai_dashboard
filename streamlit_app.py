import streamlit as st
import pandas as pd
import plost

st.set_page_config(layout='wide', initial_sidebar_state='expanded')

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Sidebar parameter
st.sidebar.header('Dashboard `Status: Online`')

st.sidebar.subheader('Heat map parameter')
time_hist_color = st.sidebar.selectbox(
    'Color by', ('temp_data1', 'temp_data2'))

st.sidebar.subheader('Line chart parameters')
# First sidebar
plot_data1 = st.sidebar.multiselect(
    'Select data', ['Sensor1_temp', 'Sensor2_temp'], ['Sensor1_temp', 'Sensor2_temp'])
plot_height1 = st.sidebar.slider('Specify plot height', 100, 600, 500)

# Second sidebar
# plot_data2 = st.sidebar.multiselect(
#    'Select data', ['', ''], ['', ''])
# plot_height2 = st.sidebar.slider('Specify plot height', 100, 600, 500)


st.sidebar.markdown('''
---
Created with ❤️ by UCI MENG students.
''')

# Read csv
data1 = pd.read_csv(
    '/Users/ltkao/Downloads/Dataset/All data.csv', parse_dates=['timestamp'])
# data2 = pd.read_csv(
#    '', parse_dates=['timestamp'])
temp_data1 = data1[data1['sensorid'] == 1]
temp_data2 = data1[data1['sensorid'] == 2]
Avg_Upper_temp = int(data1['Sensor1_temp'].sum())//980
Avg_Lower_temp = data1['Sensor2_temp'].sum()//510

# Row A (Metrics)
st.markdown('### Metrics')
col1, col2, col3 = st.columns(3)
col1.metric("Avg. Upper Temp.", Avg_Upper_temp,
            Avg_Upper_temp - Avg_Lower_temp)
col2.metric("Avg. UV Intensity", "", "")
col3.metric("Avg. Lower Temp.", Avg_Lower_temp,
            Avg_Lower_temp - Avg_Upper_temp)

# Row B (Temperature Line chart)
st.markdown('### Temperature & Time')
st.line_chart(temp_data1, x='timestamp', y=plot_data1, height=plot_height1)

# Row C (UV Line chart)
st.markdown('### UV intensity & Time')
# st.line_chart(temp_data2, x='timestamp', y=plot_data2, height=plot_height2)
