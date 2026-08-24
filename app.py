import streamlit as st

st.set_page_config(
    page_title="Ketrin Plase | Главная", 
    page_icon="🌸", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# ТЕМНЫЙ СТИЛЬ И НАСТРОЙКА БОКОВОГО МЕНЮ
st.markdown("""
<style>
/* Загружаем фоновый рисунок из интернета с красивым затемнением */
.stApp, .main, [data-testid="stAppViewContainer"] { 
    background-image: linear-gradient(rgba(20, 15, 13, 0.8), rgba(20, 15, 13, 0.8)), url("https://ibb.co") !important;
    background-size: cover !important;
    background-position: center !important;
    background-attachment: fixed !important;
    background-color: #140f0d !important;
} 

/* Внутренний контейнер для читаемости */
[data-testid="stHeader"] { background: rgba(0,0,0,0); }

/* Все буквы на сайте делаем элегантными белыми/кремовыми */
h1, h2, h3, h4, h5, h6, p, span, label, li, div, b { 
    color: #f5ebe6 !important; 
    font-family: 'Georgia', serif !important; 
}

/* Перекрашиваем боковое меню в строгий темный цвет шоколада */
[data-testid="stSidebar"], [data-testid="stSidebarNav"] {
    background-color: #2d2320 !important;
}
/* Намертво убираем кнопку с уродливой системной надписью */
[data-testid="stSidebarCollapseButton"] {
    display: none !important;
}

/* Прячем системный текст и заменяем его на красивую стрелочку */
[data-testid="stSidebarCollapseButton"] button {
    font-size: 0 !important;
}
[data-testid="stSidebarCollapseButton"] button::after {
    content: "←" !important;
    font-size: 24px !important;
    color: #dfba9d !important;
}

/* Делаем буквы и иконки внутри меню крупными и золотыми */
[data-testid="stSidebarNav"] span, [data-testid="stSidebarNav"] a {
    color: #dfba9d !important;
    font-size: 18px !important;
    font-family: 'Georgia', serif !important;
}
</style>
""", unsafe_allow_html=True)

# 2. Строгая шапка сайта
st.markdown(
    "<div style='background-color: rgba(25, 20, 18, 0.9); padding: 30px; border-radius: 12px; text-align: center; border: 1px solid #4a3b32;'>"
    "<h1 style='color: #dfba9d !important; margin: 0; font-size: 42px; letter-spacing: 2px;'>Ketrin Plase</h1>"
    "<p style='margin: 10px 0 0 0; color: #b3b3b3 !important; font-size: 16px; letter-spacing: 3px; text-transform: uppercase;'>Премиум СПА-салон в Гомеле</p>"
    "</div>", 
    unsafe_allow_html=True
)

st.write("") 

# 3. Баннер
col1, col2 = st.columns([1.2, 1])
with col1:
    st.markdown("<h4 style='color: #bc987e !important; text-transform: uppercase; letter-spacing: 2px;'>Эстетика релакса</h4>", unsafe_allow_html=True)
    st.title("Добро пожаловать в Ketrin Plase")
    st.write("Выберите интересующий вас раздел в боковом меню слева, чтобы посмотреть цены или открыть галерею нашего салона.")

with col2:
    st.image("https://ibb.co", caption="Интерьер нашего салона", use_container_width=True)

st.divider()

# 4. Форма онлайн-записи
st.markdown("<h2>📩 Онлайн-резервирование визита</h2>", unsafe_allow_html=True)
FORMSPREE_URL = "https://formspree.io" 

form_html = f"""
<form action="{FORMSPREE_URL}" method="POST" style="background-color: rgba(25, 20, 18, 0.9); padding: 30px; border-radius: 12px; border: 1px solid #4a3b32;">
    <div style="margin-bottom: 20px;"><label style="color: #dfba9d !important; font-weight: bold;">Ваше имя:</label><br><input type="text" name="name" required style="width: 100%; padding: 12px; background-color: #140f0d; border: 1px solid #bc987e; border-radius: 6px; color: white;"></div>
    <div style="margin-bottom: 20px;"><label style="color: #dfba9d !important; font-weight: bold;">Телефон или Email:</label><br><input type="email" name="_replyto" required style="width: 100%; padding: 12px; background-color: #140f0d; border: 1px solid #bc987e; border-radius: 6px; color: white;"></div>
    <div style="margin-bottom: 20px;"><label style="color: #dfba9d !important; font-weight: bold;">Пожелания к визиту:</label><br><textarea name="message" required style="width: 100%; height: 100px; background-color: #140f0d; border: 1px solid #bc987e; border-radius: 6px; color: white; resize: none;"></textarea></div>
    <button type="submit" style="background-color: #bc987e; color: #231f20; padding: 14px 28px; border: none; border-radius: 6px; cursor: pointer; font-size: 16px; font-weight: bold; width: 100%; text-transform: uppercase;">Забронировать визит</button>
</form>
"""
st.markdown(form_html, unsafe_allow_html=True)

st.divider()
st.caption("© 2026 Ketrin Plase. Режим работы: с 9:00 до 23:00 ежедневно. Все права защищены.")
