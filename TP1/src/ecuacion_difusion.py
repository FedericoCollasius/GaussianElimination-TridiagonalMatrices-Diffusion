import matplotlib.pyplot as plt
import numpy as np
import copy

# Ejercicio 5
def precomputo_eliminacion_gaussiana(a, b, c):
  n = len(b)

  mult_upper = []
  mult_lower = []

  # Itera columnas, triangula superiormente
  for i in range(0, n - 1): 
    if (b[i] == 0):
      return -1

    mji = a[i] / b[i]

    a[i] = a[i] - mji * b[i]
    b[i + 1] = b[i + 1] - mji * c[i]

    mult_upper.append(mji)

  # Itera columnas, triangula inferiormente
  for i in reversed(range(1, n)): 
    if (b[i] == 0):
      return -1

    mji = c[i - 1] / b[i]
    c[i - 1] = c[i - 1] - mji * b[i]

    mult_lower.append(mji)

  return [mult_upper, mult_lower, b]

def calculo_solucion(precomputo, cte):
  n = len(cte)

  copy_precomputo = copy.deepcopy(precomputo)

  mult_upper = copy_precomputo[0]
  mult_lower = copy_precomputo[1]
  b = copy_precomputo[2]

  # Construye las soluciones a partir de las operaciones guardadas
  x = copy.deepcopy(np.array(cte, dtype=float))

  for i in range(1, n):
    x[i] = x[i] - x[i - 1] * mult_upper[i - 1]

  for i in reversed(range(0, n - 1)):
    x[i] -= x[i + 1] * mult_lower[n - 2 - i]

  for i in range(0, n):
    x[i] *= 1 / b[i]

  return x 

def operador_difusion(n, alfa):
  a = np.full(n - 1, -1, dtype=float)
  b = np.full(n, 2 * alfa + 1, dtype=float)
  c = np.full(n - 1, -1, dtype=float)

  return [a, b, c]

def difusion(ci, k):
  n = len(ci)
  pasos_difusion = [ci]

  precomputo = precomputo_eliminacion_gaussiana(*operador_difusion(n, 1))

  for i in range(0, k):
    resultado = calculo_solucion(precomputo, pasos_difusion[i])
    pasos_difusion.append(resultado)

  return pasos_difusion


if __name__ == '__main__':
#EXPERIMENTACION
  n = 101
  r = 20
  k = 101

  ci = np.array([1 if (n // 2 - r < i) and (i < n // 2 + r) else 0 for i in range(0, n)])

  resultado_difusion = difusion(ci, k)

  plt.pcolor(np.transpose(resultado_difusion), cmap='RdBu', vmin=0, vmax=1)
  plt.xlabel("Paso k-esimo")
  plt.ylabel("Distribucion calor")

  plt.show()
