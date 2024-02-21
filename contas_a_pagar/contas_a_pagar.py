import modulos.salvar, modulos.tratamento_json


if __name__ == '__main__':
    modulos.tratamento_json.transforma_dataframe()
    modulos.salvar.salva_excel()
    
    print('Concluido!!')