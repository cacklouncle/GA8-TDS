import streamlit as st
st.write("""
### Largest among 3 finder
Made by Piyush Agrawal (21f1004416) 
""")

st.header('Input parameters')
num1 = st.number_input("Number 1",step = 1)
num2 = st.number_input("Number 2",step = 1)
num3 = st.number_input("Number 3",step = 1)
st.write(num1, num2, num3)
st.write("### Largest among the three is ", max(num1,num2,num3))
