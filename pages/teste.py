import streamlit as st
import pandas as pd

df = pd.read_csv('/home/sarah/code/sarahgurgel/projeto_streamlit/raw_data/dadosmapa2.csv', sep=',')
st.map(df)




# mapa das escolas por execução de recurso

#plotar 130 mil escolas no mapa

#classificar por "índice de execução" associado a uma cor no mapa

#colocar container com legenda com as informações da escola

#colocar legenda do mapa com as categorias
