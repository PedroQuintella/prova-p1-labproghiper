from flask import render_template, request
from application import app
from application.model.dao.noticia_dao import NoticiaDAO
from application.model.entity.noticia import Noticia
from application.model.dao.estado_dao import EstadoDAO
from application.model.entity.estado import Estado
from application.model.entity.comentarios import Comentarios
from application import listaNoticias
from application import listaEstados

@app.route("/noticia/<noticia_id>", methods=['GET'])
def noticia(noticia_id):
    noticia_dao = NoticiaDAO()
    noticia = noticia_dao.buscar_por_id(noticia_id)
    noticia_dao.armazenar_visualizacao(noticia)
    lista_comentarios = noticia.get_comentarios()
    return render_template("noticia.html", noticia = noticia, listaEstados = listaEstados, lista_comentarios = lista_comentarios)


@app.route('/noticia/<noticia_id>/comentarios', methods=['POST'])
def comentar(noticia_id):
    noticia_dao = NoticiaDAO()
    noticia = noticia_dao.buscar_por_id(noticia_id)
    autor = request.values.get('nome') 
    texto = request.values.get('texto')
    comentario = Comentarios(autor, texto)
    noticia.set_comentario(comentario)
    return render_template('comentarios.html', noticia = noticia), 201

@app.route("/noticia/<noticia_id>/curtir", methods=['POST'])
def curtir(noticia_id):
    noticia_dao = NoticiaDAO()
    noticia = noticia_dao.buscar_por_id(noticia_id)
    noticia_dao.armazenar_curtida(noticia)
    return render_template("curtidas.html", noticia = noticia), 200

@app.route('/noticia/<noticia_id>/comentarios', methods=['DELETE'])
def apagar(noticia_id):
    noticia_dao = NoticiaDAO()
    noticia = noticia_dao.buscar_por_id(noticia_id)
    noticia_dao.apagar_comentario(noticia)
    return render_template('comentarios.html', noticia = noticia), 200

