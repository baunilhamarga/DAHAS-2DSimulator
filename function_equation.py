import difflib

import numpy as np

from anastruct import SystemElements

ss = SystemElements()
x, y = ss.plot_values.axial_force(factor=None)

degree = 3  # Por exemplo, um polinômio cúbico
coefficients = np.polyfit(x, y, degree)
polynomial = np.poly1d(coefficients)

# Imprimir a equação do polinômio
def polynomial_equation(coeffs) -> str:
    equation = "y = "
    for i, coef in enumerate(coeffs):
        power = len(coeffs) - i - 1
        if power == 0:
            equation += f"{coef:.2f}"
        elif power == 1:
            equation += f"{coef:.2f}x + "
        else:
            equation += f"{coef:.2f}x^{power} + "
    return equation

equation = polynomial_equation(coefficients)
print("Equação do polinômio ajustado:")
print(equation)
