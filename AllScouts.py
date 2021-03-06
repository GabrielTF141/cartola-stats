
import urllib2, json, pandas, requests, set_key, database as db
from pandas.io import sql
from time import sleep
url ='https://api.cartolafc.globo.com/atletas/mercado'

key = set_key.get_key()

json_obj = urllib2.urlopen(url)


data = json.load(json_obj)
atl_id=[]
for item in data ['atletas']:
    atl_id.append(item['atleta_id'])



headers = {
    'x-glb-token': str(key),
    'cache-control': "no-cache",
    'postman-token': "f08561bb-27de-6845-0c7b-e8d4cfb5c5b5"
    }
medias = []
ids = []
rodadas = []
preco = []
variacao = []
from random import randint
for i in range(len(atl_id)):
    url2 = "https://api.cartolafc.globo.com/auth/mercado/atleta/"+str(atl_id[i])+"/pontuacao"
    pl = "{\"player\": "+requests.request("GET", url2, headers=headers).text+"}"
    hist =json.loads(pl)
    for dados in hist ['player']:
        ids.append( dados['atleta_id'])
        rodadas.append(dados['rodada_id'])
        medias.append(dados['media'])
        preco.append(dados['preco'])
        variacao.append(dados['variacao'])
    if (i % 5 == 0):
        sleep(6)
lista = {'id': pandas.Series(ids), 'rodada_id': pandas.Series(rodadas), 'media': pandas.Series(medias), 'preco': pandas.Series(preco), 'variacao': pandas.Series(variacao)}
big_df = pandas.DataFrame(lista)



db.df2sqlite(big_df,"cartola_fc","scout_hist")



