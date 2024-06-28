from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# Conexão atabase
conexao = mysql.connector.connect(
    host="localhost",
    user="estoque_roupas_how_vi",
    passwd="12345",
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
        idRoupa = cursor.execute(inserir_roupas, (roupa_nome, roupa_tamanho, roupa_preco))
        
        select_id_roupa = "SELECT LAST_INSERT_ID();"
        cursor.execute(select_id_roupa)
        idRoupa = cursor.fetchone()[0]
        conexao.commit()

        inserir_fornecedor = "INSERT INTO fornecedor(nome, endereco, telefone) VALUES (%s, %s, %s)"
        idFornecedor = cursor.execute(inserir_fornecedor, (fornecedor_nome, fornecedor_endereco, fornecedor_fone))
    
        select_id_fornecedor= "SELECT LAST_INSERT_ID();"
        cursor.execute(select_id_fornecedor)
        idFornecedor = cursor.fetchone()[0]
        conexao.commit()

        inserir_roupas_fornecedor = "INSERT INTO roupas_fornecedor(id_roupas, id_fornecedor) VALUES (%s, %s)"
        cursor.execute(inserir_roupas_fornecedor, (idRoupa, idFornecedor))
        conexao.commit()

        conexao.close()

        # display mensagem de sucesso
        return "Dados inseridos com sucesso!"

    return render_template('index.html')



@app.route('/consulta', methods=['GET', 'POST'])
def consulta():
    cursor.execute('''SELECT * FROM 
                `estoque_roupas_how_vi`.roupas r
            JOIN 
                `estoque_roupas_how_vi`.roupas_fornecedor rf ON r.id_roupas = rf.id_roupas
            JOIN 
                `estoque_roupas_how_vi`.fornecedor f ON rf.id_fornecedor = f.id_fornecedor''')
    
    
    listar_dados = cursor.fetchall()

    
    return render_template('consulta.html',
                           listar_dados=listar_dados,
                            titulo="Lista das roupas e fornecedores"
                            )
    cursor.close()
    
if __name__ == '__main__':
    app.run(debug=True)