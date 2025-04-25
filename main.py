from flask import Flask, render_template, request
from datetime import datetime
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/calcular_idade', methods=['POST'])
def calcular_idade():
    try:
        ano_nascimento = int(request.form['ano_nascimento'])
        ano_atual = datetime.now().year
        nascimento = int(ano_atual-ano_nascimento)


        return render_template('index.html',nascimento=nascimento)
    except Exception as e:
        nascimento = f'Ocorreu um erro inesperado {e}'
        return render_template('index.html',nascimento=nascimento)


if __name__=='__main__' :
    app.run(debug=True)