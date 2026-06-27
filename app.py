import streamlit as st
import pandas as pd
from io import BytesIO

st.title("🧹 Data Cleaning Toolkit")
st.write("Upload any messy CSV and get it cleaned instantly!")

uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    
    st.header("Before Cleaning")
    st.write(f"Shape: {df.shape}")
    st.write("Missing Values:")
    st.dataframe(df.isnull().sum().reset_index().rename(columns={0:"Null Count", "index":"Column"}))
    st.dataframe(df.head())

    # Clean
    df.drop_duplicates(inplace=True)
    for col in df.columns:
        if df[col].dtype == "float64" or df[col].dtype == "int64":
            df[col] = df[col].fillna(df[col].median())
        else:
            df[col] = df[col].fillna(df[col].mode()[0] if not df[col].mode().empty else "Unknown")
    df.columns = df.columns.str.lower().str.strip()

    st.header("After Cleaning")
    st.write(f"Shape: {df.shape}")
    st.write("Missing Values:")
    st.dataframe(df.isnull().sum().reset_index().rename(columns={0:"Null Count", "index":"Column"}))
    st.dataframe(df.head())

    # Download button
    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button("Download Cleaned CSV", csv, "cleaned.csv", "text/csv")
    st.success("✅ Duplicates removed | Nulls filled | Columns standardized")

else:
    st.info("Please upload a CSV file to get started!")