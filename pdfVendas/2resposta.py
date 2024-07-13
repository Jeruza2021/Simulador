import pandas as pd
import matplotlib.pyplot as plt

vendas_2023 = pd.read_excel('Vendas_de_2023.xlsx')

colunas_numericas = vendas_2023.select_dtypes(include=['number']).columns
media_vendas_2023 = vendas_2023[colunas_numericas].mean(axis=1)

vendas_2023['Media'] = media_vendas_2023

# fazer o ranking

ranking_vendas = vendas_2023.sort_values(by='Media', ascending=False)


# criar o grafico

plt.figure(figsize=(10, 6))
plt.bar(ranking_vendas['Cidade'], ranking_vendas['Media'])
plt.xlabel('Cidade')
plt.ylabel('Media de Vendas')
plt.title('Ranking das Lojas por Média de Vendas em 2023')
plt.xticks(rotation=45)
plt.show()