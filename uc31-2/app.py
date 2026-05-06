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
    