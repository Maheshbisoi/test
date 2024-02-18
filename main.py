'''import streamlit as st'''

'''st.write("# hello world")'''


import streamlit as st

num1 = st.number_input("Enter the first value")
num2 = st.number_input("Enter the second value")

if st.button("Add"):
    total = num1 + num2
    st.write(f"The total is {total}")
    st.balloons()
    st.balloons()
