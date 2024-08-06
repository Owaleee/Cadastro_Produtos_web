# Bibliotecas importadas
import streamlit as st
import pandas as pd
import os
import time

def carregar_dados():
    try:
        return pd.read_csv("Produtos.csv", header=None, names=["Nome", "Valor", "Quantidade", "Estado"])
    except FileNotFoundError:
        return pd.DataFrame(columns=["Nome", "Valor", "Quantidade", "Estado"])
    
def salvar_dados(nome, valor, quantdade, estado):
    with open("Produtos.csv", "a", encoding="utf8") as arquivo:
        arquivo.write(f"{nome}, {valor}, {quantdade}, {estado}\n")

def calcular_valor_total(df):
    return(df["Valor"] * df["Quantidade"]).sum()

def limpar_cadastro():
    if os.path.exists("Produtos.csv"):
        os.remove("Produtos.csv")
        return True
    return False
st.title("Cadastro de Produtos")

nome_produto = st.text_input("Nome do Produto")
valor_produto = st.number_input("Valor do Produto (R$)", min_value=0.01, step=0.01)
qtd_produto = st.number_input("Quantidade", step=1, value=1, min_value=1, format="%d")
estd_conservacao = st.selectbox("Estado de Conservação", ["Novo", "Usado"])

if st.button("Cadastrar Produto"):
    if not nome_produto:
        st.error("O nome do produto é obrigatório.")
    elif valor_produto <= 0:
        st.error("O valor do produto deve ser maior que 0.")
    else:
        salvar_dados(nome_produto, valor_produto, qtd_produto, estd_conservacao)
        st.success("Produto cadastrado com sucesso!")

df = carregar_dados()

total_valor = calcular_valor_total(df)
st.markdown(f'Soma total dos valores dos produtos <span style="color:green">R${total_valor:.2F}</span>', unsafe_allow_html=True)

if not df.empty:
    st.write("Produtos cadastrados:")
    st.dataframe(df)
    st.write("-------")
else:
    st.write("Nenhum produto cadastrado ainda.")
    st.write("-------")

if st.button("Limpar Cadastro"):
    if limpar_cadastro():
        st.warning("Cadastro limpo com sucesso. Atualizando...")
        time.sleep(1)
        st.rerun()
    else:
        st.warning("Nunhum cadastro encontrado para limpar.")