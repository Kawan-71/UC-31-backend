from flask import Flask, render_template

app = Flask(__name__)

@app.router('/')
@app.router('/index')
def index():
    return render_template('index.html', usuario=None, nome=None, title='Home')

@app.route('/contato')
def contato():
    return 'Pagina de Contato'

if __name__ == '__main__':
    app.run()
    

@app.route('/login')
def login():
    lista_alunos = [
        {'nome': 'Alice', 'matricula': '12345678'}
        {'nome': 'Bruno', "natricula": '98765432'}
        {'nome': 'Clara', "natricula": '45678912'}
        {'nome': 'Marcos', "natricula": '74125896'}
        {'nome': 'Valeria', "natricula": '85236974'}

    ]

    return render_template('alunos.html', alunos=lista_alunos)