import streamlit as st

st.set_page_config(page_title="我的第一個網站", page_icon="🏠", layout="wide")

all_pages = {
    "": [
        st.Page("pages/hand_book.py", title="課程筆記", icon="📖"),
    ],
    "📚 程式練習": [
        st.Page("pages/class1-2.py", title="Markdown語法", icon="📝"),
        st.Page("pages/class2-1.py", title="成績等第判斷", icon="📊"),
        st.Page("pages/class2-3.py", title="金字塔系列", icon="🔺"),
        st.Page("pages/class2-7.py", title="排版練習", icon="🎨"),
        st.Page("pages/class3-5.py", title="猜數字遊戲", icon="🎲"),
        st.Page("pages/class4-1.py", title="Picture elements", icon="🖼️"),
        st.Page("pages/class4-2.py", title="Shoppee", icon="🛒"),
        st.Page("pages/class5-1.py", title="Dice", icon="🎲"),
        st.Page("pages/class5-2.py", title="AI Chat", icon="🤖"),
        st.Page("pages/class5-3.py", title="AI Enter", icon="👌"),
        st.Page("pages/class5-5.py", title="Real Ai Chat", icon="😍"),
        st.Page("pages/class5-6.py", title="AAAII Chat", icon="👍🏻"),
        st.Page("pages/class5-7.py", title="Upload pic", icon="😎"),
        st.Page("pages/class5-8.py", title="Ai pic", icon="🥹"),
        st.Page("pages/class5-9.py", title="Animation", icon="😊"),
        st.Page("pages/class5-10.py", title="Ai picture generate", icon="😉"),
    ],
}


nav = st.navigation(all_pages, position="sidebar")
nav.run()
