import streamlit as st
import pandas as pd

st.title("🧹 Data Cleaning Toolkit - Titanic Dataset")

raw = pd.read_csv("Titanic-Dataset.csv")
clean = pd.read_csv("Titanic_Cleaned.csv")

st.header("Before Cleaning")
st.write(f"Shape: {raw.shape}")
st.write(f"Missing Values:")
st.dataframe(raw.isnull().sum().reset_index().rename(columns={0:"Null Count", "index":"Column"}))
st.dataframe(raw.head())

st.header("After Cleaning")
st.write(f"Shape: {clean.shape}")
st.write(f"Missing Values:")
st.dataframe(clean.isnull().sum().reset_index().rename(columns={0:"Null Count", "index":"Column"}))
st.dataframe(clean.head())

st.success("✅ 177 Age nulls filled | 687 Cabin rows dropped | Columns standardized")