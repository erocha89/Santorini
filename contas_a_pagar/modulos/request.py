from datetime import date, timedelta
import requests
import json
from modulos.pega_data import data_inicio

#informações da requisição da api
starDate = data_inicio()
endDate = date.today()
limit = "100"

# Variaveis de acesso
username = '############'
token = '#################'

# URL 
url = f"https://api.sienge.com.br/santorinienergy/public/api/v1/bills?startDate={starDate}&endDate={endDate}&limit={limit}"

#Validação do site
basic = auth = (username, token)

def conexao():
#Retorno do site
    response = requests.get(url, auth=basic)
    df = json.loads(response.content)
    return df



    
