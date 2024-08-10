import streamlit as st
import pandas as pd
import plotly.express as px

def app():
    # Load dataset
    data_url = 'mock_smart_bin_data.csv'  # Update this to the path where your CSV file is located
    df = pd.read_csv(data_url)

    # Convert 'Timestamp' to datetime
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])

    # Sidebar filters
    st.sidebar.header('Filters')
    start_date = st.sidebar.date_input('Start date', df['Timestamp'].min().date())
    end_date = st.sidebar.date_input('End date', df['Timestamp'].max().date())

    # Filter data based on date range
    filtered_df = df[(df['Timestamp'] >= pd.to_datetime(start_date)) & (df['Timestamp'] <= pd.to_datetime(end_date))]

    # Main dashboard
    st.title('Smart Bin Dashboard')

    # Fill Level Over Time
    st.subheader('Fill Level Over Time')
    fig_fill_level = px.line(filtered_df, x='Timestamp', y='Fill Level (%)', title='Fill Level Over Time')
    st.plotly_chart(fig_fill_level)

    # Object Classification Distribution
    st.subheader('Object Classification Distribution')
    classification_counts = filtered_df['Detected Object'].value_counts().reset_index()
    classification_counts.columns = ['Detected Object', 'Count']
    fig_classification = px.bar(classification_counts, x='Detected Object', y='Count', title='Object Classification Distribution')
    st.plotly_chart(fig_classification)

    # Flap Position Over Time
    st.subheader('Flap Position Over Time')
    fig_flap_position = px.scatter(filtered_df, x='Timestamp', y='Flap Position', color='Flap Position', title='Flap Position Over Time')
    st.plotly_chart(fig_flap_position)

    # Download Filtered Data
    st.subheader('Download Filtered Data')
    csv = filtered_df.to_csv(index=False)
    st.download_button(
        label="Download CSV",
        data=csv,
        file_name='filtered_smart_bin_data.csv',
        mime='text/csv',
    )
