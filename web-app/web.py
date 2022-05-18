import streamlit as st
import pandas as pd
import numpy as np
import altair as alt


st.write(""" # UBC Bus Loop Queue Counter! 
Check the number of people standing in queue in different location
and the estimated waiting time
""")

# x = st.slider('Number of people infront of UBC bus loop')

# st.write('Number of people in queue is ', x-3)

df= pd.DataFrame(
    np.random.randint(20, size=(24,2)),
    columns = ['In Line', 'Not in Line']
)


print(df)

# st.area_chart(df)

st.bar_chart(df)

st.line_chart(df)

