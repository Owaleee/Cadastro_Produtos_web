# Bibliotecas importadas
import streamlit as st
import pandas as pd
import os
import time

# Título da aplicação
st.title("Cadastro de Produtos")

# Campos de entrada para os dados do produto
nome_produto = st.text_input("Nome do Produto")
valor_produto = st.number_input("Valor do Produto (R$)")
qtd_produto = st.number_input("Quantidade", step=1, value=1, min_value=1, format="%d")
estd_conservacao = st.selectbox("Estado de Conservação", ["Novo", "Usado"])

# Botão para cadastrar o produto
cadastrar = st.button("Cadastrar Produto")

# Verificação e cadastro do produto
if cadastrar:
    if valor_produto <= 0:
        st.error("O valor do produto deve ser maior que 0.")
    else:
        with open("Produtos.csv", "a", encoding="utf8") as arquivo:
            arquivo.write(f"{nome_produto},{valor_produto},{qtd_produto},{estd_conservacao}\n")
            st.success("Produto cadastrado com sucesso!")

# Leitura e processamento do arquivo CSV
try:
    df = pd.read_csv("Produtos.csv", header=None, names=["Nome", "Valor", "Quantidade", "Estado"])
    # Cálculo do valor total dos produtos
    total_valor = (df["Valor"] * df["Quantidade"]).sum()
    st.markdown(f'Soma total dos valores dos produtos: <span style="color:green">R$ {total_valor}</span>', unsafe_allow_html=True)
except FileNotFoundError:
    # Criação de um DataFrame vazio se o arquivo não existir
    df = pd.DataFrame(columns=["Nome", "Valor", "Quantidade", "Estado"])

# Exibição dos produtos cadastrados
if not df.empty:
    st.write("Produtos cadastrados:")
    st.dataframe(df)
    st.write("-------")
else:
    st.write("Nenhum produto cadastrado ainda.")
    st.write("-------")

# Botão para limpar o cadastro
limpar = st.button("Limpar Cadastro")

# Lógica para limpar o arquivo CSV e atualizar a página
if limpar:
    if os.path.exists("Produtos.csv"):
        os.remove("Produtos.csv")
        # Mensagem de atualização e timer
        sucesso_placeholder = st.empty()
        sucesso_placeholder.warning("Atualizando Cadastro...")
        time.sleep(1)
        st.rerun()
    else:
        st.warning("Nenhum cadastro encontrado para limpar.")
