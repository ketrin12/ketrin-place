import streamlit as st

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

/* Намертво красим ВСЕ обычные буквы на сайте в читаемый темно-коричневый цвет */
p, span, label, li, div, b, th, td { 
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
</style>
""", unsafe_allow_html=True)

# 2. НАДЁЖНАЯ ШАПКА (100% СРАБОТАЕТ)
st.title("🌸 Салон «Ketrin Plase» в Гомеле")
st.subheader("Услуги • Сертификаты • Галерея • Цены • Контакты")
st.divider()

# 3. Главный баннер
col1, col2 = st.columns([1.2, 1])

with col1:
    st.markdown("<h4 style='text-transform: uppercase; letter-spacing: 2px;'>Премиум отдых в Гомеле</h4>", unsafe_allow_html=True)
    st.header("Новая процедура: СПА для волос и тела")
    st.write("📍 **Гомель, ул. Карповича**")
    st.write(
        "Погрузитесь в атмосферу полного блаженства. Наш салон создан для того, "
        "чтобы вы могли отдохнуть от городской суеты, восстановить силы и позаботиться о себе."
    )
    st.write("### 🔥 Скидка -20% на первое посещение!")

with col2:
    spa_image = "https://unsplash.com"
    st.image(spa_image, caption="Интерьер Ketrin Plase", use_container_width=True)

st.divider()

# 4. БЛОК: УСЛУГИ И ЦЕНЫ (ИСПРАВИЛИ ПУТИ К КАРТИНКАМ)
st.write("## 🌸 Наши услуги и привилегии")
st.write("")

p_col1, p_col2, p_col3 = st.columns(3)

with p_col1:
    # Исправили путь к первой картинке!
    st.image("images/image1.jpg", use_container_width=True)
    st.markdown("""
<div class="price-card">
    <h3 style="color: #3d2f2b;">🛁 Тайский массаж</h3>
    <p><b>Что включено:</b> массаж всего тела! Помогает для тех у кого проблемы со спиной. В течении массажа будет играть расслабляющая музыка, а в начале массажа подают чай или кофе на выбор.</p>
    <hr style='border-color: #bc987e;'>
    <h4 style="color: #3d2f2b;">Цена: 45 BYN / час</h4>
</div>
""", unsafe_allow_html=True)

with p_col2:
    # Исправили путь ко второй картинке!
    st.image("images/image2.jpg", use_container_width=True)
    st.markdown("""
<div class="price-card">
    <h3 style="color: #3d2f2b;">🌲 Массаж ног</h3>
    <p><b>Что включено:</b> Распаривание на целебных алтайских травах, глубокое очищение пор, ингаляция и чашечка горячего таежного чая с медом.</p>
    <hr style='border-color: #bc987e;'>
    <h4 style="color: #3d2f2b;">Цена: 35 BYN / сеанс</h4>
</div>
""", unsafe_allow_html=True)

with p_col3:
    # Исправили путь к третьей картинке!
    st.image("images/image3.jpg", use_container_width=True)
    st.markdown("""
<div class="price-card">
    <h3 style="color: #3d2f2b;">💆‍♂️ Спа-Массаж</h3>
    <p><b>Что включено:</b> Массаж всего тела горячими камнями или кокосовым маслом, снятие зажимов и усталости, увлажнение кожи.</p>
    <hr style='border-color: #bc987e;'>
    <h4 style="color: #3d2f2b;">Цена: 60 BYN / 60 мин</h4>
</div>
""", unsafe_allow_html=True)

st.divider()

# 5. Форма отправки на почту
st.write("## 📩 Онлайн-запись и вопросы")
st.write("Заполните форму, и детали визита придут администратору на email!")

FORMSPREE_URL = "https://formspree.io" 

form_html = f"""
<form action="{FORMSPREE_URL}" method="POST" style="background-color: white; padding: 25px; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.05);">
    <div style="margin-bottom: 15px;">
        <label style="font-weight: bold; color: #3d2f2b;">Ваше имя:</label><br>
        <input type="text" name="name" required style="width: 100%; padding: 10px; border: 1px solid #ddd; border-radius: 6px; margin-top: 5px;">
    </div>
    <div style="margin-bottom: 15px;">
        <label style="font-weight: bold; color: #3d2f2b;">Ваш Email:</label><br>
        <input type="email" name="_replyto" required style="width: 100%; padding: 10px; border: 1px solid #ddd; border-radius: 6px; margin-top: 5px;">
    </div>
    <div style="margin-bottom: 15px;">
        <label style="font-weight: bold; color: #3d2f2b;">Что вы хотите заказать или спросить?:</label><br>
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
