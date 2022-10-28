import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import altair as alt

st.markdown("# Streamlit Plot Example")
st.markdown("""
            - This
            - is an
            - unordered list
            """)

# Data Frame
st.dataframe(pd.DataFrame([[1, 2], [3, 4]], columns=["a", "b"]))

# Dic
st.write({"a": [1, 2, 3], 
          "b": [2, 3, 4]})

# pandas dataframe
st.write(pd.DataFrame({
    "a": [1, 2, 3, 4, 5],
    "b": [4, 5, 6, 7, 8]
}))

# Graph Title
st.write("Hello, *World!* :sunglasses:")

# Plot
df = pd.DataFrame(
    np.random.randn(200, 3),
    columns=["a", "b", "c"]
)

c = alt.Chart(df).mark_circle().encode(
    x="a", y="b", size="c", color="c", tooltip=["a", "b", "c"])
st.write(c)

# User interaction
number = st.number_input("Insert a number", 123)
st.write("Inserted nunmber is: ", number)