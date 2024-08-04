import streamlit as st
import pandas as pd

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
    st.write("Nenhum produto cadastrado ainda.")


try:
    st.write("Produtos cadastrados: ")
    st.dataframe(df)
except NameError:
    st.write("N/A")