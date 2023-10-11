import pandas as pd
import streamlit as st

st.set_page_config(layout="wide")

teste = pd.read_csv("Teste.csv", sep=',')
teste = teste.set_index('ID')
teste.drop(columns='Status',inplace=True)

#print(teste.head())

tipo = st.sidebar.selectbox("Tipo", teste["Tipo"].unique(), key="1")
cantor = st.sidebar.selectbox("Cantor", teste["Cantor"].unique(), key="2")

dados = teste[teste["Tipo"] == tipo]
dados2 = dados[dados["Cantor"] == cantor]

st.dataframe(dados2)