import streamlit as st
import pandas as pd
from sklearn import datasets

st.write('Return largest of 3 input numbers')

def user_input_features():
  num1 = st.number_input("num1")
  num2 = st.number_input("num2")
  num3 = st.number_input("num3")

  data = {
    'num1': num1,
    'num2': num2,
    'num3': num3
  }

  inputs = pd.DataFrame(data, index = [0])

  return(inputs)

df = user_input_features()

st.dataframe(df)

st.write('The max of the three numbers is ' + str(df.iloc[0].max()))