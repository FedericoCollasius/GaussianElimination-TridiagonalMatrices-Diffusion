import numpy as np
import matplotlib.pyplot as plt
import time

# Ejercicio 5
def eliminacion_gaussiana_tridiagonal_ineficiente(a, b, c, d):
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

  # Construye las soluciones a partir de las operaciones guardadas
  x = np.array(d, dtype=float)

  for i in range(1, n):
    x[i] = x[i] - x[i - 1] * mult_upper[i - 1]

  for i in reversed(range(0, n - 1)):
    x[i] -= x[i + 1] * mult_lower[n - 2 - i]

  for i in range(0, n):
    x[i] *= 1 / b[i]

  return x

def eliminacion_gaussiana_tridiagonal_eficiente(a, b, c, d):
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

  # Construye las soluciones a partir de las operaciones guardadas
  sols = []
  for cte in d: 
    x = np.array(cte, dtype=float)

    for i in range(1, n):
      x[i] = x[i] - x[i - 1] * mult_upper[i - 1]

    for i in reversed(range(0, n - 1)):
      x[i] -= x[i + 1] * mult_lower[n - 2 - i]

    for i in range(0, n):
      x[i] *= 1 / b[i]

    sols.append(x)

  return sols


#EXPERIMENTACION
def tiempo_computo_eficiente(n):
  tiempos = []

  for i in range(20):
    t = time.time()

    d = [np.array([2 for j in range(0, n)], dtype=float)]

    a = np.array([1 for j in range(0, n - 1)])
    b = np.array([2 for j in range(0, n)])
    c = np.array([1 for j in range(0, n - 1)])

    eliminacion_gaussiana_tridiagonal_eficiente(a, b, c, d)

    elapsed_time = time.time() - t

    tiempos.append(elapsed_time)

  return [min(tiempos), np.median(tiempos)]


def tiempo_computo_ineficiente(n):
  tiempos = []

  for i in range(20):
    t = time.time()

    d = [np.array([2 for j in range(0, n)], dtype=float) for t in range(15)]

    for cte in d:
      a = np.array([1 for j in range(0, n - 1)])
      b = np.array([2 for j in range(0, n)])
      c = np.array([1 for j in range(0, n - 1)])

      eliminacion_gaussiana_tridiagonal_ineficiente(a, b, c, cte)
    
    elapsed_time = time.time() - t
    tiempos.append(elapsed_time)

  return [min(tiempos), np.median(tiempos)]


tiempo_eficiente_min = []
tiempo_ineficiente_min = []
tiempo_eficiente_median = []
tiempo_ineficiente_median = []

intervalo = [500, 3000, 5000, 10000, 50000]

for i in intervalo:
  a = np.array([1 for j in range(0, i - 1)])
  b = np.array([2 for j in range(0, i)])
  c = np.array([1 for j in range(0, i - 1)])

  d = [np.array([2 for j in range(0, i)], dtype=float) for i in range(15)]

  tiempo_precomputo = tiempo_computo_eficiente(i)
  tiempo_sin_precomputo = tiempo_computo_ineficiente(i)

  tiempo_eficiente_min.append(tiempo_precomputo[0])
  tiempo_eficiente_median.append(tiempo_precomputo[1])
  tiempo_ineficiente_min.append(tiempo_sin_precomputo[0])
  tiempo_ineficiente_median.append(tiempo_sin_precomputo[1])

  print('Terminado con tamaño ' + str(i))

def linear(x):
  return x - min(np.log(intervalo)) * 1.2

if __name__ == "__main__":
  plt.plot(np.log(intervalo), np.log(tiempo_eficiente_median), marker='o', label='Tiempo medio con precomputo')
  plt.plot(np.log(intervalo), np.log(tiempo_ineficiente_median), marker='o', label='Tiempo medio sin precomputo')

  x = np.linspace(min(np.log(intervalo)), max(np.log(intervalo)))
  plt.plot(x, linear(x), label='Recta de pendiente 1')

  plt.grid()

  plt.xlabel('log(Tamaño matriz)')
  plt.ylabel('log(Tiempo computo [s])')

  plt.legend()

  plt.savefig('comparacion_tiempo_tridiagonal.png')

  plt.show()
