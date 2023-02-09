# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import streamlit as st
import pandas as pd
import plotly.express as px
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)
    #df = pd.read_excel(r"C:\Users\aspirex99\Documents\DIGICIDES_MACROS SHEET\final_2.xlsx")
    df = df.iloc[:,1:]

    def plot_pie_charts(df, column_name):
        figures = []
        col = df[column_name]
        x = []
        y = []
        for i in pd.DataFrame(df.groupby([col, 'Clients'])).iloc[1:,0]:
            x.append(i[0])
            y.append(i[1])
        u = pd.DataFrame({'status' : x,
                         'client' : y})

        u['count'] = 0
        u['per'] = 0
        opt_count = u[u['status'] == 'Opted']['status'].count()
        not_opt_count = u[u['status'] == 'Not Opted']['status'].count()
        total_count = opt_count + not_opt_count
        u.loc[u['status'] == 'Opted', 'count'] = opt_count
        u.loc[u['status'] == 'Not Opted', 'count'] = not_opt_count
        u.loc[u['status'] == 'Opted', 'per'] = opt_count / total_count
        u.loc[u['status'] == 'Not Opted', 'per'] = not_opt_count / total_count

        fig = px.pie(u, values='count', names='client', color='status', title=column_name, hole=.6,
                     color_discrete_sequence=["red", "yellow"])
        fig.update_traces(textposition='outside', textinfo='label')
        figures.append(fig)
        return figures
    st.sidebar.image('https://media.licdn.com/dms/image/C510BAQFZsV_j-73Tzw/company-logo_200_200/0/1519890386330?e=1683763200&v=beta&t=-8K5AWdR9zXC79DfaOvfaAJl5XuuguM6MEwFaYqXXdc')
    st.title("Digicides")

    cols = ['Diginews', 'OBD/IVR', 'Whatsapp promotional', 'SMS',
           'Only Miss Call', 'SMS/Whatsapp Plugin', 'Digiscan', 'Digiask',
           'DigiSampling', 'CPI', 'CPL', 'DigiServices']

    column_name = st.sidebar.selectbox("Select Product", cols, index=0)

    figures = plot_pie_charts(df, column_name)
    st.plotly_chart(figures[0])
    def ploting(cn):
        x = []
        y = []
        for i in pd.DataFrame(df.groupby([cn,'Clients'])).iloc[1:,0]:
            x.append(i[0])
            y.append(i[1])
        u = pd.DataFrame({'status' : x,
                     'client' : y})

        u['status'].value_counts().values[1]
        u['count'] = 0
        u['per'] = 0
        opt_count = u[u['status'] == 'Opted']['status'].count()
        not_opt_count = u[u['status'] == 'Not Opted']['status'].count()
        total_count = opt_count + not_opt_count
        u.loc[u['status'] == 'Opted', 'count'] = opt_count
        u.loc[u['status'] == 'Not Opted', 'count'] = not_opt_count
        u.loc[u['status'] == 'Opted', 'per'] = opt_count / total_count
        u.loc[u['status'] == 'Not Opted', 'per'] = not_opt_count / total_count
        return u
    df = ploting(column_name)
    total_count = df['count'].sum()
    df['percentage'] = df['count'] / total_count * 100

    fig = px.bar(df, x='status', y='count', color='status', title='Clients Status',
                color_discrete_sequence=["cyan", "yellow"])

    fig.update_layout(
        xaxis=dict(
            ticktext=[f"{count} Clients ({percentage:.2f}%)" for count, percentage in zip(df['count'], df['percentage'])],
            tickvals=df['status'],
        )
    )

    st.plotly_chart(fig)
