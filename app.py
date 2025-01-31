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

# Sidebar: Select an industry
industry_filter = st.sidebar.selectbox('Select Industry to Filter By', df['Industry'].unique())

# Filter the data based on selected industry
industry_df = df[df['Industry'] == industry_filter]

# Sort the filtered data by the selected column and display top-ranked stocks
sorted_industry_df = industry_df.sort_values(by=selected_column, ascending=False)

# Display top stocks in the selected industry
st.write(f"Top Ranked Stocks in the {industry_filter} Industry (Sorted by {selected_column})")
st.dataframe(sorted_industry_df[['Stock', 'Sector', 'Industry', selected_column, 'Performance Rank']])

# Optionally, show more details like top 10 or allow ranking by more columns
top_n = st.slider('Select Top N Stocks', 1, 20, 10)
st.write(f"Top {top_n} Stocks in {industry_filter} Industry")
st.dataframe(sorted_industry_df[['Stock', 'Sector', 'Industry', selected_column, 'Performance Rank']].head(top_n))

