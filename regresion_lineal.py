
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# Dataset para entrenar el modelo
data = {        
    'ESTATURA': [121, 123, 108, 118, 111, 109, 114, 103, 110, 115],
    'PESO': [25, 22, 19, 24, 19, 18, 20, 15, 20, 21]
}

df = pd.DataFrame(data)
x = df[['ESTATURA']]  # Variable independiente
y = df[['PESO']]      # Variable dependiente

model = LinearRegression()
model.fit(x, y)

print(f'Coeficiente m: {model.coef_[0][0]}')
print(f'Intercepción b: {model.intercept_[0]}')

estatura_nueva = np.array([[150]])
peso_predecido = model.predict(estatura_nueva)
print(f'el peso predecido es: (estatura_nueva[0][0]): {peso_predecido}')
