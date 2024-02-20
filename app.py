import os
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import date
import tabula


app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

db = SQL("sqlite:///users.db")

@app.route("/index")
def index():
    '''
        Aqui eu vou desenvolver uma tabela onde vai aparecer os ativos do usuario.
        Vai ter os nome do ativo, simbolo, preco_medio, valor total investido, preco atual, e se está tendo um ganho ou perda.
    '''
    return render_template("index.html")


@app.route("/notas", methods=["GET", "POST"])
def quote():
    if request.method == "POST":
        return redirect("/")
    else:
        return render_template("notas.html")