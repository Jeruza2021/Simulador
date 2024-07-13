import pandas as pd

vendas_2023 = pd.read_excel('Vendas_de_2023.xlsx')


colunas_numericas = vendas_2023.select_dtypes(include=['number']).columns
media_vendas_2023 = vendas_2023[colunas_numericas].mean(axis=1)

vendas_2023['Media'] = media_vendas_2023

cidade_maior_media_vendas = vendas_2023.loc[vendas_2023['Media'].idxmax(), 'Cidade' ]

print(cidade_maior_media_vendas, media_vendas_2023.max())