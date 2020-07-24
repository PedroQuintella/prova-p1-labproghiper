from flask import render_template, request
from application import app
from application.model.entity.estado import Estado
from application.model.dao.estado_dao import EstadoDAO
from application.model.entity.noticia import Noticia
from application.model.dao.noticia_dao import NoticiaDAO
from application import listaEstados
from application import listaNoticias


@app.route('/')
def home():
    estado_dao = EstadoDAO()
    for estado in listaEstados:
        estado_id = estado.get_id()
    estado = estado_dao.buscar_por_id(estado_id)  
    listaNoticiasRecentes = [listaNoticias[len(listaNoticias)-1], listaNoticias[len(listaNoticias)-2], listaNoticias[len(listaNoticias)-3], listaNoticias[len(listaNoticias)-4]]
    maisCurtidas = sorted(listaNoticias, key=Noticia.get_qtdCurtidas, reverse=True)
    listaNoticiasMaisCurtidas = [maisCurtidas[0], maisCurtidas[1], maisCurtidas[2], maisCurtidas[3]]
    return render_template("index.html", listaEstados = listaEstados, listaNoticiasRecentes = listaNoticiasRecentes, listaNoticiasMaisCurtidas = listaNoticiasMaisCurtidas, estado = estado)

