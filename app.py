import streamlit as st
import pandas as pd

# Load the data from Excel file
def load_data():
    try:
        data = pd.read_excel('Stock_Financial_Performance_Analysis_with_PE_from_excel.xlsx')
        return data
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return pd.DataFrame()  # return an empty DataFrame in case of error

# Load the data
df = load_data()

# Check if data is loaded
if df.empty:
    st.write("No data available. Please check the file path and try again.")
else:
    # Streamlit app
    st.title('Stock Financial Performance Analysis')

    # Display the first few rows of the dataframe
    st.write("### Data Preview")
    st.dataframe(df.head())

    # Display column names and data types for debugging
    st.write("Columns in the dataset:", df.columns)
    st.write("Data Types:", df.dtypes)

    # Dropdown for selecting the industry
    industry_list = df['Industry'].unique()
    selected_industry = st.selectbox("Select an Industry", industry_list)

    # Filter data by selected industry
    df_industry = df[df['Industry'] == selected_industry]

    # Dropdown for selecting column for ranking
    column_to_rank = st.selectbox("Select the column to rank", df.columns)

    # Ensure the selected column is numeric or can be compared for ranking
    # Convert column to numeric if it's not already numeric (ignoring errors)
    df_industry[column_to_rank] = pd.to_numeric(df_industry[column_to_rank], errors='coerce')

    # Sorting the data by selected column
    df_sorted = df_industry.sort_values(by=column_to_rank, ascending=False)

    # Display the top-ranked stock based on the selected industry and column
    st.write(f"### Top Stock in {selected_industry} based on {column_to_rank}")
    st.dataframe(df_sorted[['Stock', 'Industry', column_to_rank]].head(1))

    # Optionally, display the full data with ranks
    show_full_data = st.checkbox('Show full data with ranks')
    if show_full_data:
        # Add a rank column based on the selected column
        df_sorted['Rank'] = df_sorted[column_to_rank].rank(ascending=False, method='min')
        st.write("### Full Data with Rank")
        st.dataframe(df_sorted)
