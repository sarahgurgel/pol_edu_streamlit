import streamlit as st
import pandas as pd
import numpy as np

st.markdown(''' # OTIMIZANDO A POLÍTICA EDUCACIONAL
    #### Uso de algoritmos de Machine Learning para categorização das escolas conforme previsão do "Índice de Execução - IEx" dos recursos orçamentários do Programa Dinheiro Direto na Escola - PDDE do Ministério da Educação - MEC, visando auxiliar na seleção de escolas para receber Assistência Técnica de forma antecipada, qualificada e territorializada.
    #\n
    # O Programa Dinheiro Direto na Escola - PDDE:
    ###### Site oficial do Programa: https://www.gov.br/fnde/pt-br/acesso-a-informacao/acoes-e-programas/programas/pdde
    #\n
    ## Finalidade:
    #### O PDDE possui caráter suplementar e consiste na destinação anual de recursos financeiros repassados às entidades participantes, cujas finalidades consistem em contribuir para:
    ##### ▪ o provimento das necessidades prioritárias dos estabelecimentos educacionais beneficiários que concorram para a garantia de seu funcionamento;
    ##### ▪ a promoção de melhorias em sua infraestrutura física e pedagógica; e
    ##### ▪ o incentivo da autogestão escolar e do exercício da cidadania, com a participação da comunidade no controle social.
    #\n
    ## Princípios:
    ##### ▪ Participação social
    ##### ▪ Autonomia escolar
    ##### ▪ Simplificação de processos
    #\n
    ## Público:
    ##### ▪ Mais de 130 mil escolas de educação pública básica, recenseada pelo INEP
    ##### ▪ Mais de 33 milhões de alunos alcançados
    ##### ▪ 30 anos de programa
    #\n
    ## Recursos Orçamentários: ''')

col1, col2 = st.columns(2)
col1.metric("Orçamento anual", "R$ 2,2 bilhões")
col2.metric("Saldo acumulado", "R$ 1.1 bilhão")

st.markdown(''' #\n
    ## Índice de Execução -IEx dos Recursos Orçamentários:
    ##### ▪ Fórmula: ''')
st.markdown('''```''')
st.latex(r'''IEx = \left(\frac{VTE}{VTD}\right)''')
st.markdown('''```''')
st.markdown('''  ##### ▪ Onde:
    ###### - IEx é o Indicador de Execução dos recursos orçamentários;
    ###### - VTE é o Valor Total Executado, calculado pela diferença entre o Valor Total Disponível no período e o saldo do último mês do período;
    ###### - VTD é o Valor Total Repassado durante o período, somado ao saldo disponível no mês anterior do período.
    # ''')

from PIL import Image
image = Image.open('raw_data/mapa_iex.png')

st.image(image, caption='Sunrise by the mountains')
