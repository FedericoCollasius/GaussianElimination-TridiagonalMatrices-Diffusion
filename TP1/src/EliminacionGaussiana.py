import numpy as np
import matplotlib.pyplot as plt
import time as time
import os 

def isClose(a,b, rel_tol=1e-09, abs_tol=1e-06):
    return abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)

def Eliminacion_Gaussiana_Sin_Pivoteo(A, b):
    n = np.shape(A)[0]
    for i in range(0, n):
        if isClose(A[i,i], 0) and i != n-1: # Salvo el caso que la ultima
            return -1
        for j in range(i+1, n):
            mji = A[j, i]/A[i, i]

            for k in range(i, n):
                A[j, k] = A[j, k] - mji*A[i, k]

            b[j] = b[j] - mji*b[i]

    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        if isClose(A[i,i],0): # Si la diagonal es 0, no hay solucion o hay infinitas
            return -1
        for j in range(i+1, n):
            b[i] = b[i] - A[i, j]*x[j]

        x[i] = b[i]/A[i, i]
    return x

def Eliminacion_Gaussiana(A, b):
    n = np.shape(A)[0]
    for i in range(0, n):
        if isClose(A[i,i], 0) and i != n-1: # Salvo el caso que la ultima
            max = 0
            row = 0
            for w in range(i+1, n):
                if A[w, i] > max:
                    max = A[w, i]
                    row = w
            if isClose(max, 0):
                return -1
            else:
                A[i, row] = A[row, i]

        for j in range(i+1, n):
            mji = A[j, i]/A[i, i]
            for k in range(i, n):
                A[j, k] = A[j, k] - mji*A[i, k]

            b[j] = b[j] - mji*b[i]

    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        if isClose(A[i,i],0): # Si la diagonal es 0, no hay solucion o hay infinitas
            return -1
        for j in range(i+1, n):
            b[i] = b[i] - A[i, j]*x[j]

        x[i] = b[i]/A[i, i]
    return x

def test():
    for i in range(1000):
        n = np.random.randint(1, 100)
        A = np.random.rand(n, n)
        b = np.random.rand(n)
        assert(np.allclose(np.linalg.solve(A, b), Eliminacion_Gaussiana(A,b)))
    print("Test pasado")
            
if __name__ == "__main__":
    test()
