import numpy as np
from sklearn.preprocessing import StandardScaler

conjunt = np.array([[10, 0], [15, 2], [20, 5], [25, 10], [30, 15]])

scaler = StandardScaler()

Escala_de_datos = scaler.fit_transform(conjunt)

print(Escala_de_datos)
