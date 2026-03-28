import streamlit as st
import pandas as pd

st.title("Fashion AI - Customer Insights Dashboard")

uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
else:
    df = pd.read_csv("fashion_data.csv")

st.subheader("Data Preview")
st.write(df.head())

st.subheader("Basic Insights")
st.write(df.describe(include='all'))

st.subheader("Purchase Intent Distribution")
st.bar_chart(df['Purchase_Intent'].value_counts())
