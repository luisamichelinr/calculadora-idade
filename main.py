from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calcular_idade', methods=['POST'])
def calcular_idade():
    try:
        ano = int(request.form['ano'])
        ano_atual = datetime.now().year
        idade = ano_atual - ano
        return render_template('index.html', idade=idade)
    except Exception as e:
        idade = f"Ocorreu um erro inesperado {e}"
        return render_template('index.html', idade = idade)

if __name__ == '__main__':
    app.run(debug=True)
