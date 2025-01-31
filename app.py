import pandas as pd
import streamlit as st

# Load the Excel file
@st.cache
def load_data():
    # Adjust the file path as needed
    file_path = 'Stock_Financial_Performance_Analysis_with_PE_from_excel.xlsx'
    df = pd.read_excel(file_path, engine='openpyxl')
    return df

# Load data
df = load_data()

# Streamlit app
st.title('Stock Financial Performance Analysis')

# Sidebar: Select a column to rank by
st.sidebar.header('Ranking Options')
columns = df.columns.tolist()
columns.remove('Stock')  # Remove 'Stock' from the column list, as we don't want to rank by it
selected_column = st.sidebar.selectbox('Select Column to Rank By', columns)

# Sort the data by the selected column and display it
sorted_df = df.sort_values(by=selected_column, ascending=False)
st.write(f"Ranking by {selected_column}")
st.dataframe(sorted_df[['Stock', 'Sector', 'Industry', selected_column, 'Performance Rank']])

# Optional: You can add more interactivity or options like filtering by sector or industry
sector_filter = st.sidebar.selectbox('Filter by Sector', df['Sector'].unique())
filtered_df = sorted_df[sorted_df['Sector'] == sector_filter]
st.write(f"Ranking by {selected_column} (Filtered by {sector_filter} Sector)")
st.dataframe(filtered_df[['Stock', 'Sector', 'Industry', selected_column, 'Performance Rank']])

