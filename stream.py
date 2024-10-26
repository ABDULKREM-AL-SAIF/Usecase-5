import streamlit as st
import streamlit.components.v1 as components

from Jadarat import Jadarat
    
jadarat = Jadarat()

st.set_page_config(page_title='تحليل لبيانات موقع جدارات')


st.markdown("""
<style>
body, html {
    direction: RTL;
}
</style>
""", unsafe_allow_html=True)

text = '''
    <p style='padding-right: 50px;font-size:20px;'>
        يعد موقع جدارات أحد مواقع التوظيف المعتمده لدى المملكة العربية السعودية. 
        في هذا المقال سنجيب عن بعض التساؤلات المتعلقه بما قدمته المنصة للباحثين عن العمل.
    </p>
'''

st.title(' ماذا فعل موقع جدارات في سنة 2023 ؟ ')
st.write(" ")
st.write(" ")
st.image("jadarat.png", caption="الصورة الرسمية لموقع جادارات")
st.write(" ")
st.write(" ")
st.markdown(text, unsafe_allow_html=True)
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")

st.subheader(" ما هي المدينة الأكثر طلبا للوظائف ؟ ")

st.write(" ")
st.write(" ")

st.plotly_chart(jadarat.load_Q1_chart(), use_container_width = True)



st.write(" ")
st.write(" ")

text = '''
    <p style='padding-right: 50px;font-size:20px;'>
        في الرسم البياني تحرز الرياض المركز الأول. 
        السبب الأول و هو بالطبع أنها العاصمة للمملكة العربية السعودية 
        و السبب الثاني لأن هنالك الكثير من المشاريع القائمة بسبب رؤية 2030.
        المملكة أعلنت أنها لن تقبل التعاقد مع أي شركه عالمية إلى إذا كان لها مقر إقليمي في 
        المملكة العربية السعودية.
    </p>
'''

st.markdown(text, unsafe_allow_html=True)

st.write(" ")
st.write(" ")

st.subheader(" للذكور أم للإناث ؟ ")

st.write(" ")
st.write(" ")

text = """
    <p style='padding-right: 50px;font-size:20px;'>
        جزء من رئية المملكة العربية السعودية هو رفع نسبة المرأه في سوق العمل.
        لذالك نرى أن تقريبا لايوجد تحيز لجنس معين .
        الأجدر هو من سيجد مكان.
    </p>
"""

st.markdown(text, unsafe_allow_html=True)

st.write(" ")
st.write(" ")

st.plotly_chart(jadarat.load_Q2_chart(), use_container_width = True)

st.write(" ")
st.write(" ")

st.subheader(" فرص الخريجين ؟")

st.write(" ")
st.write(" ")

text = f"""
    <p style='padding-right: 50px;font-size:20px;'>
    دائما ما نسمع أن الشركات تفضل الأشخاص أصحاب الخبره لكن من خلال تحليل بيانات موقع جدارات كانت 
    الأعداد عاليه بالنسبه للأشخاص الذين لايملكون خبره
    </p>
"""

st.markdown(text, unsafe_allow_html=True)


st.plotly_chart(jadarat.load_Q4_chart(), use_container_width = True)

st.write(" ")
st.write(" ")

text = f"""
    <p style='padding-right: 50px;font-size:20px;'>
    {jadarat.Q3()}
    لحديثي التخرج.
    لكن الممللكة رفعت الحد الأدناء للأجور إلى 4000.
    </p>
"""

st.markdown(text, unsafe_allow_html=True)