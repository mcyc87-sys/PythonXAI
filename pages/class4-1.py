import streamlit as st
import os

st.title("Picture element")

st.image(
    "image/anime-initial-d-final-stage-toyota-ae86-toyota-trueno-wallpaper-preview.jpg",
    width=1000,
    caption="Initial D",
)
st.image(
    "image/initial-d-background-nj29bq91uh5rfycz.jpg", width=1000, caption="Mazda Rx7"
)
st.image(
    "image/initial-d-fujiwara-takumi-cbs8jev7bqol21bp.jpg",
    width=1000,
    caption="Toyota AE86",
)
st.image(
    "image/initial-d-racing-sports-cars-2nulf7szl2hb4b9a.jpg",
    width=1000,
    caption="Nissan Skyline GT-R",
)

image_folder = "image"
image_files = os.listdir(image_folder)
image_files.sort()
st.write(image_files)

for image_file in image_files:
    image_path = image_folder + "/" + image_file
    st.image(image_path, width=300)

for image_file in image_files:
    image_path = image_folder + "/" + image_file
    st.image(image_path, use_container_width=True)

st.title("Select Box Component")

selected_image = st.selectbox("Please choose a image", image_files)
st.write("Your chosen image is:", selected_image[:-4])
image_path = image_folder + "/" + selected_image
st.image(image_path, width=1000)

import time

st.title("Website Radio Component")
cols = st.columns(4)

# success
if cols[0].button("Success Button"):
    st.success("This is st.success message")
    time.sleep(1)
    st.rerun()
# error
if cols[1].button("Error Button"):
    st.error("This is st.error message")
    time.sleep(1)
    st.rerun()
# warning
if cols[2].button("Warning Button"):
    st.warning("This is st.warning message")
    time.sleep(1)
    st.rerun()
# info
if cols[3].button("Info Button"):
    st.info("This is st.info message")
    time.sleep(1)
    st.rerun()
