import pandas as pd

vendas_2023 = pd.read_excel('Vendas_de_2023.xlsx')


colunas_numericas = vendas_2023.select_dtypes(include=['number']).columns
media_vendas_2023 = vendas_2023[colunas_numericas].mean(axis=1)

vendas_2023['Media'] = media_vendas_2023

quartil_inferior = media_vendas_2023.quantile(0.25)

lojas_piores_medias = vendas_2023.loc[media_vendas_2023 <= quartil_inferior, 'Cidade']

variacao_vendas = vendas_2023.loc[media_vendas_2023 <= quartil_inferior, colunas_numericas].std(axis=1)

loja_mais_inconstante = vendas_2023.loc[variacao_vendas.idxmax(), 'Cidade']

print("Loja mais inconstante", loja_mais_inconstante)

print("Maior Variação nas vendas", variacao_vendas.max())