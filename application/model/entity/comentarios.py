class Comentarios:

    def __init__(self, autor, texto):
        self._autor = autor
        self._texto = texto

    def get_autor(self):
        return self._autor
    
    def get_texto(self):
        return self._texto

    