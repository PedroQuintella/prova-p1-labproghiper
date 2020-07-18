from application.model.entity.noticia import Noticia
from application import listaNoticias

class NoticiaDAO:

    def __init__(self):
        self._listaNoticias = listaNoticias 
    
    def listar_noticias(self):
        return self._listaNoticias 

    def buscar_por_id(self):
        for noticia in range(0, len(self._listaNoticias)):
            if self._listaNoticias[noticia].get_id() == int(id):
                return self._listaNoticias[noticia]
        return None

    def apagar_comentario(self, noticia):
        noticia.get_comentarios().pop(0)

    def armazenar_visualizacao(self, noticia):
        noticia.set_visualizacao()
    
    def armazenar_curtida(self, noticia):
        noticia.set_curtida()

    


    
