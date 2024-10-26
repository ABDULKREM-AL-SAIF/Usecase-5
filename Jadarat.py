import numpy as np
import pandas as pd
import plotly.express as px

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
        chart = px.pie(df_Q1, values='count', names='region')
        chart.update_traces(textposition='inside')
        chart.update_layout(uniformtext_minsize=25, margin=dict(t=0, b=0, l=0, r=0), uniformtext_mode='hide')
        return chart
    
    def load_Q2_chart(self):
        df_Q2 = self.__Q2()
        chart = px.pie(df_Q2, values='count', names='gender')
        chart.update_traces(textposition='inside')
        chart.update_layout(uniformtext_minsize=15, margin=dict(t=0, b=0, l=0, r=0), uniformtext_mode='hide')
        return chart
    
    def load_Q4_chart(self):
        df_Q4 = self.__Q4()
        chart = px.bar(data_frame = df_Q4, x = 'year', y = 'count')
        chart.update_traces(textposition='inside', texttemplate=list(df_Q4['count']))
        chart.update_layout(uniformtext_minsize=15, margin=dict(t=0, b=0, l=0, r=0), uniformtext_mode='hide')
        return chart
