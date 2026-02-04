import streamlit as st

st.title("Shopping List")

ss = st.session_state

if "orders" not in ss:
    ss.orders = []

col1, col2 = st.columns([9, 1])
foodInput = col1.text_input("Enter food item:")
if col2.button("Add"):
    ss.orders.append(foodInput)
    st.rerun()

st.write("### Your Shopping List:")
for i in range(len(ss.orders)):
    col3, col4 = st.columns([9, 1])
    col3.write(ss.orders[i])
    if col4.button("Delete", key=f"del_{i}"):
        ss.orders.pop(i)
        st.rerun()
