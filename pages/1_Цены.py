import streamlit as st

st.set_page_config(
    page_title="Цены | Ketrin Plase",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Простая стандартная кнопка возврата без всяких стилей
if st.button("⬅️ Вернуться на главную", use_container_width=True):
    st.switch_page("app.py")

st.title("💆‍♀️ Наши услуги и цены")
st.write("Ознакомьтесь с премиальными ритуалами нашего салона:")
st.divider()

st.title("🌸 Наши услуги и цены")
st.write("Ознакомьтесь с премиальными ритуалами нашего салона:")
st.divider()

# Создаем 4 колонки для карточек услуг
p_col1, p_col2, p_col3, p_col4 = st.columns(4)

with p_col1:
    # Заменяем сломанную ссылку на локальное фото из папки images
    st.image("images/image1.jpg.png", use_container_width=True)
    st.markdown("""<div class="price-card" style="margin-top: -15px;"><h3>💆‍♂️ Тайский массаж</h3><p>Массаж всего тела. Помогает при проблемах со спиной и зажимах. Подается элитный чай или кофе.</p></div>""", unsafe_allow_html=True)
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
    # Если файла image4 нет, используем картинку bg или снова image1
    st.image("images/image1.jpg.png", use_container_width=True)
    st.markdown("""<div class="price-card" style="margin-top: -15px;"><h3>🛁 Молочная ванна</h3><p>Ванна наполняется теплым молочным раствором, экстрактами трав и лепестками роз.</p></div>""", unsafe_allow_html=True)
    st.subheader("Цена: 50 BYN / час")
