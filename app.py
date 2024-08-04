import streamlit as st

st.title("Cadastro de Produtos")

nome_produto = st.text_input("Digite o nome do Produto")
valor_produto = st.number_input("Digite o Valor R$")
qtd_produto = st.number_input("Digite a Quantidade", step=1, value=1, min_value=1, format="%d")
estd_conservacao = st.selectbox("Estado de conservação", ["Novo", "Usado"])

cadastrar = st.button("Cadastrar Produto")

if cadastrar:
    with open("Produtos.csv", "a", encoding="utf8") as arquivo:
        arquivo.write(f"{nome_produto},{valor_produto},{qtd_produto},{estd_conservacao} \n")
        st.success("Produto cadastrado com sucesso!")