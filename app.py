from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/pesquisa", methods=["POST"])
def pesquisa():
    termo = request.form["termo"]
    resultado = f"Você pesquisou por: {termo}. (Aqui aparecerá o conteúdo relacionado)"
    return render_template("resultado.html", resultado=resultado)