from database import connect_to_database, execute_query
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/consulta')
def consulta():
    return render_template('consulta.html')

if __name__ == '__main__':
    app.run(debug=True)