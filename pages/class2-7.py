import streamlit as st

st.title("Arrangement Practice")

col1, col2 = st.columns(2)
if col1.button("Balloon Button"):
    col1.balloons()
if col2.button("Snow Button"):
    col2.snow()

col3, col4, col5 = st.columns([1, 2, 3])
with col3:
    st.write("It is at col3")
    st.button("Button at col3")
with col4:
    st.write("It is at col4")
    st.button("Button at col4")
with col5:
    st.write("It is at col5")
    st.button("Button at col5")

    numCol = st.number_input(
        "Enter number of columns:", min_value=1, max_value=5, value=3, step=1
    )
    numButton = st.number_input(
        "Enter number of buttons per column:", min_value=1, step=1
    )
    cols = st.columns(numCol)
    for i in range(numButton):
        cols[i % numCol].button(f"Button {i+1}")

st.title("Text Input")
text = st.text_input("Enter some text:")
st.write("You entered: " + text)
