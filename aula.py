import streamlit as st;
import pandas as pd;

st.title("Aula CD")

st.text("Apartamentos RJ")
rioAptos = pd.read_csv('https://raw.githubusercontent.com/mvinoba/notebooks-for-binder/master/dados.csv')
base = rioAptos.copy()

# Escolha de bairro
bairros = base["bairro"].unique()
bairro = st.selectbox(label="Bairrox do Rio", options = bairros)

valores = st.slider("Valor", 0, 2000, (5, 15))
st.write(valores)

# Escolha das colunas
indices = base["bairro"] == bairro
aptos_bairro = base[indices]
#st.dataframe(base[base["bairro"] == bairro])
qtde_aptos = aptos_bairro.shape[0]
st.text(f"Total: {qtde_aptos} apartamentos encontrados")

colunas = aptos_bairro.columns
colunas_selecionadas = st.multiselect(label="Variáveis" , options = colunas)

st.dataframe(aptos_bairro[colunas_selecionadas])
st.dataframe(aptos_bairro)


