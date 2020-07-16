from flask import render_template
from application import app


@app.route("/noticia")
def noticia():
    return render_template("noticia.html")

