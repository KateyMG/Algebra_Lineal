import numpy as np;
import sympy as sp;
print("----LABORATORIO # 2----")

a = np.random.randint(10, size=(10, 10))      #Matriz de 10x10 con random
b = np.random.randint(10, size=(10, 10))

A = np.array([[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], #Matriz de 10x10 manualmente
              [3, 4, 1, 0, 2, 9, 3, 8, 7, 5],
              [8, 9, 7, 6, 5, 4, 3, 4, 2 ,1],
              [0, 1, 9, 2, 8, 4, 7, 5, 3, 6],
              [6, 2, 1, 4, 5, 3, 6, 7, 9, 8],
              [1, 0, 8, 9, 4, 3, 2, 1, 5, 7],
              [5, 0, 3, 6, 1, 7, 8, 9, 4, 2],
              [7, 1, 0, 9, 2, 4, 5, 8, 9, 3],
              [1, 0, 2, 7, 8, 9, 6, 5, 3, 4],
              [1, 0, 2, 5, 6, 4 ,8, 9, 3, 7]])

B = np.array([[0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
              [1, 5, 1, 0, 2, 9, 3, 8, 7, 8],
              [2, 9, 5, 6, 5, 4, 3, 4, 2 ,7],
              [3, 1, 9, 5, 8, 4, 7, 5, 3, 6],
              [4, 2, 1, 4, 5, 3, 6, 7, 9, 5],
              [5, 0, 8, 9, 4, 5, 2, 1, 5, 4],
              [6, 0, 3, 6, 1, 7, 5, 9, 4, 3],
              [7, 1, 0, 9, 2, 4, 5, 5, 9, 3],
              [8, 0, 2, 7, 8, 9, 6, 5, 5, 1],
              [9, 0, 2, 5, 6, 4 ,8, 9, 3, 0]])

print("****Matriz a****\n"+str(a)+"\n")
print("---diagonal 00000---\n")        #Cambiar diagonal de la matriz
np.fill_diagonal(a, 0)
print(str(a)+"\n")

print("****Matriz b****\n"+str(b)+"\n")
print("---diagonal 00000---\n")        #Cambiar diagonal de la matriz
np.fill_diagonal(b, 0)
print(str(b)+"\n")

print("****Matriz A****\n"+str(A)+"\n")
print("---diagonal 00000---\n")        #Cambiar diagonal de la matriz
np.fill_diagonal(A, 0)
print(str(A)+"\n")

print("****Matriz B****\n"+str(B)+"\n")
print("---diagonal 00000---\n")        #Cambiar diagonal de la matriz
np.fill_diagonal(B, 0)
print(str(B)+"\n")

#Cambiar diagonal
e = np.zeros((10, 10), int)
np.fill_diagonal(e, 5)
print(e)

#Suma de Matrices
print ("suma a+b \n " + str(a+b) +"\n")
print ("suma A+B \n " + str(A+B) +"\n")

#Resta de Matrices
print ("suma a-b \n " + str(a-b) +"\n")
print ("suma A-B \n " + str(A-B) +"\n")

#Multiplicación de Matrices, elemento por elemento
print ("suma a*b \n " + str(a*b) +"\n")
print ("suma A*B \n " + str(A*B) +"\n")

#Producto Matricial
print ("Producto Matricial a*b \n " + str(np.matmul(a,b)) +"\n")
print ("Producto Matricial A*B \n " + str(np.matmul(A,B)) +"\n")

#Vectores para producto punto y cruz
c = np.arange(3)
d = 2 + c
print("c \n" + str(c) + " \nd\n " + str(d))
#Producto Punto
print ("Producto Punto\n" + str(np.dot(c,d)) +"\n")

#Producto Cruz
print("Producto cruz\n" + str(np.cross(c, d))+"\n")

#Traspuesta
print ("a traspuesta \n " + str(a.transpose()) +"\n")
print ("b traspuesta \n " + str(b.transpose()) +"\n")
print ("A traspuesta \n " + str(A.transpose()) +"\n")
print ("B traspuesta \n " + str(B.transpose()) +"\n")

#FERR
C = np.array([[3, -6, 9, 0, -3, 18],
              [-1, 2,-3, 2, 11, 2 ],
              [2, -4, 6,-2, -12, 4]])
print("C: \n " + str(C)+"\n")
print("FERR de C= \n " + str(sp.Matrix(C).rref()))






