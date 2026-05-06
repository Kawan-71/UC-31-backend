from flask import Flask, render_template

app = Flask(__name__)

@app.route('/index')
def index():
    return 'Oláaaaaa'

@app.route('/arearestrita/<int:id>')
def arearestrita(id):
    if id == 1: 
        return 'cadeado fechado'
    elif id == 2: 
        return 'cadeado aberto'
    else:
        return 'ERRO'
    
@app.route('/operacao/<tipo>/<int:op1>/<int:op2>')
def operacao(tipo, op1, op2):
    if tipo == 'sum':
        resultado = op1 + op2
    elif tipo == 'sub':
        resultado = op1 - op2
    elif tipo == 'mult':
        resultado = op1 * op2
    elif tipo == 'div':
        if op2 == 0:
            return 'ERRO: divisão por 0'
        resultado = op1/op2
    else:
        return 'ERRO'
    
    return f'Resultado: {resultado}'

if __name__ == '__main__':
    app.run(debug=True)