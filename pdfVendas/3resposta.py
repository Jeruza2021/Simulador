import pandas as pd

Pesquisa_Populacao_Geral = pd.read_excel('Pesquisa_Populacao_Geral.xlsx')

conhecimento_lojas = Pesquisa_Populacao_Geral[Pesquisa_Populacao_Geral['Conhece a conessionária?']== 'Sim'].groupby('Cidade').size().sort_values(ascending=False)


print(conhecimento_lojas)