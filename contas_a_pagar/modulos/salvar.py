import pathlib
import pandas as pd
import os


data_arquivo_folder = pathlib.Path("bases")

df =[]

def salva_excel():
    for file in os.listdir(data_arquivo_folder):
        if file.endswith('.json'):
            print('loading file, {0}....'.format(file))
            df.append(pd.read_json(os.path.join(data_arquivo_folder, file)))

    print(len(df))

    df_principal = pd.concat(df, axis=0)
    df_principal = df_principal.drop_duplicates(subset='id', keep = 'last')
    df_principal.to_excel('contas_a_pagar.xlsx', index=False, sheet_name='Dados')
    
