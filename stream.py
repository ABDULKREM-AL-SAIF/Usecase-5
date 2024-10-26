import streamlit as st
import streamlit.components.v1 as components

import numpy as np
import pandas as pd
import plotly.express as px

#st.set_page_config(layout="wide")

class Jadarat:

    def __init__(self):
        self.__df = pd.read_csv('Jadarat_data.csv')
        self.__clean_data()
    
    def __stringToList(self, element):
        if pd.isna(element):
            return ['لا توجد معلومات']
        else:
            return eval(element)

    def __clean_data(self):
        mask = self.__df[self.__df['eco_activity'].isnull()].index.tolist()
        self.__df = self.__df.drop(mask)

        mask = self.__df[self.__df['comp_size'].isnull()].index.tolist()
        self.__df = self.__df.drop(mask)

        self.__df['benefits'] = self.__df['benefits'].apply(self.__stringToList)

        self.__df['salary'] = self.__df['benefits'].apply(lambda x : x[1])
        self.__df['salary'] = self.__df['salary'].astype(float)

        self.__df.rename(columns={'exper': 'exper_year'}, inplace=True)
        self.__df['exper_year'].replace(' Years', '', regex = True, inplace=True)
        self.__df['exper_year'] = self.__df['exper_year'].astype(int)


    
    def __Q1(self):
        Q1 = self.__df.groupby(by = 'region').size().sort_values(ascending = False)
        D1 = { 'region' : [] , 'count' : [] }
        df_Q1 = pd.DataFrame({ 'region' : Q1.index, 'count' : Q1.values })
        return df_Q1
    
    def __Q2(self):
        Q2 = self.__df.groupby(by = 'gender').size().sort_values(ascending = False)
        D2 = { 'gender' : [] , 'count' : [] }
        df_Q2 = pd.DataFrame({ 'gender' : Q2.index, 'count' : Q2.values })
        df_Q2['gender'] = ['كلاهما  ', ' رجال ', 'نساء']
        return df_Q2

    def Q3(self):
        Q3 = self.__df[self.__df['exper_year'] == 0]
        mi = Q3['salary'].min()
        mx = Q3['salary'].max()
        return f' أقل راتب متوقع هو { mi } و أعلى راتب متوقع هو { mx } '

    def __Q4(self):
        Q4 = self.__df.groupby('exper_year').size().sort_values(ascending = False)
        df_Q4 = pd.DataFrame({ 'year' : Q4.index, 'count' : Q4.values })
        return df_Q4

    def load_Q1_chart(self):
        df_Q1 = self.__Q1()
        char = px.pie(df_Q1, values='count', names='region')
        char.update_traces(textposition='inside')
        char.update_layout(uniformtext_minsize=25, margin=dict(t=0, b=0, l=0, r=0), uniformtext_mode='hide')
        st.plotly_chart(char, use_container_width = True)
    
    def load_Q2_chart(self):
        df_Q2 = self.__Q2()
        char = px.pie(df_Q2, values='count', names='gender')
        char.update_traces(textposition='inside')
        char.update_layout(uniformtext_minsize=15, margin=dict(t=0, b=0, l=0, r=0), uniformtext_mode='hide')
        st.plotly_chart(char, use_container_width = True)
    
    def load_Q4_chart(self):
        df_Q4 = self.__Q4()
        char = px.bar(data_frame = df_Q4, x = 'year', y = 'count')
        char.update_traces(textposition='inside', texttemplate=list(df_Q4['count']))
        char.update_layout(uniformtext_minsize=15, margin=dict(t=0, b=0, l=0, r=0), uniformtext_mode='hide')
        st.plotly_chart(char, use_container_width = True)
    
jadarat = Jadarat()

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
st.markdown(text, unsafe_allow_html=True)
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")

st.subheader(" ما هي المدينة الأكثر طلبا للوظائف ؟ ")

st.write(" ")
st.write(" ")

jadarat.load_Q1_chart()

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

jadarat.load_Q2_chart()

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

jadarat.load_Q4_chart()

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