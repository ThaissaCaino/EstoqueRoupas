import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="estoque_roupas_how_vi",
    passwd="estoque_roupas_how_vi",
    database="estoque_roupas_how_vi"
)

cursor= conexao.cursor()

#local do CRUD

cursor.close()
conexao.close()