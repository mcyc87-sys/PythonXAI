import streamlit as st
import random

st.title("🎲 Dice Throw Game")

# user input
times = st.number_input(
    "How many times do you want to throw the dice?",
    min_value=1,
    max_value=100,
    value=5,
    step=1,
)

# button
if st.button("Throw Dice"):
    results = []

    for i in range(times):
        dice = random.randint(1, 6)
        results.append(dice)

    # show results
    st.subheader("🎯 Dice Results")
    st.write(results)

    # summary
    st.subheader("📊 Summary")
    for i in range(1, 7):
        st.write(f"Number {i}: {results.count(i)} times")

    st.success(f"Finished throwing the dice {times} times!")
