import streamlit as st

# 1. Настройка страницы
st.set_page_config(
    page_title="Ketrin Plase | SPA & Бани", 
    page_icon="🌸", 
    layout="wide"
)

# СТРОГИЙ СТИЛЬ: Настраиваем благородный темный фон для премиум-салона
st.markdown("""
<style>
/* Загружаем фоновый рисунок из интернета с красивым затемнением */
.stApp, .main, [data-testid="stAppViewContainer"] { 
    background-image: linear-gradient(rgba(20, 15, 13, 0.8), rgba(20, 15, 13, 0.8)), url("https://ibb.co") !important;
    background-size: cover !important;
    background-position: center !important;
    background-attachment: fixed !important;
    background-color: #140f0d !important; /* Глубокий благородный темный цвет */
} 

/* Внутренний контейнер для читаемости */
[data-testid="stHeader"] { background: rgba(0,0,0,0); }

/* Все буквы на сайте делаем элегантными белыми/кремовыми для темного спа-фона */
h1, h2, h3, h4, h5, h6, p, span, label, li, div, b { 
    color: #f5ebe6 !important; 
    font-family: 'Georgia', serif !important; 
}

/* Премиальные карточки для услуг (темный полупрозрачный шоколадный оттенок) */
.price-card {
    background-color: rgba(45, 35, 32, 0.85) !important;
    padding: 25px;
    border-radius: 15px;
    box-shadow: 0 8px 16px rgba(0,0,0,0.5);
    border-top: 4px solid #bc987e !important;
    margin-bottom: 20px;
    backdrop-filter: blur(5px);
}

/* Текст внутри карточек услуг */
.price-card h3 { color: #dfba9d !important; margin-top: 0; }
.price-card p { color: #e1d5ce !important; font-size: 15px; }
.price-card h4 { color: #dfba9d !important; margin-bottom: 0; }
</style>
""", unsafe_allow_html=True)

# 2. Строгая шапка сайта (УБРАЛИ СЕРТИФИКАТЫ!)
st.markdown(
    "<div style='background-color: rgba(25, 20, 18, 0.9); padding: 30px; border-radius: 12px; text-align: center; border: 1px solid #4a3b32;'> "
    "<h1 style='color: #dfba9d !important; margin: 0; font-size: 42px; letter-spacing: 2px;'>Ketrin Plase</h1>"
    "<p style='margin: 10px 0 0 0; color: #b3b3b3 !important; font-size: 16px; letter-spacing: 3px; text-transform: uppercase;'>Услуги • Галерея • Цены • Контакты</p>"
    "</div>", 
    unsafe_allow_html=True
)

st.write("") 

# 3. Главный баннер салона
col1, col2 = st.columns([1.2, 1])

with col1:
    st.markdown("<h4 style='color: #bc987e !important; text-transform: uppercase; letter-spacing: 2px;'>Эстетика релакса в Гомеле</h4>", unsafe_allow_html=True)
    st.title("Новая процедура: СПА для волос и тела")
    st.subheader("📍 Гомель, ул. Карповича")
    st.write(
        "Забудьте о стрессе и городской суете. Наш премиальный спа-салон создан для тех, "
        "кто ценит глубокое расслабление, профессиональный уход и безупречный сервис."
    )
    st.markdown("<h3 style='color: #dfba9d !important;'>Скидка -20% на первый визит</h3>", unsafe_allow_html=True)

with col2:
    # Главный баннер с фото интерьера салона
    st.image("https://ibb.co", caption="Атмосфера нашего салона", use_container_width=True)

st.divider()

# 4. БЛОК: УСЛУГИ И ЦЕНЫ
st.markdown("<h2 style='text-align: center; letter-spacing: 1px;'>🌸 Наши услуги и привилегии</h2>", unsafe_allow_html=True)
st.write("")

p_col1, p_col2, p_col3, p_col4 = st.columns(4)

with p_col1:
    # Публичная ссылка на твое фото №1
    st.image(image1.jpg, use_container_width=True)
    st.markdown("""
<div class="price-card" style="margin-top: -15px;">
    <h3>🛁 Тайский массаж</h3>
    <p>Массаж всего тела. Эффективно помогает при проблемах со спиной и зажимах. Сеанс проходит под расслабляющую музыку. Перед началом процедуры гостям предлагается элитный чай или кофе на выбор.</p>
    <hr style='border-color: #bc987e;'>
    <h4>Цена: 45 BYN / час</h4>
</div>
""", unsafe_allow_html=True)

