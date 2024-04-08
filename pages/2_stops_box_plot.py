import streamlit as st
import pandas as pd
import altair as alt
import matplotlib.pyplot as plt
import seaborn as sns

@st.cache_data
def load_data(csv):
    df =pd.read_csv(csv)
    return df

stops = load_data("data/Officer_Traffic_Stops.csv")

st.set_option('deprecation.showPyplotGlobalUse', False)


# box plot

plt.figure(figsize=(8, 8))

sns.boxplot(x='Was_a_Search_Conducted', y='Driver_Age', data=stops)

# labels and title
plt.xlabel('Was a Search Conducted')
plt.ylabel('Driver Age')
plt.title('Box Plot of Driver Age by Search Conducted')


# plot
st.pyplot()