from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def formulario():
    return render_template('formulario.html')

@app.route('/cartao', methods=['POST'])
def cartao():
    nome = request.form['nome']
    cargo = request.form['cargo']
    email = request.form['email']
    telefone = request.form['telefone']

    return render_template(
        'cartao.html',
        nome=nome,
        cargo=cargo,
        email=email,
        telefone=telefone
    )

@app.route('/novo')
def novo():
    return redirect(url_for('formulario'))

if __name__ == '__main__':
    app.run(debug=True)