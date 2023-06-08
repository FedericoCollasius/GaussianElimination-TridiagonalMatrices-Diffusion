import numpy as np
import matplotlib.pyplot as plt
import time

# Ejercicio 5
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

def operador_laplaciano(n):
  a = np.ones(n - 1, dtype=float)
  c = np.ones(n - 1, dtype=float)
  b = np.full(n, -2, dtype=float)

  return [a, b, c]

# Experimentacion enunciado
def aproximacion(d):
  n = len(d)
  return eliminacion_gaussiana_tridiagonal_eficiente(*operador_laplaciano(n), [d])[0]

if __name__ == '__main__':
  #EXPERIMENTACION
  n = 101
  matriz_operador = operador_laplaciano(n)

  d_1 = np.array([4 / n if i == (n // 2 + 1) else 0 for i in range(n)]) 
  d_2 = np.array([4 / (n ** 2) for i in range(n)], dtype=float)
  d_3 = np.array([(-1 + 2 * i / (n - 1)) * 12 / (n ** 2) for i in range(n)], dtype=float)

  resultado_1 = eliminacion_gaussiana_tridiagonal_eficiente(*operador_laplaciano(n), [d_1])[0]
  resultado_2 = eliminacion_gaussiana_tridiagonal_eficiente(*operador_laplaciano(n), [d_2])[0]
  resultado_3 = eliminacion_gaussiana_tridiagonal_eficiente(*operador_laplaciano(n), [d_3])[0]

  plt.plot(resultado_1, label='$d_1$')
  plt.plot(resultado_2, label='$d_2$')
  plt.plot(resultado_3, label='$d_3$')

  plt.legend()

  plt.xlabel("x")
  plt.ylabel("u(x) aproximado")

  plt.savefig('soluciones_3_poisson.png')

  plt.show()


  # Aproximacion solucion
  n_relevante = [5, 50, 500, 5000]

  for n in n_relevante:
    d_sampleado = np.array([3 for i in range(n)], dtype=float) * (1 / n ** 2)
    u = eliminacion_gaussiana_tridiagonal_eficiente(*operador_laplaciano(n), [d_sampleado])[0]
    intervalo = np.array(range(1, n + 1)) / n
    plt.plot(intervalo, u, label=f'1/{n}')

  plt.xlabel('x')
  plt.ylabel('u(x)')
  plt.legend()
  plt.grid()
  plt.savefig('resultado_ecuacion_poisson.png')
  plt.show()

