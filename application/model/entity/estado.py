class Estado:

    def __init__(self, id, nome, sigla, bandeira, listaNoticias):
        self._id = id
        self._nome = nome
        self._sigla = sigla
        self._bandeira = bandeira
        self._listaNoticias = listaNoticias

    def get_id(self):
        return self._id
    
    def get_nome(self):
        return self._nome
    
    def get_sigla(self):
        return self._sigla
    
    def get_bandeira(self):
        return self._bandeira

    def get_listaNoticias(self):
        return self._listaNoticias
    