import matplotlib.pyplot as plt
import numpy as np

categorias = ["Inicial", "+100", "+100", "+100", "+100"]

base = np.array([700, 800, 900, 1000, 1100])
complemento = np.array([300, 200, 100, 0, 0])
salario_sin_complemento = np.array([1000, 1100, 1200, 1300, 1400])

x = np.arange(len(categorias))   # Posiciones en el eje X
width = 0.35                     # Ancho de las barras

plt.bar(x - width/2, base, width, label="Base")
plt.bar(x - width/2, complemento, width,
        bottom=base,  # que se base en la anterior, que se ponga encima
        label="Complemento")

# barra de la serie Complemento. x + width/2 para separarse del otro grupo
plt.bar(x + width/2, salario_sin_complemento, width, label="Salario sin Complemento")

# Etiquetar y mostrar
plt.xticks(x, categorias)
plt.ylabel("Importe")
plt.title("Comparación: Salario con Complemento vs Salario sin Complemento")
plt.legend()

plt.show()
