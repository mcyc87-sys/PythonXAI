import streamlit as st
import os
import time

ss = st.session_state

image_folder = "image"
image_files = os.listdir(image_folder)
image_files.sort()

if "products" not in ss:
    ss.products = {}
    for image_file in image_files:
        product_name = image_file[:-4]
        ss.products[product_name] = {
            "image_path": image_folder + "/" + image_file,
            "price": 10,
            "stock": 10,
        }

st.title("Shop")

colNum = st.number_input(
    "請輸入要購買的產品數量: ", min_value=1, max_value=5, value=3, step=1
)
cols = st.columns(colNum)
counter = 0

for name, details in ss.products.items():
    with cols[counter % colNum]:
        st.image(details["image_path"], use_container_width=True)
        st.write(f"## {name}")
        st.write(f"### 價格: ${details['price']}")
        st.write(f"### 庫存: {details['stock']}")
        if st.button(f"購買 {name}"):
            if details["stock"] > 0:
                details["stock"] -= 1
                st.success(f"成功購買 {name}")
            else:
                st.error(f"{name}庫存不足")
            time.sleep(1)
            st.rerun()
    counter += 1

st.title("Generate Product")


col1, col2 = st.columns(2)
selected_product = col1.selectbox("請選擇要購買的產品", ss.products.keys())
add_stock = col2.number_input("Generate Product", min_value=1, value=1)
if st.button("Generate Product"):
    ss.products[selected_product]["stock"] += add_stock
    st.success(f"{selected_product} Restocked {add_stock} 件")
    time.sleep(1)
    st.rerun()

st.title("Right now, we have these products in our shop:")
for name, details in ss.products.items():
    st.write(f"## {name}: ${details['stock']}件")
