import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.write(''' #Strive-Nutrition Analysis ''')

df = pd.read_csv("https://raw.githubusercontent.com/chriswmann/datasets/master/500_Person_Gender_Height_Weight_Index.csv")

st.line_chart(df)