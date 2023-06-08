from numpy.random import random_integers
from EliminacionGaussiana import Eliminacion_Gaussiana
import numpy
import matplotlib.pyplot as plt
import os
import random
import datetime
import sys
import time

def timeFunction(f, *args):
    start = time.time()
    f(*args)
    end = time.time()
    #print(end - start)
    return end - start

def testTime():
    # Always test on the same matrix. We define A = [1,1,....,1] and b = [1,1,....,1]
    currentDateTime = datetime.datetime.now()
    with open("../datos/CorridaTimes.out", "w") as f:
        f.write("")
    data = []
    medians = []
    minimuns = []
    dataset = []
    # Test matrices on size 10, 20, ..., 500
    # Each matrix will be tested 10 times and recorded time, after that we will take the median and minimum for each size
    for i in range(100, 700, 150):
        A = numpy.identity(i)
        b = numpy.array(numpy.ones(i))
        local = []
        # We will test 10 times each matrix
        for j in range(11):
            # We will record the time for each run
            record = timeFunction(Eliminacion_Gaussiana, A, b)
            data.append([i, record])
            local.append([record])
        local.sort()
        # Median alwasy odd, so we take the middle one
        medians.append([i, local[len(local)//2][0]])
        minimuns.append([i, local[0]])
        dataset.append(local)

    # Write to file the data and begin the row with the size, median and minimum
    with open("../datos/CorridaTimes.out", "w") as f:
        # Write the size and times for each run, which is dataset, a list of lists
        # Write first size of matriz minium time and median time and then the times for each run
        for i in range(len(dataset)):
            #write the items withouth brackets
            for j in range(len(dataset[i])):
                f.write(str(dataset[i][j])[1:-1])
                f.write(" ")
            f.write("\n")
    return


def plotTime():
    with open("../datos/CorridaTimes.out", "r") as f:
        data = f.readlines()
    data = numpy.array([list(map(float, line.split())) for line in data])

    min_time = data[:,0]
    med_time = data[:,1]
    ind_times = data[:,2:]

    # Crear una matriz de entrada x
    x = numpy.arange(100, 700, 150)

    # Calcular la función cúbica de x
    cubic_func = numpy.poly1d(numpy.polyfit(x, numpy.mean(ind_times, axis=1), 3))

    # Crear un gráfico de líneas que muestra los datos de tiempo mínimo y mediana, así como la función cúbica
    #plt.plot(x, min_time, label='Tiempo mínimo')
    plt.plot(x, med_time, label='Tiempo mediana', marker='o')
    plt.plot(x, min_time, label='Tiempo mínimo', marker='o')
    plt.plot(x, cubic_func(x), label='Función cúbica')
    plt.legend()
    plt.xlabel('N (Tamaño de la Matriz)')
    plt.ylabel('Tiempo (segundos)')
    plt.xscale('log')
    plt.yscale('log')
    plt.grid(True)
    plt.title('Tiempos de ejecución y función cúbica')
    #Exportar gráfico a png
    #plt.savefig('Tiempos.png')
    return



if __name__ == "__main__":
    # Matrix 2x2 
    # A = [4x*10**-6 +7y = 5][9x +3y*10**6 = -0.5], sol exacta = [-30000007/102, 22500001/25500000]
    # B Matrix = [4x*10**-12 +7y = 5][9x +3y = -0.5], sol exacta = [-46525000000000/15749999999997, 22500000000001/31499999999994]
    # C [4x*10**-4 +7y = 5][9x +3y*10**-4 = -0.5], sol exacta = [-87537500/1574999997, 1125005000/1574999997]
    A = numpy.matrix([[4*10**-6, 7], [9, 3*10**6]])
    b = numpy.array([5, -0.5])
    aSol = numpy.array([-30000007/102, 22500001/25500000])
    B = numpy.matrix([[4*10**-12, 7], [9, 3]])
    bSol = numpy.array([-46525000000000/15749999999997, 22500000000001/31499999999994])
    C = numpy.matrix([[4*10**-4, 7], [9, 3*10**-4]])
    cSol = numpy.array([-87537500/1574999997, 1125005000/1574999997])
    # Condition number
    print("Condicion de A: ", numpy.linalg.cond(A))
    print("Condicion de B: ", numpy.linalg.cond(B))
    print("Condicion de C: ", numpy.linalg.cond(C))
    # Test the error as difference between the solution and the exact solution
    print("Error A: ", (Eliminacion_Gaussiana(A, b) - aSol))
    print("Error B: ", (Eliminacion_Gaussiana(B, b) - bSol))
    print("Error C: ", (Eliminacion_Gaussiana(C, b) - cSol))

    #testTime()
    plotTime()
 