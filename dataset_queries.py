import streamlit as st
import pandas as pd

st.title("🗂️ Dataset Explorer")

file = st.selectbox("Choose a file", ["calories.csv", "exercise.csv"])

if file:
    df = pd.read_csv(file)
    st.write("Dataset Preview:")
    st.dataframe(df)

    st.write("Search/Filter:")
    column = st.selectbox("Filter Column", df.columns)
    value = st.text_input("Enter filter value")

    if value:
        st.dataframe(df[df[column].astype(str).str.contains(value)])
