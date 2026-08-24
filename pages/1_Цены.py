import streamlit as st

st.set_page_config(page_title="Цены | Ketrin Plase", layout="wide", initial_sidebar_state="expanded")

st.markdown("""
<style>
.stApp, .main, [data-testid="stAppViewContainer"] { 
    background-image: linear-gradient(rgba(20, 15, 13, 0.8), rgba(20, 15, 13, 0.8)), url("https://ibb.co") !important;
    background-size: cover !important;
    background-attachment: fixed !important;
    background-color: #140f0d !important;
} 
h1, h2, h3, h4, p, span, div { color: #f5ebe6 !important; font-family: 'Georgia', serif !important; }
.price-card {
    background-color: rgba(45, 35, 32, 0.85) !important;
    padding: 25px;
    border-radius: 15px;
    border-top: 4px solid #bc987e !important;
    margin-bottom: 20px;
}
.price-card h3 { color: #dfba9d !important; margin-top: 0; }
.price-card h4 { color: #dfba9d !important; margin-bottom: 0; }
</style>
""", unsafe_allow_html=True)

st.title("🌸 Наши услуги и цены")
st.write("Ознакомьтесь с премиальными ритуалами нашего салона:")
st.divider()

p_col1, p_col2, p_col3, p_col4 = st.columns(4)

with p_col1:
    st.image("https://ibb.co", use_container_width=True)
    st.markdown("""<div class="price-card" style="margin-top: -15px;"><h3>🛁 Тайский массаж</h3><p>Массаж всего тела. Помогает при проблемах со спиной и зажимах. Подается элитный чай или кофе.</p><hr><h4 style="color:#dfba9d!important;">Цена: 45 BYN / час</h4></div>""", unsafe_allow_html=True)

with p_col2:
    st.image("https://ibb.co", use_container_width=True)
    st.markdown("""<div class="price-card" style="margin-top: -15px;"><h3>🌲 Массаж ног</h3><p>Распаривание ног на алтайских травах, очищение пор, ингаляция и таежный чай с медом.</p><hr><h4 style="color:#dfba9d!important;">Цена: 35 BYN / сеанс</h4></div>""", unsafe_allow_html=True)

with p_col3:
    st.image("https://ibb.co", use_container_width=True)
    st.markdown("""<div class="price-card" style="margin-top: -15px;"><h3>💆‍♂️ Спа-Массаж</h3><p>Массаж горячими базальтовыми камнями или кокосовым маслом. Снятие мышечных зажимов.</p><hr><h4 style="color:#dfba9d!important;">Цена: 60 BYN / 60 мин</h4></div>""", unsafe_allow_html=True)

with p_col4:
    st.image("https://ibb.co", use_container_width=True)
    st.markdown("""<div class="price-card" style="margin-top: -15px;"><h3>🛁 Молочная ванна</h3><p>Ванна наполняется теплым молочным раствором, экстрактами трав и лепестками роз.</p><hr><h4 style="color:#dfba9d!important;">Цена: 50 BYN / час</h4></div>""", unsafe_allow_html=True)
