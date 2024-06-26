import mysql.connector
import requests

conexao = mysql.connector.connect(
    host="localhost",
    user="estoque_roupas_how_vi",
    passwd="estoque_roupas_how_vi",
    database="estoque_roupas_how_vi"
)

cursor= conexao.cursor()

# CREATE
# nome_produto = "chocolate"
# valor = 15
# comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor})'
# cursor.execute(comando)
# conexao.commit() # edita o banco de dados


inserir_roupas = f'INSERT INTO roupas(nome, tamanho, preco) VALUES ("{roupa_nome}", {roupa_tamanho}, {roupa_preco})'
inserir_fornecedor = f'INSERT INTO fornecedor(nome, endereco, telefone) VALUES ("{fornecedor_nome}", {fornecedor_endereco}, {fornecedor_fone})'
# Inserir na tabela roupas
cursor.execute(inserir_roupas)
conexao.commit()

# Inserir na tabela fornecedor
cursor.execute(inserir_fornecedor)
conexao.commit()


# READ
# comando = f'SELECT * FROM vendas'
# cursor.execute(comando)
# resultado = cursor.fetchall() # ler o banco de dados
# print(resultado)

cursor.close()
conexao.close()
