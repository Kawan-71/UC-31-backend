from flask import Flask

app = Flask(__name__)

@app.route('/ola/<nome>')
def saudacao(nome):
    return f'olá, {nome}! Seja bem vindo(a) ao sistema.'

@app.route('/calculo/<int:n1>/<int:n2>')
def calculo(n1, n2):
    resultado = n1 + n2
    return f'Resultado da soma é: {resultado}'

@app.route('/idade/<nome>/<int:idade>')
def maior_idade(nome, idade):
    if idade >= 18:
        return f'{nome} é maior de idade.'
    else:
        return f'{nome} é menor de idade'
    
@app.route('/produto/<nome>/<float:preco>')
def produto(nome, preco):
    return f'O {nome} custa R${preco}'

@app.route('/repetir/<palavra>/<int:vezes>')
def repetir(palavra, vezes):
    if vezes < 1:
        return "O número de vezes deve ser maior que 0"

    resultado = (palavra + " ") * vezes
    return resultado

if __name__ == '__main__':
    app.run(debug=True)