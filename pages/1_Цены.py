import streamlit as st

st.set_page_config(
    page_title="Цены | Ketrin Plase",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Жестко задаем темную тему и стили для всей страницы
st.markdown("""
<style>
    /* Скрываем меню и шапку */
    [data-testid="stSidebar"], 
    [data-testid="collapsedControl"], 
    [data-testid="stHeader"] {
        display: none !important;
    }
    
    /* Делаем фон всей страницы темным */
    .stApp, .main, [data-testid="stAppViewContainer"] {
        background-color: #140f0d !important;
    }
    
    /* Делаем все тексты на странице светлыми */
    h1, h2, h3, h4, p, span, div, label { 
        color: #f5ebe6 !important; 
        font-family: 'Georgia', serif !important; 
    }
    
    /* Стиль для кнопки возврата (чтобы она не была белой) */
    .stButton > button {
        background-color: #2d2320 !important;
        color: #bc987e !important;
        border: 1px solid #bc987e !important;
    }
    
    /* Красивые темные карточки для цен */
    .price-card {
        background-color: #2d2320 !important;
        padding: 25px;
        border-radius: 15px;
        border-top: 4px solid #bc987e !important;
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

# Кнопка возврата
if st.button("⬅️ Вернуться на главную", use_container_width=True):
    st.switch_page("app.py")

# Здесь мы убрали st.title, чтобы заголовок не дублировался!

st.title("💆‍♀️ Наши услуги и цены")
st.write("Ознакомьтесь с премиальными ритуалами нашего салона:")
st.divider()

st.title("🌸 Наши услуги и цены")
st.write("Ознакомьтесь с премиальными ритуалами нашего салона:")
st.divider()

# Создаем 4充колонки для карточек услуг
p_col1, p_col2, p_col3, p_col4 = st.columns(4)

with p_col1:
    # Используем точное имя файла с гитхаба
    st.image("images/image1.jpg.png", use_container_width=True)
    st.markdown("""<div class="price-card" style="margin-top: -15px;"><h3>💆‍♂️ Тайский массаж</h3><p>Массаж всего тела. Помогает при проблемы со спиной и зажимах. Подается элитный чай или кофе.</p></div>""", unsafe_allow_html=True)
    st.subheader("Цена: 45 BYN / час")

with p_col2:
    st.image("images/image2.jpg.png", use_container_width=True)
    st.markdown("""<div class="price-card" style="margin-top: -15px;"><h3>🌲 Массаж ног</h3><p>Распаривание ног на алтайских травах, очищение пор, ингаляция и таежный чай с медом.</p></div>""", unsafe_allow_html=True)
    st.subheader("Цена: 35 BYN / сеанс")

with p_col3:
    st.image("images/image3.jpg.png", use_container_width=True)
    st.markdown("""<div class="price-card" style="margin-top: -15px;"><h3>🪨 Спа-Массаж</h3><p>Массаж горячими базальтовыми камнями или кокосовым маслом. Снятие мышечных зажимов.</p></div>""", unsafe_allow_html=True)
    st.subheader("Цена: 60 BYN / 60 мин")

with p_col4:
    # Для четвертой карточки временно берем bg.jpg.webp, которая точно была на гитхабе
    st.image("images/bg.jpg.webp", use_container_width=True)
    st.markdown("""<div class="price-card" style="margin-top: -15px;"><h3>🛁 Молочная ванна</h3><p>Ванна наполняется теплым молочным раствором, экстрактами трав и лепестками роз.</p></div>""", unsafe_allow_html=True)
    st.subheader("Цена: 50 BYN / час")

