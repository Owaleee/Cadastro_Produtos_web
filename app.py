import streamlit as st
import pandas as pd
import os
import time

st.title("Cadastro de Produtos")

nome_produto = st.text_input("Digite o nome do Produto")
valor_produto = st.number_input("Digite o Valor R$")
qtd_produto = st.number_input("Digite a Quantidade", step=1, value=1, min_value=1, format="%d")
estd_conservacao = st.selectbox("Estado de conservação", ["Novo", "Usado"])

cadastrar = st.button("Cadastrar Produto")

if cadastrar:
    if valor_produto <= 0:
        st.error("O valor do produto deve ser maior que 0.")
    else:    
        with open("Produtos.csv", "a", encoding="utf8") as arquivo:
            arquivo.write(f"{nome_produto},{valor_produto},{qtd_produto},{estd_conservacao} \n")
            st.success("Produto cadastrado com sucesso!")

try:
    df = pd.read_csv("Produtos.csv", header=None, names=["Nome","Valor", "Quantidade", "Estado"])
    total_valor = (df["Valor"] * df["Quantidade"]).sum()
    st.markdown(f'Soma total dos valores dos produtos: <span style="color:green"> R$ {total_valor}</span>', unsafe_allow_html=True)
except FileNotFoundError:
    df = pd.DataFrame(columns=["Nome","Valor", "Quantidade", "Estado"])


if not df.empty:
    st.write("Produtos cadastrados: ")
    st.dataframe(df)
    st.write("-------")
else:
    st.write("Nenhum produto cadastrado ainda.")
    st.write("-------")

limpar = st.button("Limpar Cadastro")

if limpar:
    if os.path.exists("Produtos.csv"):
        os.remove("Produtos.csv")
        sucess_placeholder = st.empty()
        sucess_placeholder.warning("Atualizando Cadastro...")
        time.sleep(1)
        st.rerun()
    else:
        st.warning("Nenhum cadastro encontrado para limpar.")