from flask import Flask
import os
from application.model.entity.estado import Estado
from application.model.entity.noticia import Noticia


app = Flask(__name__, static_folder=os.path.abspath("application/view/static"), template_folder=os.path.abspath("application/view/templates"))

noticia1 = Noticia(1, "Minas tem 322 presos contaminados pela Covid-19 e duas mortes.", "Desde o início da pandemia, 322 presos do estado foram diagnosticados com Covid-19, segundo o Governo de Minas. Dois morreram. O número de agentes penitenciários que também foram contaminados pelo vírus e foram afastados não é informado, por “motivo de segurança”, segundo a Secretaria de Estado de Justiça e Segurança Pública (Sejusp).", "img/noticias/minas-tem-322-presos-com-Covid-19.jpg", "videos/minas-tem-322-presos-com-Covid-19.mp4", "Minas Gerais", "13/07/2020")
noticia2 = Noticia(2, "Coronavírus: 90% dos municípios de MG não possuem leitos de UTI.", "O número de infectados pelo novo coronavírus continua a subir, fazendo com que o sistema de saúde de alguns estados esteja próximo do colapso. Minas Gerais, mesmo com uma baixa taxa de mortalidade até agora, tem o maior número de municípios do país e 90% deles não possuem leitos de UTI.", "img/noticias/coronavirus-municipios-de-mg-sem-leitos-uti.jpg", "videos/coronavirus-municipios-de-mg-sem-leitos-uti.mp4", "Minas Gerais", "14/07/2020")
noticia3 = Noticia(3, "Covid-19: Rio de Janeiro começa a multar banhistas que permanecerem na areia.", "O calçadão e as praias da Zona Sul do Rio de Janeiro registraram movimentação neste sábado, mesmo sob ameaça de multa por conta da covid-19.", "img/noticias/rio-de-janeiro-comeca-a-multar-banhista.jpg", "videos/covid-19-rio-de-janeiro-comeca-a-multar-banhistas.mp4", "Rio de Janeiro", "15/07/2020")
noticia4 = Noticia(4, "Coronavírus em SP: Mortes batem recorde semanal no estado.", "O estado de São Paulo registrou o maior número de mortes por Covid-19 em uma semana desde o início da pandemia do coronavírus: 1.945. Com isso, o estado chegou a 19.647 óbitos. Com 270 mortes registradas neste sábado (18), os últimos 7 dias bateram o recorde anterior de 1.913 mortes da semana que fechou no dia 20 de junho.", "img/noticias/coronavirus-sp-recorde-semanal-de-morte.jpg", "videos/coronavirus-sp-recorde-semanal-de-mortes.mp4", "São Paulo", "16/07/2020")
noticia5 = Noticia(5, "Rio cria unidade hospitalar para tratamento de pacientes pós-Coronavírus.", "Um hospital no Rio de Janeiro criou uma unidade para tratar os pacientes que se recuperaram do novo coronavírus, mas ainda precisam de um tempo de reabilitação e cuidados especiais. O local é destinado às pessoas carentes de estrutura para continuar o tratamento em casa.", "img/noticias/hospital-no-rio-para-pos-coronavirus-thumbnail.jpg", "videos/hospital-no-rio-para-pos-coronavirus.mp4", "Rio de Janeiro", "17/07/2020")
noticia6 = Noticia(6, "Covid-19: Governo de São Paulo dá início aos testes da vacina chinesa hoje.", "O Governador João Doria anunciou nesta segunda-feira (20/07) o início dos testes da CoronaVac, vacina contra o coronavírus, no Brasil. O Instituto Butantan receberá as doses de imunizantes e placebos que serão utilizados na realização da terceira fase de ensaios clínicos para desenvolvimento da vacina, em parceria com a farmacêutica Sinovac Life Science. Sobre essa novidade, o BandNews TV conversou com o infectologista, Dr. Jean Gorinchetyn.", "img/noticias/sp-comeca-a-testar-vacina-chinesa-thumbnail.jpg", "videos/covid-19-sp-comeca-a-testar-vacina-chinesa.mp4", "São Paulo", "18/07/2020")
listaNoticias = [noticia1, noticia2, noticia3, noticia4, noticia5, noticia6]

estado1 = Estado(1,"Rio de Janeiro", "RJ", 'img/estados/bandeira_riodejaneiro.png', [noticia3, noticia5])
estado2 = Estado(2, "São Paulo", "SP", 'img/estados/bandeira_saopaulo.png', [noticia4, noticia6])
estado3 = Estado(3, "Minas Gerais", "MG", 'img/estados/bandeira_minasgerais.png', [noticia1, noticia2])
listaEstados = [estado1, estado2, estado3]


from application.controller import index_controller
from application.controller import estado_controller
from application.controller import noticia_controller


