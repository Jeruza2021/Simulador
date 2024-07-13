import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression



Total_de_vendas = pd.read_excel('Total_de_vendas.xlsx')


anos = np.array(range(2004, 2023)).reshape(-1 , 1)
vendas_totais = Total_de_vendas['Total de Vendas'].values[:19]

modelo = LinearRegression()
modelo.fit(anos, vendas_totais)

# previsão de 3 anos 

anos_futuros = np.array(range(2023, 2026)).reshape(-1, 1)
previsoes = modelo.predict(anos_futuros)

print("Anos futuros", anos_futuros.flatten())
print("Previsões de vendas", previsoes)