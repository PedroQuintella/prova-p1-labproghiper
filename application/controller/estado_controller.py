from flask import render_template, request
from application import app
from application.model.entity.estado import Estado
from application.model.dao.estado_dao import EstadoDAO


@app.route("/estado/<estado_id>")
def estado(estado_id):
    estado_dao = EstadoDAO()
    estado = estado_dao.buscar_por_id(estado_id)
    return render_template("estado.html", estado = estado)