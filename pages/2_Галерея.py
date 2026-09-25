import streamlit as st

st.set_page_config(
    page_title="Галерея | Ketrin Plase",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Жестко скрываем меню и красим фон в темный
st.markdown("""
<style>
    [data-testid="stSidebar"], 
    [data-testid="collapsedControl"], 
    [data-testid="stHeader"] {
        display: none !important;
    }
    .stApp, .main, [data-testid="stAppViewContainer"] {
        background-color: #140f0d !important;
    }
    h1, h2, h3, h4, p, span, div { 
        color: #f5ebe6 !important; 
        font-family: 'Georgia', serif !important; 
    }
    .stButton > button {
        background-color: #2d2320 !important;
        color: #bc987e !important;
        border: 1px solid #bc987e !important;
    }
</style>
""", unsafe_allow_html=True)

# Кнопка возврата на главную
if st.button("⬅️ Вернуться на главную", use_container_width=True):
    st.switch_page("app.py")

# Наш красивый заголовок
st.markdown("<h2 style='text-align: center; color: #dfba9d;'>🌸 Галерея нашего салона</h2>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# Выводим фотку интерьера bg.jpg
st.image("images/bg.jpg.webp", caption="Уютная атмосфера релакса в Ketrin Plase", use_container_width=True)

st.image("images/zona.jpg", caption="Комфортная зона ожидания в Ketrin Plase", use_container_width=True)
