import pandas as pd
from sklearn.linear_model import LinearRegression



satisfacao_dos_clientes = pd.read_excel('Satisfacao_dos_Clientes.xlsx')

# tratar valores ausentes
satisfacao_dos_clientes = satisfacao_dos_clientes.dropna(subset=['Probabilidade do cliente retornar (0% - 100%)'])


X = satisfacao_dos_clientes['Satisfação dos clientes (1 - 100)'].values.reshape(-1, 1)
y = satisfacao_dos_clientes['Probabilidade do cliente retornar (0% - 100%)'].values

# Treinar modelo
modelo_satisfacao = LinearRegression()
modelo_satisfacao.fit(X, y)

# Exibição do nosso coeficiente
coeficiente = modelo_satisfacao.coef_[0]
intercepto = modelo_satisfacao.intercept_

print(f"Coeficiente: {coeficiente}")
print(f"Intercepto: {intercepto}")