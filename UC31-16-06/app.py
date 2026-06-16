from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)


app.secret_key = "minha_chave_secreta"


USUARIO_CORRETO = "admin"
SENHA_CORRETA = "1234"


@app.route("/")
def inicio():
    return render_template("index.html")



@app.route("/login", methods=["GET", "POST"])
def login():
    mensagem = ""

    if request.method == "POST":
        usuario = request.form["usuario"]
        senha = request.form["senha"]

    
        if usuario == USUARIO_CORRETO and senha == SENHA_CORRETA:
            session["usuario"] = usuario
            return redirect(url_for("dashboard"))
        else:
            mensagem = "Usuário ou senha incorretos!"

    return render_template("login.html", mensagem=mensagem)



@app.route("/dashboard")
def dashboard():
   
    if "usuario" not in session:
        return redirect(url_for("login"))

    return render_template("dashboard.html", usuario=session["usuario"])



@app.route("/logout")
def logout():
    session.pop("usuario", None)
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)