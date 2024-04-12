import streamlit as st
import pandas as pd
import numpy as np

def filter_data(df,carname,transmission,price_range,year_range):
    df = df.filter(items = ['Car_Name','Year','Selling_Price','Transmission'])
    df = df[df['Car_Name']==car_name]
    df = df[df['Transmission'].isin(transmission)]
    df = df[df['Selling_Price'].between(price_range[0],price_range[1])]
    df = df[df['Year'].between(year_range[0],year_range[1])] 
    return df


st.title("This is the Car Data Selection APP")
car_name = st.sidebar.text_input("Car Name")
transmission = st.sidebar.multiselect("Transmission", ['Manual', 'Automatic'], default=['Manual', 'Automatic'])
selling_price_range = st.sidebar.slider("Selling Price Range", 0, 20, (0, 20))
year_range = st.sidebar.slider("Year Range", 2000, 2024, (2000, 2024))

df = pd.read_csv('car_data.csv')

filter = filter_data(df,car_name,transmission,selling_price_range,year_range)

if st.sidebar.button("Submit"):
    st.write(filter)
else:
    st.write(df)