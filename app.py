import streamlit as st
import pandas as pd

# Load the data from Excel file
@st.cache
def load_data():
    data = pd.read_excel('Stock_Financial_Performance_Analysis_with_PE_from_excel.xlsx')
    return data

# Load the data
df = load_data()

# Streamlit app
st.title('Stock Financial Performance Analysis')

# Display the first few rows of the dataframe
st.write("### Data Preview")
st.dataframe(df.head())

# Dropdown for selecting column for ranking
column_to_rank = st.selectbox("Select the column to rank", df.columns)

# Sorting the data by selected column
df_sorted = df.sort_values(by=column_to_rank, ascending=False)

# Display the top 10 rows of the sorted data
st.write(f"### Top 10 Stocks based on {column_to_rank}")
st.dataframe(df_sorted[['Stock', column_to_rank]].head(10))

# Optionally, display the full data with ranks
show_full_data = st.checkbox('Show full data with ranks')
if show_full_data:
    # Add a rank column based on the selected column
    df_sorted['Rank'] = df_sorted[column_to_rank].rank(ascending=False, method='min')
    st.write("### Full Data with Rank")
    st.dataframe(df_sorted)
