import streamlit as st
import pandas as pd

st.title("Simpe Data Dashboard")

uploaded_file =st.file_uploader("choose a csv file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("data preview")
    st.write(df.head())

    st.subheader("Data summary")
    st.write(df.describe())

    st.dubheader('filter data')
    columns = df.columns.tolist()
    selected_column = st.selectbox("select column to filter by", columns)
    unique_values = df[selected_column].unique()
    selected_value =st.selectbox("select value", unique_values)
    filtered_df =df[df[selected_column]== selected_value]
    st.write("filterd_df")
    st.subheader("plot data")
    x_column = st.selectbox("select x-axis column", columns)
    y_column = st.selectbox("select y-axis column", columns)

    if st.button("generate plot"):
        st.line_chart(filtered_df.set_index(x_column)[y_column])
else:
    st.write("waiting on file upload...")        
