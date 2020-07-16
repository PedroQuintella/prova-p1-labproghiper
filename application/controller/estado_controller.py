from flask import render_template
from application import app


@app.route("/estado")
def estado():
    return render_template("estado.html")