import streamlit as st
a=st.number_input("Enter num 1:")
b=st.number_input("Enter num 2:")
if st.button("Add"):
	st.success(a+b)
elif st.button("Sub"):
	st.success(a-b)
elif st.button("Multiply"):
	st.success(a*b)
elif st.button("Division"):
	st.success(a/b)

