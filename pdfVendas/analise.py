import pandas as pd

vendas_2023 = pd.read_excel('Vendas_de_2023.xlsx')
Total_de_vendas = pd.read_excel('Total_de_vendas.xlsx')
Sastifacao_dos_clientes = pd.read_excel('Sastifacao_dos_clientes.xlsx')
Pesquisa_Populacao_Geral = pd.read_excel('Pesquisa_Populacao_Geral.xlsx')

vendas_2023.head(), Total_de_vendas.head(), Sastifacao_dos_clientes.head(), Pesquisa_Populacao_Geral.head()
 
media_de_vendas_2023 = vendas_2023.mean(axis=1)
cidade_maior_media_vendas = vendas_2023.loc[media_de_vendas_2023.idxmax(), 'cidade']
cidade_maior_media_vendas, media_de_vendas_2023.max()
