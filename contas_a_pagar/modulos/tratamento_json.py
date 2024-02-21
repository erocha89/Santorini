import pandas as pd
from .request import starDate, endDate, conexao


def transforma_dataframe():
    response = conexao()
    nro = 0
    lista = []

    for n in response.get(['results'][nro]):
        lista.append(response['results'][nro])

        nro +=1

    
    dataframe = pd.DataFrame(lista)
    nome_json = f'bases/{starDate}_{endDate}.json'
    dataframe.to_json(nome_json)

    
    return dataframe

if __name__=='__main__':
    transforma_dataframe()

