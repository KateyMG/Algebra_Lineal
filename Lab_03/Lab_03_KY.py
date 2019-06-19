import numpy as np
import sympy as sp

import matplotlib

import matplotlib.pyplot as plt

#Funciones
def Aumentar(a):
    Valor='h'+str(sp.Matrix(a).shape)
    Identidad=sp.eye(int(Valor[2]))
    for x in range(0, int(Valor[2])):
        Identidad=Identidad.col_insert(x, sp.Matrix(a).col(x))
    return Identidad


A = np.array([[1, 1, 0], [1, 0, 1], [0, 1,0]])

B = np.array([[2, 0, 1], [1, 1, -4], [3, 7, -3]])

C = np.array([[1, 1, 0], [1, 0, 1], [0, 1,0], [0, 1,0]])

#Inversas
print(" Inversa de la matriz A usando distintos métodos \n")

inva = np.linalg.inv(A)               #con numpy
print("NUMPY: \n " + str(inva)+"\n")

inva2 = sp.Matrix(A).inv()            #con sympy
print("SYMPY: \n " + str(inva2)+"\n")

inva3 = Aumentar(A).rref()
print("FERR: \n " + str(inva3)+"\n")  #con FERR

print ('------------------------------------------------------ \n')

print(" Inversa de la matriz B usando distintos métodos \n")

inva = np.linalg.inv(B)               #con numpy
print("NUMPY: \n " + str(inva)+"\n")

inva2 = sp.Matrix(B).inv()            #con sympy
print("SYMPY: \n " + str(inva2)+"\n")

inva3 = Aumentar(B).rref()
print("FERR: \n " + str(inva3)+"\n")  #con FERR

print ('------------------------------------------------------ \n')

print(" Inversa de la matriz C usando distintos métodos \n")

try:
    inva = np.linalg.inv(C)
    print("NUMPY: \n " + str(inva) + "\n")
except np.linalg.LinAlgError:
    print("La matriz C no tiene inversa\n")


print ('****************************************************** \n')

#Rango de las Matrices
#El rango de las matrices es el numero maximo de columnas que son LI

print("Rango de la matriz A  \n")
RangoA = np.linalg.matrix_rank(A)
print("Rango: " +str(RangoA)+"\n")
print ('------------------------ \n')

print("Rango de la matriz B  \n")
RangoB = np.linalg.matrix_rank(B)
print("Rango: " +str(RangoB)+"\n")
print ('------------------------ \n')

print("  Rango de la matriz C  \n")
RangoC = np.linalg.matrix_rank(C)
print("Rango: " +str(RangoC)+"\n")

print ('****************************************************** \n')

#Espacio Nulo y Nulidad

print("Nulidad de la matriz A\n")
NumcolsA = A.shape[1]
NulidadA= RangoA-NumcolsA
print("Nulidad: " +str(NulidadA)+"\n")
print("Base Espacio nulo: \n" + str(sp.Matrix(A).nullspace()))
print ('------------------------ \n')

print("Nulidad de la matriz B\n")
NumcolsB = B.shape[1]
NulidadB= RangoB-NumcolsB
print("Nulidad: " +str(NulidadB)+"\n")
print("Base Espacio nulo: \n" + str(sp.Matrix(B).nullspace()))
print ('------------------------ \n')

print("Nulidad de la matriz C\n")
NumcolsC = C.shape[1]
NulidadC= RangoC-NumcolsC
print("Nulidad: " +str(NulidadC)+"\n")
print("Base Espacio nulo: \n" + str(sp.Matrix(C).nullspace()))

print ('****************************************************** \n')

#Graficas

def f(x):
    return 1-x
def f1(x):
    return x-4
def f2(x):
    return x+4
def f3(x):
    return 6-x

# Valores que tomara x
x = range(-10, 10)

#Color de los ejes.
plt.axhline(0, color="black")
plt.axvline(0, color="black")

#Limites de los ejes.
plt.xlim(-8, 8)
plt.ylim(-8, 8)

plt.savefig("output.png")
plt.grid

plt.title("Región")
plt.xlabel("Eje x")
plt.ylabel("Eje y")
plt.plot(x, [f(i) for i in x], label="1-x")
plt.plot(x, [f1(i) for i in x], label="x-4")
plt.plot(x, [f2(i) for i in x], label="x+4")
plt.plot(x, [f3(i) for i in x], label="6-x")
plt.legend()
plt.legend(loc="upper left")
plt.grid(linestyle="--")
plt.show()

#Graficar region
def f(x):
    return 1-x
def f1(x):
    return x-4
def f2(x):
    return x+4
def f3(x):
    return 6-x

def f4(x):
    if(x>=1):
        return f3(x)
    else:
        return f2(x)
def f5(x):
    if(x>=(5/2)):
        return f1(x)
    else:
        return f(x)

# Valores que tomara x
x = np.arange(-10, 10,0.1)
x1 = np.arange(-1.5, 5.1,0.1)

#Color de los ejes.
plt.axhline(0, color="black")
plt.axvline(0, color="black")

#Limites de los ejes.
plt.xlim(-8, 8)
plt.ylim(-8, 8)


plt.grid

plt.title("Región")
plt.xlabel("Eje x")
plt.ylabel("Eje y")
y = [f(i) for i in x]
y1 = [f1(i) for i in x]
y2=[f2(i) for i in x]
y3=[f3(i) for i in x]
y7 = [f4(i) for i in x1]
y8= [f5(i) for i in x1]
plt.plot(x, y, label="y")
plt.plot(x, y1, label="y1")
plt.plot(x, y2, label="y2")
plt.plot(x, y3, label="y3")
#plt.plot(x1, y7, label="y7")
#plt.plot(x1, y8, label="y8")

plt.legend()
plt.legend(loc="upper left")
plt.grid(linestyle="--")
y5=np.minimum(y2,y3)
y6=np.maximum(y,y1)

plt.fill_between(x1, y7, y8)
plt.show()


