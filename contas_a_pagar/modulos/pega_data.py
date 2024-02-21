import os
import pathlib

def data_inicio(): 
    caminho = pathlib.Path("bases")
    lista_arquivo = os.listdir(caminho)

    lista_datas = []

    for arquivo in lista_arquivo:
        data = os.path.getmtime(f'{caminho}/{arquivo}')
        lista_datas.append((data, arquivo))

    lista_datas.sort(reverse=True)
    arquivo_recente = lista_datas[0]
    ult_data = arquivo_recente[1]
    data_inicio = ult_data[11:21]
    return data_inicio