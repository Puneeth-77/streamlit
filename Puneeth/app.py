import streamlit as st
a=st.number_input("Enter a number:")
b=st.number_input("Enter another number:")
if st.button("Add"):
	st.success(a+b)
elif st.button("Sub"):
	st.success(a-b)
elif st.button("Multiply"):
	st.success(a*b)


