import streamlit as st
a=st.number_input("Enter a num:")
b=st.number_input("Enter another num:")
if st.button("Add"):
	st.success(a+b)
elif st.button("Sub"):
	st.success(a-b)
elif st.button("Multiply"):
	st.success(a*b)


