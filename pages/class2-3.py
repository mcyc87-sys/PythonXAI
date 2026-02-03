import streamlit as st

st.title("Number Pyramid")
height = st.number_input(
    "Enter a whole number:", min_value=1, max_value=1000, value=5, step=1
)
st.write("Number Pyramid:")
for i in range(1, height + 1):
    st.write(str(i) * i)

st.title("Number Pyramid")
arrow_height = st.number_input(
    "Enter the height of the arrow:", min_value=1, value=5, step=1
)
st.write("Arrow Pyramid:")
a = ""
for i in range(1, arrow_height + 1):
    a = a + (" " * (arrow_height - i) + "*" * (i * 2 - 1) + "\n")

for i in range(arrow_height):
    a = a + (" " * (arrow_height - 1) + "*" + "\n")
st.write(f"```\n\n{a}```")
