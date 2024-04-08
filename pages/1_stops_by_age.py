import streamlit as st
import pandas as pd
import altair as alt

@st.cache_data
def load_data(csv):
    df =pd.read_csv(csv)
    return df

stops = load_data("data/Officer_Traffic_Stops.csv")

age_bar = alt.Chart(stops).mark_bar().encode(
    alt.X('Driver_Age:Q', bin=alt.Bin(maxbins=10), title='Driver Age'),
    y='count():Q',
    tooltip=['Driver_Age:Q', 'count():Q']
).properties(
    title='Histogram of Driver Age'
)

st.altair_chart(age_bar)
