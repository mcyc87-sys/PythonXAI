import streamlit as st

st.set_page_config(page_title="My Streamlit App", page_icon="😇", layout="wide")
all_pages = {
    "": [
        st.Page("pages/hand_book.py", title="課程筆記", icon="📖"),
    ],
    "📚 程式練習": [
        st.Page("pages/class1-2.py", title="Markdown語法", icon="📝"),
        st.Page("pages/class2-1.py", title="成績等第判斷", icon="📊"),
        st.Page("pages/class2-3.py", title="金字塔系列", icon="🔺"),
        st.Page("pages/class2-7.py", title="排版練習", icon="🔺"),
    ],
}


nav = st.navigation(all_pages, position="sidebar")
nav.run()
