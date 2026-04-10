import streamlit as st;
import pandas as pd;

st.title("Aula CD")

st.text("Apartamentos RJ")
rioAptos = pd.read_csv('https://raw.githubusercontent.com/mvinoba/notebooks-for-binder/master/dados.csv')
base = rioAptos.copy()

# Escolha de bairro
bairros = base["bairro"].unique()

bairro = st.selectbox(
    label="Bairrox do Rio", 
    options = ["Todos"] + list(bairros)
)

if bairro == "Todos":
    aptos_bairro = base
else:
    aptos_bairro = base[base["bairro"] == bairro]

#st.dataframe(base[base["bairro"] == bairro])
qtde_aptos = aptos_bairro.shape[0]
st.text(f"Total: {qtde_aptos} apartamentos encontrados")

# Pegando o valor mínimo e maximo do db
valorMax = base["preco"].max()
valorMin = base["preco"].min()

# Slider de preços
valores = st.slider("Valor", valorMin, valorMax, (valorMin, valorMax))
st.write(valores)

# Escolha das clunas
colunas = aptos_bairro.columns
colunas_selecionadas = st.multiselect(label="Variáveis" , options = colunas)

# definicao do dataframe
apartamentos = aptos_bairro[
    (aptos_bairro["preco"] >= valores[0]) &
    (aptos_bairro["preco"] <= valores[1])
]

st.dataframe(apartamentos[colunas_selecionadas])
