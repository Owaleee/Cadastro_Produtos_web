# Cadastro de Produtos

## O que é isso?

Este é um aplicativo simples que cria uma **interface web** usando Streamlit para ajudar você a cadastrar produtos. As informações são salvas em um arquivo CSV. Com ele, você pode adicionar produtos, ver a lista dos produtos cadastrados e até limpar todos os dados quando precisar.

## O que o aplicativo faz?

- **Cadastrar Produtos**: Adicione o nome, valor, quantidade e estado de conservação dos produtos. Eles são salvos em um arquivo CSV.
- **Mostrar Produtos**: Veja a lista dos produtos que você cadastrou e o valor total de todos os produtos juntos.
- **Limpar Cadastro**: Apague todos os produtos cadastrados e atualize a página.

## O que você precisa?

- Python 3.x
- Streamlit
- Pandas

## Como instalar?

1. Clone o repositório ou baixe o código.
2. Instale as bibliotecas necessárias rodando este comando:

    ```bash
    pip install streamlit pandas
    ```

## Como usar?

1. Vá para o diretório onde o código está salvo.
2. Rode o aplicativo Streamlit com este comando:

    ```bash
    streamlit run nome_do_arquivo.py
    ```

    Troque `nome_do_arquivo.py` pelo nome do arquivo onde o código está.

3. O aplicativo abrirá uma **interface web** no seu navegador.

4. Preencha os campos para cadastrar um produto:
    - **Nome do Produto**: Digite o nome do produto.
    - **Valor do Produto (R$)**: Coloque o valor do produto.
    - **Quantidade**: Defina a quantidade do produto.
    - **Estado de Conservação**: Escolha se o produto é "Novo" ou "Usado".

5. Clique em **Cadastrar Produto** para adicionar o produto.

6. Abaixo do formulário de cadastro, você verá:
    - A lista de produtos cadastrados.
    - O valor total de todos os produtos.

7. Se quiser limpar todos os cadastros, clique em **Limpar Cadastro**. Isso vai excluir o arquivo CSV e atualizar a página.

## Observações

- Verifique se o arquivo `Produtos.csv` pode ser lido e escrito.
- Se o aplicativo não funcionar, verifique se as bibliotecas estão instaladas corretamente.

## Contribuições

Sinta-se à vontade para ajudar com melhorias ou reportar problemas. Para isso, faça um fork do repositório e envie um pull request com suas alterações.

## Licença

Este projeto é de código aberto e pode ser usado conforme a licença [MIT](https://opensource.org/licenses/MIT).