with p_col2:
    # Публичная ссылка на твое фото №2
    st.image(image2.jpg, use_container_width=True)
    st.markdown("""
<div class="price-card" style="margin-top: -15px;">
    <h3>🌲 Массаж ног</h3>
    <p>Глубокое расслабление и снятие усталости. Включает в себя распаривание стоп на целебных алтайских травах, очищение пор, ингаляцию и чашечка горячего таежного чая с натуральным медом.</p>
    <hr style='border-color: #bc987e;'>
    <h4>Цена: 35 BYN / сеанс</h4>
</div>
""", unsafe_allow_html=True)

with p_col3:
    # Публичная ссылка на твое фото №3
    st.image(image3.jpg, use_container_width=True)
    st.markdown("""
<div class="price-card" style="margin-top: -15px;">
    <h3>💆‍♂️ Спа-Массаж</h3>
    <p>Эксклюзивный уход за телом. Массаж горячими базальтовыми камнями или натуральным кокосовым маслом. Направлен на полное снятие мышечных зажимов и глубокое увлажнение кожи.</p>
    <hr style='border-color: #bc987e;'>
    <h4>Цена: 60 BYN / 60 мин</h4>
</div>
""", unsafe_allow_html=True)

with p_col4:
    # Публичная ссылка на твое фото №4
    st.image(image4.jpg, use_container_width=True)
    st.markdown("""
<div class="price-card" style="margin-top: -15px;">
    <h3>🛁 Молочная ванна</h3>
    <p>Премиальный ритуал красоты. Специальный чан или ванна наполняется теплым молочным раствором, экстрактами трав и лепестками роз. Очищает мысли, снимает усталость и обновляет кожу.</p>
    <hr style='border-color: #bc987e;'>
    <h4>Цена: 50 BYN / час</h4>
</div>
""", unsafe_allow_html=True)

st.divider()

# 5. Форма отправки на почту
st.markdown("<h2>📩 Онлайн-резервирование визита</h2>", unsafe_allow_html=True)

FORMSPREE_URL = "https://formspree.io" 

form_html = f"""
<form action="{FORMSPREE_URL}" method="POST" style="background-color: rgba(25, 20, 18, 0.9); padding: 30px; border-radius: 12px; border: 1px solid #4a3b32;">
    <div style="margin-bottom: 20px;">
        <label style="font-weight: bold; color: #dfba9d !important; display: block; margin-bottom: 8px;">Ваше имя:</label>
        <input type="text" name="name" required style="width: 100%; padding: 12px; background-color: #140f0d; border: 1px solid #bc987e; border-radius: 6px; color: white;">
    </div>
    <div style="margin-bottom: 20px;">
        <label style="font-weight: bold; color: #dfba9d !important; display: block; margin-bottom: 8px;">Контактный Email или телефон:</label>
        <input type="email" name="_replyto" required style="width: 100%; padding: 12px; background-color: #140f0d; border: 1px solid #bc987e; border-radius: 6px; color: white;">
    </div>
    <div style="margin-bottom: 20px;">
        <label style="font-weight: bold; color: #dfba9d !important; display: block; margin-bottom: 8px;">Ваши пожелания к заказу:</label>
        <textarea name="message" required style="width: 100%; height: 120px; padding: 12px; background-color: #140f0d; border: 1px solid #bc987e; border-radius: 6px; color: white; resize: none;"></textarea>
    </div>
    <button type="submit" style="background-color: #bc987e; color: #231f20; padding: 14px 28px; border: none; border-radius: 6px; cursor: pointer; font-size: 16px; font-weight: bold; width: 100%; text-transform: uppercase; letter-spacing: 1px;">
        Подтвердить бронирование визита
    </button>
</form>
"""

st.markdown(form_html, unsafe_allow_html=True)

st.divider()
st.caption("© 2026 Ketrin Plase. Режим работы: с 9:00 до 23:00 ежедневно. Все права защищены.")
