from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calcular_idade', methods=['POST'])
def calcular_idade():
    ano = int(request.form['ano'])

    idade = 2025 - ano

    return render_template('index.html', idade=idade)

if __name__ == '__main__':
    app.run(debug=True)