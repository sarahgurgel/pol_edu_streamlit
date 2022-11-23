import streamlit as st
import plotly.graph_objects as go

import pandas as pd

df = pd.read_csv('/home/sarah/code/sarahgurgel/projeto_streamlit/raw_data/dadosmapa2.csv', sep=',')
df['text'] = df['Escola']


fig = go.Figure(data=go.Scattergeo(
        locationmode = None,
        lon = df['lon'],
        lat = df['lat'],
        text = df['text'],
        mode = 'markers',
        marker = dict(
            size = 8,
            opacity = 0.8,
            reversescale = True,
            autocolorscale = False,
            symbol = 'square',
            line = dict(
                width=1,
                color='rgba(102, 102, 102)'
            ),
            colorscale = 'Blues',
            cmin = 0,
            color = df['IEX'],
            cmax = df['IEX'].max(),
            colorbar_title="escolas"
        )))

fig.update_layout(
        title = 'Escolas',
        geo_scope='south america',
        #geo = dict(
            #scope='south america',
            #projection_type='albers usa',
            #showland = True,
            #landcolor = "rgb(250, 250, 250)",
            #subunitcolor = "rgb(217, 217, 217)",
            #countrycolor = "rgb(217, 217, 217)",
            #countrywidth = 0.5,
            #subunitwidth = 0.5
        #),
    )


fig.update_layout(
        title = 'Most trafficked US airports<br>(Hover for airport names)',
        geo_scope='usa',
    )



fig.show()
