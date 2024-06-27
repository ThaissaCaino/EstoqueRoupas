from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# Conexão atabase
conexao = mysql.connector.connect(
    host="localhost",
    user="estoque_roupas_how_vi",
    passwd="estoque_roupas_how_vi",
    database="estoque_roupas_how_vi"
)
cursor = conexao.cursor()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get data do formulário
        roupa_nome = request.form['roupa_nome']
        roupa_tamanho = request.form['roupa_tamanho']
        roupa_preco = request.form['roupa_preco']
        fornecedor_nome = request.form['fornecedor_nome']
        fornecedor_endereco = request.form['fornecedor_endereco']
        fornecedor_fone = request.form['fornecedor_fone']

        # Inserir no database (using parameterized queries)
        inserir_roupas = "INSERT INTO roupas(nome, tamanho, preco) VALUES (%s, %s, %s)"
        cursor.execute(inserir_roupas, (roupa_nome, roupa_tamanho, roupa_preco))
        conexao.commit()

        inserir_fornecedor = "INSERT INTO fornecedor(nome, endereco, telefone) VALUES (%s, %s, %s)"
        cursor.execute(inserir_fornecedor, (fornecedor_nome, fornecedor_endereco, fornecedor_fone))
        conexao.commit()

        # display mensagem de sucesso
        return "Dados inseridos com sucesso!"

    return render_template('index.html')



@app.route('/consulta')
def consulta():
    return render_template('consulta.html')

if __name__ == '__main__':
    app.run(debug=True)