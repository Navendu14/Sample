import streamlit as st
import pandas as pd
data1 = {'user': ['Alice', 'Bob', 'Charlie'], 'messages': [25, 50, 10]}
df1 = pd.DataFrame(data1)
st.dataframe(df1)