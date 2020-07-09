class Noticia:

    def __init__(self, id, titulo, textoNoticia, thumbnail, video, dataPublicacao):
        self._id = id
        self._titulo = titulo
        self._textoNoticia = textoNoticia
        self._thumbnail = thumbnail
        self._video = video
        self._dataPublicacao = dataPublicacao
        self._estado = None
        self._qtdVisualizacoes = 0
        self._qtdCurtidas = 0
        self._comentarios = []

    def get_id(self):
        return self._id
    
    def get_titulo(self):
        return self._titulo
    
    def get_textoNoticia(self):
        return self._textoNoticia
    
    def get_thumbnail(self):
        return self._thumbnail
    
    def get_video(self):
        return self._video
    
    def get_dataPublicacao(self):
        return self._dataPublicacao
    
    def set_estado(self, estado):
        self._estado = estado

    def get_estado(self):
        if self._estado == None:
            return "Não informado"
        else:
            return self._estado

    def set_visualizacao(self):
        self._qtdVisualizacoes = self._qtdVisualizacoes + 1
    
    def get_qtdVisualizacoes(self):
        return self._qtdVisualizacoes
    
    def set_curtida(self):
        self._qtdCurtidas = self._qtdCurtidas + 1
    
    def get_qtdCurtidas(self):
        return self._qtdCurtidas
    
    def set_comentario(self, comentario):
        self._comentarios.append(comentario)
    
    def get_comentarios(self):
        return self._comentarios

