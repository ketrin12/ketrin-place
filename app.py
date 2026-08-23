import streamlit as st
import os

# 1. Настройка страницы в стиле спа-салона
st.set_page_config(
    page_title="Ketrin Plase | SPA & Бани", 
    page_icon="🌸", 
    layout="wide"
)

# ХИТРЫЙ СПОСОБ: Защита от тёмной темы на телефонах
st.markdown("""
<style>
/* Жестко красим фон сайта в желтый */
.stApp, .main, [data-testid="stAppViewContainer"] { 
    background-color: #fef08a !important; 
} 

/* Намертво красим ВСЕ буквы на сайте в читаемый темно-коричневый цвет */
p, span, label, li, div, h1, h2, h3, h4, h5, h6, b, th, td { 
    color: #3d2f2b !important; 
    font-family: 'Georgia', serif !important; 
}

/* Красивые белые карточки для цен */
.price-card {
    background-color: white !important;
    padding: 20px;
    border-radius: 12px;
    box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    border-left: 5px solid #bc987e !important;
    margin-bottom: 20px;
}

/* Белые карточки не должны перекрашивать текст в белый */
.price-card h3, .price-card p, .price-card h4, .price-card b {
    color: #3d2f2b !important;
}
</style>
""", unsafe_allow_html=True)

# 2. Обновленная шапка сайта
st.markdown(
    "<div style='background-color: #3d2f2b; padding: 25px; border-radius: 8px; text-align: center; color: white;'><h1 style='color: #dfba9d !important; margin: 0; font-size: 36px;'>Ketrin Plase</h1><p style='margin: 8px 0 0 0; color: #d1c2ba !important; font-size: 16px;'>Услуги • Сертификаты • Галерея • Цены • Контакты</p></div>", 
    unsafe_allow_html=True
)

st.write("") 

# 3. Главный баннер
col1, col2 = st.columns([1.2, 1])

with col1:
    st.markdown("<h4 style='color: #bc987e !important; text-transform: uppercase; letter-spacing: 2px;'>Премиум отдых в Гомеле</h4>", unsafe_allow_html=True)
    st.title("Новая процедура: СПА для волос и тела")
    st.subheader("📍 Гомель, ул. Карповича")
    st.write(
        "Погрузитесь в атмосферу полного блаженства. Наш салон создан для того, "
        "чтобы вы могли отдохнуть от городской суеты, восстановить силы и позаботиться о себе."
    )
    st.markdown("<h3 style='color: #bc987e !important;'>Скидка -20% на первое посещение!</h3>", unsafe_allow_html=True)

with col2:
    spa_image = "https://unsplash.com"
    st.image(spa_image, caption="Интерьер Ketrin Plase", use_container_width=True)

st.divider()

# 4. БЛОК: УСЛУГИ И ЦЕНЫ
st.markdown("<h2 style='text-align: center;'>🌸 Наши услуги и привилегии</h2>", unsafe_allow_html=True)
st.write("")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
images_folder = os.path.join(BASE_DIR, "images")
img1, img2, img3 = None, None, None

if os.path.exists(images_folder):
    files = sorted([f for f in os.listdir(images_folder) if os.path.isfile(os.path.join(images_folder, f))])
    if len(files) >= 1: img1 = os.path.join(images_folder, files[0])
    if len(files) >= 2: img2 = os.path.join(images_folder, files[1])
    if len(files) >= 3: img3 = os.path.join(images_folder, files[2])

p_col1, p_col2, p_col3 = st.columns(3)

with p_col1:
    if img1: st.image(img1, use_container_width=True)
    st.markdown("""
<div class="price-card" style="margin-top: -15px;">
    <h3>🛁 Тайский массаж</h3>
    <p><b>Что включено:</b> массаж всего тела! Помогает для тех у кого проблемы со спиной. В течении массажа будет играть расслабляющая музыка, а в начале массажа подают чай или кофе на выбор.</p>
    <hr style='border-color: #f5ebe6;'>
    <h4>Цена: 45 BYN / час</h4>
</div>
""", unsafe_allow_html=True)

with p_col2:
    if img2: st.image(img2, use_container_width=True)
    st.markdown("""
<div class="price-card" style="margin-top: -15px;">
    <h3>🌲 Массаж ног</h3>
    <p><b>Что включено:</b> Распаривание на целебных алтайских травах, глубокое очищение пор, ингаляция и чашечка горячего таежного чая с медом.</p>
    <hr style='border-color: #f5ebe6;'>
    <h4>Цена: 35 BYN / сеанс</h4>
</div>
""", unsafe_allow_html=True)

with p_col3:
    if img3: st.image(img3, use_container_width=True)
    st.markdown("""
<div class="price-card" style="margin-top: -15px;">
    <h3>💆‍♂️ Спа-Массаж</h3>
    <p><b>Что включено:</b> Массаж всего тела горячими камнями или кокосовым маслом, снятие зажимов и усталости, увлажнение кожи.</p>
    <hr style='border-color: #f5ebe6;'>
    <h4>Цена: 60 BYN / 60 мин</h4>
</div>
""", unsafe_allow_html=True)

st.divider()

# 5. Форма отправки на почту
st.header("📩 Онлайн-запись и вопросы")
st.write("Заполните форму, и детали визита придут администратору на email!")

# ВСТАВЬ СЮДА СВОЮ ССЫЛКУ ИЗ FORMSPREE, КОТОРУЮ ТЫ СКОПИРОВАЛ РАНЬШЕ:
FORMSPREE_URL = "https://formspree.io" 

form_html = f"""
<form action="{FORMSPREE_URL}" method="POST" style="background-color: white; padding: 25px; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.05);">
    <div style="margin-bottom: 15px;">
        <label style="font-weight: bold;">Ваше имя:</label><br>
        <input type="text" name="name" required style="width: 100%; padding: 10px; border: 1px solid #ddd; border-radius: 6px; margin-top: 5px;">
    </div>
    <div style="margin-bottom: 15px;">
        <label style="font-weight: bold;">Ваш Email:</label><br>
        <input type="email" name="_replyto" required style="width: 100%; padding: 10px; border: 1px solid #ddd; border-radius: 6px; margin-top: 5px;">
    </div>
    <div style="margin-bottom: 15px;">
        <label style="font-weight: bold;">Что вы хотите заказать или спросить?:</label><br>
        <textarea name="message" required style="width: 100%; height: 100px; padding: 10px; border: 1px solid #ddd; border-radius: 6px; margin-top: 5px;"></textarea>
    </div>
    <button type="submit" style="background-color: #3d2f2b; color: white; padding: 12px 24px; border: none; border-radius: 6px; cursor: pointer; font-size: 16px; font-weight: bold; width: 100%;">
        Отправить заявку в Ketrin Plase
    </button>
</form>
"""

st.markdown(form_html, unsafe_allow_html=True)

st.divider()
st.caption("© 2026 Ketrin Plase. Режим работы: с 9:00 до 23:00 ежедневно. Разработано будущим топовым ИТ-специалистом.")
