# MN-TPs

Para instalar los paquetes necesarios de pip simplemente correr:
pip3 install -r pipRequirements.txt

### Código:

Para testear el algoritmo de eliminación Gaussiana, toma una matriz cuadrada y un vector de números independientes y retorna si existe
una solución al sistema representado. Tanto la implementacion con y sin pivote.
Esta labor esta automatizada en el archivo TestPrecision.py, donde en el main se implementan las matrices particulares para testear el
error numérico y se puede descomentar para ejecutar el test de complejidad temporal.

Para testear eliminacion_gaussiana_tridiagonal_eficiente(a, b, c, d) toma tres vectores a, b, c
donde b representa la diagonal principal, a la diagonal adyacente inferior y c la superior.
d es un array de vectores que toma las constantes independientes de los sistemas a resolver.
Retorna un array con las soluciones de las respectivas constantes independientes.

Para testear eliminacion_gaussiana_tridiagonal_ineficiente(a, b, c, d) toma tres vectores a, b, c
donde b representa la diagonal principal, a la diagonal adyacente inferior y c la superior.
d es un vector que representa la constante independiente del sistema. Retorna la solucion.
Diferencia de nombres se debe a que una version (eficiente) implementa precomputo.

Para testear aproximacion(d, delta_x) toma una segunda derivada sampleada en intervalos regulares delta_x
y retorna la solucion aproximada (u(delta_x), ..., u(n delta_x)) donde u(0) = u(n + 1 delta_x) = 0

Para testear difusion(ci, k) toma un vector ci que representa la constante inicial del proceso y un entero k que
es la cantidad de iteraciones del proceso a correr. Retorna un vector donde el i-esimo elemento
es el resultado del proceso en la i-esima iteracion.
