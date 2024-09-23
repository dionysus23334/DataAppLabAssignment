import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()


st.title('California Housing Data(1990) by Yuxi Guo')
df = pd.read_csv('./housing.csv')

# note that you have to use 0.0 and 40.0 given that the data type of population is float
Value_filter = st.slider('Minimal Median House Value:', 0, 500001, 1000)  # min, max, default

# create a multi select
filter_location = st.sidebar.multiselect(
     'Choose the location type',
     df.ocean_proximity.unique(),  # options
     df.ocean_proximity.unique())  # defaults

filter_income = st.sidebar.radio('Choose income level:', ["Low", "Medium", "High"])
st.markdown('## **See more filters in the sidebar:**')

df = df[df.median_house_value >= Value_filter]

df = df[df.ocean_proximity.isin(filter_location)]

if filter_income=='Low':
    df = df[df.median_income <=2.5]
elif filter_income=='Medium':
    df = df[(2.5 < df.median_income) & (df.median_income < 4.5)]
elif filter_income=='High':
    df = df[df.median_income > 4.5]

# show on map
st.map(df)

st.title("Histogram of Median House Values")

import matplotlib.pyplot as plt

# Generate and display the histogram of median house values
plt.figure(figsize=(10, 6))
plt.hist(df['median_house_value'], bins=30, edgecolor='steelblue')
plt.title('Histogram of Median House Values', fontsize=16)
plt.xlabel('Median House Value', fontsize=14)
plt.ylabel('Frequency', fontsize=14)

st.pyplot(plt)  # Display the plot in Streamlit

