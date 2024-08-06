# Bibliotecas importadas
import streamlit as st
import pandas as pd
import os
import time

# Função para carregar os dados do arquivo CSV
def carregar_dados():
    try:
        return pd.read_csv("Produtos.csv", header=None, names=["Nome", "Valor", "Quantidade", "Estado"])
    except FileNotFoundError:
        return pd.DataFrame(columns=["Nome", "Valor", "Quantidade", "Estado"])

# Função para salvar os dados no arquivo CSV
def salvar_dados(nome, valor, quantdade, estado):
    with open("Produtos.csv", "a", encoding="utf8") as arquivo:
        arquivo.write(f"{nome}, {valor}, {quantdade}, {estado}\n")

# Função para calcular o valor total dos produtos
def calcular_valor_total(df):
    return (df["Valor"] * df["Quantidade"]).sum()

# Função para limpar o cadastro (remover o arquivo CSV)
def limpar_cadastro():
    if os.path.exists("Produtos.csv"):
        os.remove("Produtos.csv")
        return True
    return False

# Título do aplicativo
st.title("Cadastro de Produtos")

# Criação das colunas para entrada de dados
col1, col2, col3, col4 = st.columns(4)

# Entrada do nome do produto
with col1:
    nome_produto = st.text_input("Nome do Produto")

# Entrada do valor do produto
with col2:
    valor_produto = st.number_input("Valor do Produto (R$)", min_value=0.01, step=0.01)

# Entrada da quantidade do produto
with col3:
    qtd_produto = st.number_input("Quantidade", step=1, value=1, min_value=1, format="%d")

# Seleção do estado de conservação do produto
with col4:  
    estd_conservacao = st.selectbox("Estado de Conservação", ["Novo", "Usado"])

# Botão para cadastrar o produto
if st.button("Cadastrar Produto"):
    if not nome_produto:
        st.error("O nome do produto é obrigatório.")
    elif valor_produto <= 0:
        st.error("O valor do produto deve ser maior que 0.")
    else:
        salvar_dados(nome_produto, valor_produto, qtd_produto, estd_conservacao)
        st.success("Produto cadastrado com sucesso!")

# Carregar os dados do arquivo CSV
df = carregar_dados()

# Calcular o valor total dos produtos cadastrados
total_valor = calcular_valor_total(df)
st.markdown(f'Soma total dos valores dos produtos <span style="color:green">R${total_valor:.2F}</span>', unsafe_allow_html=True)

# Exibir os produtos cadastrados, se houver
if not df.empty:
    st.write("Produtos cadastrados:")
    st.dataframe(df)
    st.write("-------")
else:
    st.write("Nenhum produto cadastrado ainda.")
    st.write("-------")

# Botão para limpar o cadastro
if st.button("Limpar Cadastro"):
    progress_bar = st.progress(0)
    for percent_complete in range(100):
        time.sleep(0.007)
        progress_bar.progress(percent_complete +1)
    if limpar_cadastro():
        st.warning("Cadastro limpo com sucesso. Atualizando...")
        time.sleep(0.20)
        st.rerun()
    else:
        st.warning("Nenhum cadastro encontrado para limpar.")