from application.model.entity.estado import Estado
from application import listaEstados


class EstadoDAO:

    def __init__(self):
        self._listaEstados = listaEstados 

    def listar_estados(self):
        return self._listaEstados

    def listar_noticias(self, estado):
        return estado.get_listaNoticias()

    def buscar_por_id(self, id):
        for estado in range(0, len(self._listaEstados)):
            if self._listaEstados[estado].get_id() == int(id):
                return self._listaEstados[estado]
        return None

        

    