import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
import requests
from streamlit_lottie import st_lottie

# إعدادات الصفحة
st.set_page_config(
    page_title="بريجو - المقاولات العامة والتشطيبات",
    page_icon="🏗️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# تحميل الرسوم المتحركة Lottie
def load_lottieurl(url):
    try:
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    except:
        return None

# تحميل CSS مخصص محسن للمقاولات
def local_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@300;400;500;700;800&display=swap');
    
    * {
        font-family: 'Tajawal', sans-serif;
    }
    
    .main-header {
        font-size: 4rem;
        color: #2E86AB;
        text-align: center;
        margin-bottom: 2rem;
        font-weight: 800;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        background: linear-gradient(45deg, #2E86AB, #A23B72);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    .section-header {
        font-size: 2.5rem;
        color: #2E86AB;
        border-bottom: 3px solid #F18F01;
        padding-bottom: 0.5rem;
        margin-top: 3rem;
        margin-bottom: 2rem;
        font-weight: 700;
        position: relative;
    }
    
    .section-header:after {
        content: '';
        position: absolute;
        bottom: -3px;
        left: 0;
        width: 100px;
        height: 3px;
        background: #A23B72;
    }
    
    .sub-section {
        background: linear-gradient(135deg, #f8f9fa 0%, #ffffff 100%);
        padding: 2rem;
        border-radius: 15px;
        margin-bottom: 2rem;
        border-left: 5px solid #2E86AB;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.08);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    .sub-section:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 40px rgba(0, 0, 0, 0.12);
    }
    
    .project-card {
        background: white;
        border-radius: 15px;
        padding: 1.5rem;
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1);
        margin-bottom: 1.5rem;
        transition: all 0.3s ease;
        border: 1px solid #e9ecef;
        position: relative;
        overflow: hidden;
    }
    
    .project-card:before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 5px;
        height: 100%;
        background: linear-gradient(to bottom, #2E86AB, #A23B72);
    }
    
    .project-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.15);
    }
    
    .service-card {
        background: white;
        border-radius: 15px;
        padding: 2rem;
        text-align: center;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
        transition: all 0.3s ease;
        border: 1px solid #e9ecef;
        height: 100%;
    }
    
    .service-card:hover {
        transform: translateY(-10px);
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.15);
        background: linear-gradient(135deg, #2E86AB, #A23B72);
        color: white;
    }
    
    .service-card:hover h3,
    .service-card:hover p {
        color: white;
    }
    
    .construction-card {
        background: linear-gradient(135deg, #2E86AB 0%, #A23B72 100%);
        color: white;
        border-radius: 15px;
        padding: 2rem;
        margin: 1rem 0;
        box-shadow: 0 10px 30px rgba(42, 134, 171, 0.3);
        position: relative;
        overflow: hidden;
    }
    
    .construction-card:before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, rgba(255,255,255,0) 70%);
    }
    
    .phase-card {
        background: white;
        border-radius: 10px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
        border-left: 4px solid #F18F01;
    }
    
    .stButton button {
        background: linear-gradient(135deg, #2E86AB 0%, #A23B72 100%);
        color: white;
        border: none;
        padding: 0.75rem 2rem;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 1rem;
        margin: 0.5rem 0.25rem;
        cursor: pointer;
        border-radius: 50px;
        font-weight: 600;
        transition: all 0.3s ease;
        box-shadow: 0 5px 15px rgba(42, 134, 171, 0.4);
    }
    
    .stButton button:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 25px rgba(42, 134, 171, 0.6);
        background: linear-gradient(135deg, #A23B72 0%, #2E86AB 100%);
    }
    
    .stats-container {
        background: linear-gradient(135deg, #2E86AB 0%, #A23B72 100%);
        color: white;
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        margin: 2rem 0;
    }
    
    .stat-number {
        font-size: 3rem;
        font-weight: 800;
        margin-bottom: 0.5rem;
    }
    
    .stat-label {
        font-size: 1.2rem;
        opacity: 0.9;
    }
    
    .testimonial-card {
        background: white;
        border-radius: 15px;
        padding: 2rem;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
        margin: 1rem;
        border-left: 5px solid #F18F01;
        position: relative;
    }
    
    .testimonial-card:before {
        content: '"';
        position: absolute;
        top: 10px;
        right: 20px;
        font-size: 5rem;
        color: #F18F01;
        opacity: 0.2;
        font-family: Georgia, serif;
    }
    
    .footer {
        background: linear-gradient(135deg, #2E86AB 0%, #A23B72 100%);
        color: white;
        padding: 3rem 2rem;
        border-radius: 15px;
        margin-top: 3rem;
        text-align: center;
    }
    
    .gradient-text {
        background: linear-gradient(45deg, #2E86AB, #A23B72, #F18F01);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800;
    }
    
    .timeline {
        position: relative;
        max-width: 1200px;
        margin: 0 auto;
    }
    
    .timeline::after {
        content: '';
        position: absolute;
        width: 6px;
        background-color: #2E86AB;
        top: 0;
        bottom: 0;
        left: 50%;
        margin-left: -3px;
    }
    
    .timeline-item {
        padding: 10px 40px;
        position: relative;
        width: 50%;
        box-sizing: border-box;
    }
    
    .timeline-item::after {
        content: '';
        position: absolute;
        width: 25px;
        height: 25px;
        right: -13px;
        background-color: white;
        border: 4px solid #F18F01;
        top: 15px;
        border-radius: 50%;
        z-index: 1;
    }
    
    .left {
        left: 0;
    }
    
    .right {
        left: 50%;
    }
    
    .left::before {
        content: " ";
        height: 0;
        position: absolute;
        top: 22px;
        width: 0;
        z-index: 1;
        right: 30px;
        border: medium solid white;
        border-width: 10px 0 10px 10px;
        border-color: transparent transparent transparent white;
    }
    
    .right::before {
        content: " ";
        height: 0;
        position: absolute;
        top: 22px;
        width: 0;
        z-index: 1;
        left: 30px;
        border: medium solid white;
        border-width: 10px 10px 10px 0;
        border-color: transparent white transparent transparent;
    }
    
    .right::after {
        left: -13px;
    }
    
    .timeline-content {
        padding: 20px 30px;
        background-color: white;
        position: relative;
        border-radius: 6px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
    }
    </style>
    """, unsafe_allow_html=True)

local_css()

# تحميل الرسوم المتحركة
lottie_construction = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_vybwn7df.json")
lottie_design = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_gn0tojcq.json")

# البيانات
construction_services = [
    {"title": "المقاولات العامة", "icon": "🏗️", "description": "تنفيذ مشاريع بناء متكاملة من التصميم إلى التسليم"},
    {"title": "التصميم المعماري", "icon": "📐", "description": "تصميم معماري مبتكر يلبي احتياجاتك ويتوافق مع المعايير"},
    {"title": "الإنشاءات", "icon": "🏢", "description": "بناء وتشييد بجودة عالية ومواد مستدامة"},
    {"title": "الإشراف الهندسي", "icon": "👷", "description": "إشراف هندسي متكامل على جميع مراحل المشروع"},
]

finishing_services = [
    {"title": "التشطيبات الداخلية", "icon": "🎨", "description": "تشطيبات داخلية فاخرة بمواد عالية الجودة"},
    {"title": "التشطيبات الخارجية", "icon": "🏛️", "description": "واجهات وتشطيبات خارجية مميزة ومتينة"},
    {"title": "أعمال البلاط والسيراميك", "icon": "🧱", "description": "تركيب بلاط وسيراميك بدقة واحترافية"},
    {"title": "أعمال الدهان والطلاء", "icon": "🖌️", "description": "أعمال دهان متقنة بألوان عصرية وجذابة"},
]

projects_data = [
    {"name": "برج التجارة", "type": "مقاولات عامة", "image": "https://via.placeholder.com/400x250/2E86AB/FFFFFF?text=برج+التجارة", "description": "بناء وتشييد برج تجاري مكون من 15 طابق", "area": "5000 م²", "duration": "18 شهر", "budget": "15 مليون ريال"},
    {"name": "فيلا السعادة", "type": "تشطيبات", "image": "https://via.placeholder.com/400x250/A23B72/FFFFFF?text=فيلا+السعادة", "description": "تشطيبات كاملة لفيلا فاخرة بمساحة 350 م²", "area": "350 م²", "duration": "6 أشهر", "budget": "2.5 مليون ريال"},
    {"name": "مركز التسوق", "type": "مقاولات عامة", "image": "https://via.placeholder.com/400x250/F18F01/FFFFFF?text=مركز+التسوق", "description": "إنشاء مركز تسوق متكامل الخدمات", "area": "8000 م²", "duration": "24 شهر", "budget": "25 مليون ريال"},
    {"name": "مجمع سكني", "type": "مقاولات عامة", "image": "https://via.placeholder.com/400x250/2E86AB/FFFFFF?text=مجمع+سكني", "description": "بناء مجمع سكني مكون من 20 وحدة", "area": "6000 م²", "duration": "20 شهر", "budget": "18 مليون ريال"},
]

construction_phases = [
    {"phase": "المرحلة الأولى", "title": "التصميم والدراسات", "description": "إعداد التصاميم المعمارية والإنشائية والدراسات الفنية", "duration": "1-2 شهر"},
    {"phase": "المرحلة الثانية", "title": "أعمال الحفر والأساسات", "description": "حفر الموقع وصب الأساسات والهيكل الإنشائي", "duration": "2-3 أشهر"},
    {"phase": "المرحلة الثالثة", "title": "البناء والتشييد", "description": "بناء الجدران والسلالم وتركيب الشبكات الأساسية", "duration": "4-6 أشهر"},
    {"phase": "المرحلة الرابعة", "title": "أعمال التشطيبات", "description": "تشطيبات داخلية وخارجية وتركيب التجهيزات", "duration": "3-4 أشهر"},
    {"phase": "المرحلة الخامسة", "title": "التسليم النهائي", "description": "مراجعة نهائية وتسليم المشروع للعميل", "duration": "2-4 أسابيع"},
]

# شريط جانبي محسن
with st.sidebar:
    
    st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
    st.image(r"3.jpg", width=150)
    st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown('<h2 style="text-align: center; color: #2E86AB; margin-bottom: 0;">بريجو</h2>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center; color: #A23B72; margin-top: 0;">المقاولات العامة والتشطيبات</p>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown("### 🏗️ خدمات المقاولات")
    page = st.radio("", ["🏠 الرئيسية", "📋 خدماتنا", "🏢 المقاولات العامة", "🎨 التشطيبات", "📊 مشاريعنا", "📞 اتصل بنا"], 
                   index=0, label_visibility="collapsed")
    
    st.markdown("---")
    
    st.markdown("### 📞 للاستفسارات السريعة")
    st.markdown("**📞 الهاتف:** 01220851965")
    st.markdown("**📧 البريد:** info@brigoeg.com")
    st.markdown("**العنوان:** السادس من اكتوبر 165 مول اجياد بجوار سيتى سكيب ")
    
    # نموذج طلب استشارة سريع
    st.markdown("---")
    st.markdown("### 💼 طلب استشارة مجانية")
    with st.form("quick_consultation"):
        name = st.text_input("الاسم")
        phone = st.text_input("رقم الهاتف")
        service_type = st.selectbox("نوع الخدمة", ["مقاولات عامة", "تشطيبات", "تصميم", "استشارة"])
        submitted = st.form_submit_button("إرسال الطلب")
        if submitted:
            st.success("شكراً لك! سنتصل بك في أقرب وقت.")

# المحتوى الرئيسي بناءً على الصفحة المحددة
if page == "🏠 الرئيسية":
    st.markdown('<h1 class="main-header">بريجو للمقاولات العامة والتشطيبات</h1>', unsafe_allow_html=True)
    
    # قسم البطل (Hero Section)
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown('<h2 class="section-header">نبني مستقبلك بثقة واحترافية</h2>', unsafe_allow_html=True)
        st.markdown("""
        <div style="font-size: 1.2rem; line-height: 1.8;">
        <p>في <span class="gradient-text">بريجو</span>، نتميز بأكثر من <strong>15 عاماً</strong> من الخبرة في مجال المقاولات العامة والتشطيبات. 
        نحن نقدم حلولاً متكاملة تلبي أعلى معايير الجودة والسلامة.</p>
        
        <p>نفخر بتسليم <strong>500+ مشروع</strong> ناجح، من المشاريع السكنية والتجارية إلى المشاريع الحكومية والصناعية.</p>
        
        <p>نلتزم بمواعيد التسليم ونعمل ضمن الميزانيات المتفق عليها، مع الحفاظ على أعلى معايير الجودة والكفاءة.</p>
        </div>
        """, unsafe_allow_html=True)
        
        col1_1, col1_2 = st.columns(2)
        with col1_1:
            st.button("📞 اطلب استشارة مجانية")
        with col1_2:
            st.button("👀 شاهد مشاريعنا")
    
    with col2:
        if lottie_construction:
            st_lottie(lottie_construction, height=300, key="construction_animation")
        else:
            st.image("https://via.placeholder.com/400x300/2E86AB/FFFFFF?text=بريجو+للمقاولات", width=400)
    
    # إحصائيات
    st.markdown('<div class="stats-container">', unsafe_allow_html=True)
    st.markdown('<h2 style="text-align: center; color: white; margin-bottom: 2rem;">إنجازاتنا بالأرقام</h2>', unsafe_allow_html=True)
    
    col3, col4, col5, col6 = st.columns(4)
    with col3:
        st.markdown('<div class="stat-number">15+</div>', unsafe_allow_html=True)
        st.markdown('<div class="stat-label">سنوات من الخبرة</div>', unsafe_allow_html=True)
    with col4:
        st.markdown('<div class="stat-number">500+</div>', unsafe_allow_html=True)
        st.markdown('<div class="stat-label">مشروع مكتمل</div>', unsafe_allow_html=True)
    with col5:
        st.markdown('<div class="stat-number">98%</div>', unsafe_allow_html=True)
        st.markdown('<div class="stat-label">رضا العملاء</div>', unsafe_allow_html=True)
    with col6:
        st.markdown('<div class="stat-number">250+</div>', unsafe_allow_html=True)
        st.markdown('<div class="stat-label">فريق متخصص</div>', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # لماذا تختار بريجو؟
    st.markdown('<h2 class="section-header">لماذا تختار بريجو للمقاولات؟</h2>', unsafe_allow_html=True)
    
    col7, col8 = st.columns(2)
    
    with col7:
        st.markdown("""
        <div class="sub-section">
            <h3 style="color: #2E86AB; margin-top: 0;">🏆 الجودة والاحترافية</h3>
            <p>نلتزم بأعلى معايير الجودة في جميع مشاريعنا، باستخدام أفضل المواد وأحدث التقنيات.</p>
        </div>
        
        <div class="sub-section">
            <h3 style="color: #2E86AB; margin-top: 0;">⏱️ الالتزام بالوقت</h3>
            <p>نقدر قيمة وقتك ونلتزم بتسليم مشاريعنا في المواعيد المتفق عليها بدقة.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col8:
        st.markdown("""
        <div class="sub-section">
            <h3 style="color: #2E86AB; margin-top: 0;">💡 حلول هندسية مبدعة</h3>
            <p>نقدم حلولاً هندسية مبتكرة تناسب احتياجاتك وتفوق توقعاتك.</p>
        </div>
        
        <div class="sub-section">
            <h3 style="color: #2E86AB; margin-top: 0;">💰 شفافية في التسعير</h3>
            <p>نوفر عروض أسعار شفافة وواضحة دون مفاجآت أو تكاليف خفية.</p>
        </div>
        """, unsafe_allow_html=True)

elif page == "📋 خدماتنا":
    st.markdown('<h1 class="section-header">خدماتنا المتكاملة</h1>', unsafe_allow_html=True)
    
    # خدمات المقاولات العامة
    st.markdown('<h2 style="color: #2E86AB; margin-top: 2rem;">🏗️ خدمات المقاولات العامة</h2>', unsafe_allow_html=True)
    
    cols = st.columns(4)
    for i, service in enumerate(construction_services):
        with cols[i]:
            st.markdown(f"""
            <div class="service-card">
                <div style="font-size: 3rem; margin-bottom: 1rem;">{service['icon']}</div>
                <h3 style="color: #2E86AB; margin-bottom: 1rem;">{service['title']}</h3>
                <p style="color: #555;">{service['description']}</p>
            </div>
            """, unsafe_allow_html=True)
    
    # خدمات التشطيبات
    st.markdown('<h2 style="color: #2E86AB; margin-top: 3rem;">🎨 خدمات التشطيبات</h2>', unsafe_allow_html=True)
    
    cols = st.columns(4)
    for i, service in enumerate(finishing_services):
        with cols[i]:
            st.markdown(f"""
            <div class="service-card">
                <div style="font-size: 3rem; margin-bottom: 1rem;">{service['icon']}</div>
                <h3 style="color: #2E86AB; margin-bottom: 1rem;">{service['title']}</h3>
                <p style="color: #555;">{service['description']}</p>
            </div>
            """, unsafe_allow_html=True)
    
    # عملية العمل
    st.markdown('<h2 class="section-header">كيف نعمل</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="timeline">
        <div class="timeline-item left">
            <div class="timeline-content">
                <h3>الاستشارة والتخطيط</h3>
                <p>نبدأ بفهم احتياجاتك وتوقعاتك، ثم نضع خطة عمل مفصلة</p>
            </div>
        </div>
        <div class="timeline-item right">
            <div class="timeline-content">
                <h3>التصميم والدراسات</h3>
                <p>نعد التصاميم المعمارية والإنشائية والدراسات الفنية اللازمة</p>
            </div>
        </div>
        <div class="timeline-item left">
            <div class="timeline-content">
                <h3>التنفيذ والبناء</h3>
                <p>ننفذ المشروع باحترافية عالية مع الالتزام بمعايير الجودة</p>
            </div>
        </div>
        <div class="timeline-item right">
            <div class="timeline-content">
                <h3>التسليم والمتابعة</h3>
                <p>نسلم المشروع في الوقت المحدد ونوفر خدمة ما بعد البيع</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

elif page == "🏢 المقاولات العامة":
    st.markdown('<h1 class="section-header">المقاولات العامة</h1>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        <div style="font-size: 1.2rem; line-height: 1.8;">
        <p>نقدم في <span class="gradient-text">بريجو</span> خدمات المقاولات العامة الشاملة التي تغطي جميع مراحل البناء، 
        من التصميم الأولي إلى التسليم النهائي.</p>
        
        <p>نتميز بخبرة واسعة في تنفيذ مختلف أنواع المشاريع:</p>
        <ul>
            <li>المشاريع السكنية (فلل، مجمعات سكنية)</li>
            <li>المشاريع التجارية (مراكز تسوق، مكاتب)</li>
            <li>المشاريع الصناعية (مصانع، مستودعات)</li>
            <li>المشاريع الحكومية والمرافق العامة</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.image("https://via.placeholder.com/400x300/2E86AB/FFFFFF?text=المقاولات+العامة", use_column_width=True)
    
    # مراحل تنفيذ المشاريع
    st.markdown('<h2 class="section-header">مراحل تنفيذ المشاريع</h2>', unsafe_allow_html=True)
    
    for phase in construction_phases:
        st.markdown(f"""
        <div class="phase-card">
            <h3 style="color: #2E86AB; margin-top: 0;">{phase['phase']}: {phase['title']}</h3>
            <p><strong>المدة:</strong> {phase['duration']}</p>
            <p>{phase['description']}</p>
        </div>
        """, unsafe_allow_html=True)
    
    # أنواع المشاريع
    st.markdown('<h2 class="section-header">أنواع المشاريع التي ننفذها</h2>', unsafe_allow_html=True)
    
    col3, col4, col5 = st.columns(3)
    
    with col3:
        st.markdown("""
        <div class="construction-card">
            <h3>🏠 المشاريع السكنية</h3>
            <p>بناء وتشييد الفلل، المجمعات السكنية، الشقق</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="construction-card">
            <h3>🏢 المشاريع التجارية</h3>
            <p>مراكز التسوق، المباني الإدارية، المطاعم</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col5:
        st.markdown("""
        <div class="construction-card">
            <h3>🏭 المشاريع الصناعية</h3>
            <p>المصانع، المستودعات، المنشآت الصناعية</p>
        </div>
        """, unsafe_allow_html=True)

elif page == "🎨 التشطيبات":
    st.markdown('<h1 class="section-header">خدمات التشطيبات</h1>', unsafe_allow_html=True)
    
    st.markdown("""
    <div style="font-size: 1.2rem; line-height: 1.8;">
    <p>نقدم في <span class="gradient-text">بريجو</span> خدمات تشطيبات متكاملة تجمع بين الجمال والمتانة، 
    باستخدام أحدث التقنيات وأجود المواد.</p>
    
    <p>نحرص على أدق التفاصيل لضمان نتائج مبهرة تناسب ذوقك وتلبي توقعاتك.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # أنواع التشطيبات
    finishing_tabs = st.tabs(["التشطيبات الداخلية", "التشطيبات الخارجية", "أعمال الدهان", "أعمال البلاط"])
    
    with finishing_tabs[0]:
        st.markdown("""
        <div class="sub-section">
            <h3>التشطيبات الداخلية المتكاملة</h3>
            <p>نقدم تشطيبات داخلية شاملة تشمل:</p>
            <ul>
                <li>تركيب الأرضيات (سيراميك، باركيه، رخام)</li>
                <li>تركيب الأسقف المعلقة والجبسية</li>
                <li>تركيب الأبواب والشبابيك</li>
                <li>تشطيب الحمامات والمطابخ</li>
                <li>تركيب الإضاءة والتجهيزات الكهربائية</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            st.image("https://via.placeholder.com/400x300/2E86AB/FFFFFF?text=تشطيبات+داخلية+1", use_column_width=True)
        with col2:
            st.image("https://via.placeholder.com/400x300/A23B72/FFFFFF?text=تشطيبات+داخلية+2", use_column_width=True)
    
    with finishing_tabs[1]:
        st.markdown("""
        <div class="sub-section">
            <h3>التشطيبات الخارجية المتميزة</h3>
            <p>تشطيبات خارجية تجمع بين الجمال والمتانة:</p>
            <ul>
                <li>تشطيب الواجهات (حجر، رخام، طلاء)</li>
                <li>أعمال العزل المائي والحراري</li>
                <li>تشطيب المداخل والسلالم الخارجية</li>
                <li>أعمال المناظر الطبيعية والحدائق</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # نماذج التشطيبات
    st.markdown('<h2 class="section-header">أنماط التشطيبات</h2>', unsafe_allow_html=True)
    
    col6, col7, col8 = st.columns(3)
    
    with col6:
        st.markdown("""
        <div class="service-card">
            <h3>التشطيبات الكلاسيكية</h3>
            <p>أناقة وفخامة مع لمسات تراثية أصيلة</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col7:
        st.markdown("""
        <div class="service-card">
            <h3>التشطيبات الحديثة</h3>
            <p>بساطة وأناقة مع خطوط نظيفة وألوان هادئة</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col8:
        st.markdown("""
        <div class="service-card">
            <h3>التشطيبات المختلطة</h3>
            <p>دمج بين الأنماط الكلاسيكية والحديثة</p>
        </div>
        """, unsafe_allow_html=True)

elif page == "📊 مشاريعنا":
    st.markdown('<h1 class="section-header">معرض مشاريعنا</h1>', unsafe_allow_html=True)
    
    # فلترة المشاريع
    col1, col2, col3 = st.columns([1, 1, 2])
    with col1:
        project_type = st.selectbox("نوع المشروع", ["جميع المشاريع", "مقاولات عامة", "تشطيبات"])
    with col2:
        budget_range = st.selectbox("نطاق الميزانية", ["جميع الميزانيات", "أقل من 5 ملايين", "5-15 مليون", "أكثر من 15 مليون"])
    
    # عرض المشاريع
    filtered_projects = projects_data 
    if project_type != "جميع المشاريع":
        filtered_projects = [p for p in projects_data if p["type"] == project_type]
    
    for project in filtered_projects:
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image(project["image"], use_column_width=True)
        with col2:
            st.markdown(f"""
            <div class="project-card">
                <h3>{project['name']}</h3>
                <p><strong>نوع المشروع:</strong> {project['type']}</p>
                <p><strong>المساحة:</strong> {project['area']}</p>
                <p><strong>مدة التنفيذ:</strong> {project['duration']}</p>
                <p><strong>الميزانية:</strong> {project['budget']}</p>
                <p>{project['description']}</p>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("---")

elif page == "📞 اتصل بنا":
    st.markdown('<h1 class="section-header">تواصل معنا</h1>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="construction-card">
            <h2 style="color: white; margin-top: 0;">لنبدأ مشروعك معاً</h2>
            <p>نحن هنا لمساعدتك في تحقيق مشروعك الإنشائي. تواصل معنا اليوم للحصول على استشارة مجانية.</p>
            
            <div style="margin-top: 2rem;">
                <p>📞 <strong>الهاتف:</strong>01220851965</p>
                <p>📧 <strong>البريد الإلكتروني:</strong> info@brigoeg.com</p>
                <p>📍 <strong>العنوان:</strong> السادس من اكتوبر - 165 مول اجياد بجوار سيتى سكيب </p>
            </div>
            
            <div style="margin-top: 2rem;">
                <h3>ساعات العمل</h3>
                <p>الأحد - الخميس: 8:00 ص - 6:00 م</p>
                <p>الجمعة: مغلق</p>
                <p>السبت: 10:00 ص - 4:00 م</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("### أرسل لنا رسالة")
        
        with st.form("contact_form", clear_on_submit=True):
            name = st.text_input("الاسم بالكامل *")
            email = st.text_input("البريد الإلكتروني *")
            phone = st.text_input("رقم الهاتف *")
            service = st.selectbox("نوع الخدمة المطلوبة *", 
                                 ["", "مقاولات عامة", "تشطيبات", "تصميم معماري", "إشراف هندسي", "استشارة"])
            project_type = st.selectbox("نوع المشروع", 
                                      ["", "سكني", "تجاري", "صناعي", "حكومي", "آخر"])
            message = st.text_area("الرسالة *", height=150)
            
            submitted = st.form_submit_button("إرسال الرسالة")
            if submitted:
                if name and email and phone and service and message:
                    st.success("شكراً لك! تم استلام رسالتك وسنتواصل معك خلال 24 ساعة.")
                else:
                    st.error("يرجى ملء جميع الحقول الإلزامية (*)")

# تذييل الصفحة
st.markdown("""
<div class="footer">
    <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap;">
        <div style="text-align: right;">
            <h3 style="margin-bottom: 1rem;">بريجو للمقاولات العامة والتشطيبات</h3>
            <p>نبني مستقبلك بثقة واحترافية</p>
        </div>
        
        <div style="text-align: left;">
            <p>تابعنا على:</p>
            <p>فيسبوك | إنستجرام | تويتر | لينكد إن</p>
        </div>
    </div>
    
    <div style="margin-top: 2rem; padding-top: 1rem; border-top: 1px solid rgba(255,255,255,0.3);">
        <p>جميع الحقوق محفوظة © 2023 بريجو | تصميم وتطوير: فريق بريجو</p>
    </div>
</div>

""", unsafe_allow_html=True)



