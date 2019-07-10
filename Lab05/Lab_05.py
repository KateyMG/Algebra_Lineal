import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
from sympy.abc import p;


###EJERCICO 1
print('Recta de Mejor Ajuste-Aproximación Lineal')
x = np.array([1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990])
y = np.array([54.1, 59.7, 62.9, 68.2, 69.7, 70.8, 73.7,75.4])
A = np.vstack([x, np.ones(len(x))]).T
print('A \n' +str(A))
m, b = np.linalg.lstsq(A, y, rcond=None)[0]
print('Los coeficientes de la recta de mejor ajuste son:')
print('pendiente = ', round(m,4), 'intersecto =', round(b,4), '\n')
plt.plot(x, y, 'o',label='Datos Actuales')
plt.plot(x, m*x + b,label='Recta Ajustada')
plt.plot(x,y-m*x-b,'x', label='Errores')
plt.plot(x,0*x,'--')
plt.title('Recta de Mejor Ajuste ')
plt.legend()
plt.savefig("Grafica.png")
plt.show()
print(x[0])

print("Esperanza de Vida Año 2000: ")
d=b+(m*2000)
print(d)

print("La esperanza de vida en USA en el año 2000 fue de 76.4")
error= d-76.4
print("Es un buen modelo, la diferencia entre el modelo y la realidad fue de ", error)


###EJERCICIO 2
df = pd.read_excel (r'C:\\Users\\yohan\\PycharmProjects\\Lab_05_AL_KM\Demandas.xlsx')
print (df)

Datos=df.to_numpy()
##x=np.array(())

datos_x = np.array(Datos[:, [0]])
datos_y = np.array(Datos[:, [1]])


A = np.hstack([datos_x, np.ones(datos_x.shape)])
print('A \n' +str(A))
m, b = np.linalg.lstsq(A, datos_y, rcond=None)[0]
m=m[0]
b=b[0]
print('Los coeficientes de la recta de mejor ajuste son:')
print('pendiente = ', round(m,4), 'intersecto =', round(b,4), '\n')
plt.plot(datos_x, datos_y, 'o',label='Datos Actuales')
plt.plot(datos_x, m*datos_x + b,label='Recta Ajustada')
plt.plot(datos_x,datos_y-m*datos_x-b,'x', label='Errores')
plt.plot(datos_x,0*datos_x,'--')
plt.title('Recta de Mejor Ajuste ')
plt.legend()
plt.savefig("Grafica.png")
plt.show()

#Maximización
funcion =(m*p + b)*(p-0.23)
print(funcion)
funcion2 = (m*p*p)+(m*p*-0.23)+(b*p)+(-0.23*b) ##derivar esto
print(funcion2) ##derivaaar
derivada = funcion2.diff(p)
print(derivada)
maximo= 11422.4034009764/16628.7289514763
print(maximo)



