import streamlit as st
import plotly.graph_objects as go
import numpy as np
import pandas as pd

st.markdown(""" # CATEGORIZAÇÃO DAS ESCOLAS CONFORME PREVISÃO DO IEx""")
url= 'https://raw.githubusercontent.com/silveirafilho/arquivo_mapa/main/dadosmapa99.csv'
df0= pd.read_csv(url)

#df0 = pd.read_csv('/Users/jairosilveirafilho/code/streamlit_sara/pol_edu_streamlit/dadosmapa99.csv', sep=',')
a= list(df0['SG_UF'].unique())
a.insert(0,'Todos')
option = st.selectbox(
    'Selecione um estado:', a)
if option == 'Todos':
    df=df0
else:
    df=df0[df0['SG_UF']==option]
    b= list(df['Município'].unique())
    b.insert(0,'Todos')
    option2 = st.selectbox(
    'Selecione um município:', b)
    if option2 == 'Todos':
        df=df
    else:
        df=df[df['Município']==option2]

classe = st.slider('Selecione uma classe de IEx:', 1,4)


df=df[df['classe']==classe]





import plotly.graph_objects as go

import pandas as pd


fig = go.Figure(data=go.Scattergeo(
        lon = df['lon'],
        lat = df['lat'],
        text = df['Escola'],
        mode = 'markers',
        marker = dict(
            size = 4,
            opacity = 0.8,
            reversescale = True,
            autocolorscale = False,
            symbol =  'circle',
            line = dict(
                width=1,
                color='rgba(102, 102, 102)'
            ),
            colorscale = 'rainbow',
            cmin = 0,
            color = df['IEX'],
            cmax = df['IEX'].max(),
            colorbar_title="Previsão do IEx"
        )))






fig.update_layout(
        height=300,
        margin={"r":0,"t":2,"l":0,"b":0},
        #title = 'MAPA de Previsão do IEx',
        geo = dict(
            scope='south america',
            projection_type='mercator',
            showland = True,
            #landcolor = "rgb(250, 250, 250)",
            #subunitcolor = "rgb(217, 217, 217)",
            #countrycolor = "rgb(217, 217, 217)",
            countrywidth = 0.5,
            subunitwidth = 0.5
        ),
    )


st.plotly_chart(fig)


st.dataframe(df)

@st.cache
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')

csv = convert_df(df)

st.download_button(
    label="Download data as CSV",
    data=csv,
    file_name='df.csv',
    mime='text/csv',
)
