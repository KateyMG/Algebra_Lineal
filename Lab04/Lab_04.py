import numpy as np
import sympy as sp
from time import time
#Matrices
A = np.array([[1,1,0],
              [1,0,1],
              [0,1,0]])

B = np.array([[2,0,1,1],
              [1,1,2,0],
              [3,7,-3,1]])

C = np.array([[1,1,0,1],
              [1,0,1,0],
              [0,1,0,0],
              [0,1,0,0]])


#determinantes_de_las_matrices
print("************** 1 **************\n")
#Matriz_A
print("Matriz A\n")
try:
    DETAa = np.linalg.det(A)                             #con numpy
    print("Determinante con numpy: \n " + str(DETAa))
except np.linalg.LinAlgError:
    print("NO ES POSIBLE CALCULAR EL DETERMINANTE")

try:
    DETA2a = sp.Matrix(A).det()                          #con sympy
    print(" \n Determinante con sympy: \n " + str(DETA2a))
except:
    print("NO ES POSIBLE CALCULAR EL DETERMINATE")

#Matriz_B
print("Matriz B\n")
try:
    DETAa = np.linalg.det(B)                             #con numpy
    print("Determinante con numpy: \n " + str(DETAa))
except np.linalg.LinAlgError:
    print("NO ES POSIBLE CALCULAR EL DETERMINANTE")

try:
    DETA2a = sp.Matrix(B).det()                          #con sympy
    print(" \n Determinante con sympy: \n " + str(DETA2a))
except:
    print("NO ES POSIBLE CALCULAR EL DETERMINANTE\n")

#Matriz_C
print("Matriz C\n")
try:
    DETAa = np.linalg.det(C)                             #con numpy
    print("Determinante con numpy: \n " + str(DETAa))
except np.linalg.LinAlgError:
    print("NO ES POSIBLE CALCULAR EL DETERMINANTE\n")

try:
    DETA2a = sp.Matrix(C).det()                          #con sympy
    print(" \n Determinante con sympy: \n " + str(DETA2a))
except:
    print("NO ES POSIBLE CALCULAR EL DETERMINANTE")

print("************** 2 **************\n")

print("La diferencia entre el output de numpy y sympy, es el tipo de dato, el primero de da floats y el segundo me los da en números enteros\n")

#Eigenvalores_y_Eigenvectores
print("************** 3 **************\n")

#Matriz_A
#con numpy
print("Matriz A\n")
EIG = np.linalg.eigvals(A) #medir tiempo
print(("\n Eigenvalores con numpy: \n " + str(EIG)))
EIGVAL, EIGVEC = np.linalg.eig(A)  #medir tiempo
print("\n Eigenvectores con numpy: \n " + str(EIGVEC))

#con sympy
EIG2 = sp.Matrix(A).eigenvals()
print("\n Eigenvalores con sympy: \n " + str(EIG2))
VEC2 = sp.Matrix(A).eigenvects()
print("\n Eigenvalores, Multipliciad y Eigenvectores con sympy: \n ")
print(str(VEC2)+"\n")

#Matriz_C
#con numpy
print("Matriz C\n")
EIG = np.linalg.eigvals(C)
print("\n Eigenvalores con numpy: \n " + str(EIG))
EIGVAL, EIGVEC = np.linalg.eig(C)
print("\n Eigenvectores con numpy: \n " + str(EIGVEC))

#con sympy
EIG2 = sp.Matrix(C).eigenvals()
print("\n Eigenvalores con sympy: \n " + str(EIG2))
VEC2 = sp.Matrix(C).eigenvects()
print("\n Eigenvalores, Multipliciad y Eigenvectores con sympy: \n ")
print(str(VEC2))

#Diagonalización_y_polinomio_caracteristico
print("************** 4 **************\n")
print("Matriz A\n")
try:
    DIAG = sp.Matrix(A).diagonalize()
    print("\n Diagonalizacion con sympy: \n " + str(DIAG))
except:
    print("LA MATRIZ NO ES DIAGONALIZABLE")

try:
    POL = sp.Matrix(A).charpoly()
    print("\n Polinomio caracteristico: \n " + str(POL)+"\n")
except:
    print("NO TIENE POLINOMIO CARACTERÍSTICO")

print("Matriz C\n")
try:
    DIAG = sp.Matrix(C).diagonalize()
    print("\n Diagonalizacion con sympy: \n " + str(DIAG))
except:
    print("LA MATRIZ NO ES DIAGONALIZABLE")

try:
    POL = sp.Matrix(C).charpoly()
    print("\n Polinomio caracteristico: \n " + str(POL))
except:
    print("NO TIENE POLINOMIO CARACTERÍSTICO")

print("\n***********BONO 1*************\n")
print("\n  Eigenvectores con sympy: \n ")
print("Matriz A\n")
A = sp.Matrix([[1,1,0],
              [1,0,1],
              [0,1,0]])
#sp.pprint(A.eigenvals())  #returns eigenvalues and their algebraic multiplicity
sp.pprint(A.eigenvects())  #returns eigenvalues, eigenvects

print("\nMatriz C\n")
C = sp.Matrix([[1,1,0,1],
              [1,0,1,0],
              [0,1,0,0],
              [0,1,0,0]])

sp.pprint(C.eigenvects())

print("************** BONO 2***********")

A = np.array([[1,1,0],
              [1,0,1],
              [0,1,0]])

tiempo_inicial = time()
print("Matriz A\n")
EIG = np.linalg.eigvals(A) #medir tiempo
print(("\n Eigenvalores con numpy: \n " + str(EIG)))
EIGVAL, EIGVEC = np.linalg.eig(A)  #medir tiempo
print("\n Eigenvectores con numpy: \n " + str(EIGVEC))
tiempo_final =time()
tiempo_ejecucion= tiempo_final-tiempo_inicial
print ("El tiempo de ejecucion fue:", tiempo_ejecucion)#En segundos

tiempo_inicial = time()
EIG2 = sp.Matrix(A).eigenvals()
print("\n Eigenvalores con sympy: \n " + str(EIG2))
VEC2 = sp.Matrix(A).eigenvects()
print("\n Eigenvalores, Multipliciad y Eigenvectores con sympy: \n ")
print(str(VEC2)+"\n")
tiempo_final =time()
tiempo_ejecucion= tiempo_final-tiempo_inicial
print ("El tiempo de ejecucion fue:", tiempo_ejecucion)

#NUMPY ES MAS RAPIDOOOOOOOOOOOOO