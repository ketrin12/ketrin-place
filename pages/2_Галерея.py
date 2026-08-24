import streamlit as st

st.set_page_config(page_title="Галерея | Ketrin Plase", layout="wide", initial_sidebar_state="expanded")

st.markdown("""
<style>
.stApp, .main, [data-testid="stAppViewContainer"] { 
    background-image: linear-gradient(rgba(20, 15, 13, 0.8), rgba(20, 15, 13, 0.8)), url("https://ibb.co") !important;
    background-size: cover !important;
    background-attachment: fixed !important;
    background-color: #140f0d !important;
} 
h1, h2, p { color: #f5ebe6 !important; font-family: 'Georgia', serif !important; }
</style>
""", unsafe_allow_html=True)

st.title("📸 Галерея нашего салона")
st.write("Посмотрите на уютную и расслабляющую атмосферу Ketrin Plase:")
st.divider()

g_col1, g_col2 = st.columns(2)
with g_col1:
    st.image("https://ibb.co", caption="Массажный кабинет премиум-класса", use_container_width=True)
with g_col2:
    st.image("https://unsplash.com", caption="Зона ожидания и релакса", use_container_width=True)
