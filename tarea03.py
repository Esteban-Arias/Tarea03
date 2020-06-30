# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 14:02:32 2020

@author: Esteban
"""


#Tarea 03 Modelos Probabilísticos de Señales y Sistemas
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
from scipy.optimize import curve_fit
from mpl_toolkits.mplot3d import axes3d
from matplotlib import style


#Guardamos los datos dados en matrices
xy = pd.read_csv('xy.csv', header=0)
xy1 = pd.read_csv('xy1.csv')
xyp = pd.read_csv('xyp.csv')

#Realizamos sumatoria de vectores para obtener la PMF
PMFy = np.sum(xy, axis=0)
PMFx = np.sum(xy, axis=1)

#Definimos vectores de x y y (hardcoding)
x = np.array([5,6,7,8,9,10,11,12,13,14,15])
y = np.array([5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25])

#Grafica de PMFx
a = plt.plot(x, PMFx)

plt.grid(True)
plt.title('Función Marginal de X')
plt.ylabel('Probabilidad')
plt.xlabel('X')
plt.savefig('PMFx.jpg')
plt.show()
plt.cla()


#Grafica de PMFy
b = plt.plot(y, PMFy[1:])

#Se grafica a partir del elemento 1 de PMFy para eliminar la sumatorias de letras x (x5x6x7..)
plt.grid(True)
plt.title('Función Margilnal de Y')
plt.xlabel('Y')
plt.ylabel('Probabilidad')
plt.savefig('PMFy.jpg')
plt.show()
plt.cla()

#Definimos función Gaussiana
def gauss(x, mu, sigma):
    return 1/(np.sqrt(2*np.pi*sigma**2))*np.exp((-(x - mu)**2)/(2*sigma**2))
"""-Ahora se prueban valores de mu y sigma que mejor se ajusten a las curvas de densidad marginal
-Analizando la gráfica de la PMF de x se llega a la conslusión que: mu=10, sigma=0.03989"""
#Curva de mejor ajuste para la PMF de x
paramx , _ = curve_fit(gauss, x, PMFx)
gaussX = gauss(x, paramx[0], paramx[1])
#Graficamos a PMFx y Gaussx en el mismo gráfico
plt.plot(x, gaussX)
plt.plot(x, PMFx)
plt.title('Curva de mejor ajuste de la PMF de X')
plt.xlabel('x')
plt.ylabel('Probabilidad de ocurrencia')
plt.grid(True)
plt.savefig('mejorajusteX.png')
plt.show()
plt.cla()

#Curva de mejor ajuste para la PMF de Y
paramy , _ = curve_fit(gauss, y, PMFy[1:])
gaussY = gauss(y, paramy[0], paramy[1])
plt.plot(y, gaussY)
plt.plot(y, PMFy[1:])
plt.title('Curva de mejor ajuste de la PMF de Y')
plt.grid(True)
plt.xlabel('y')
plt.ylabel('Probabilidad de ocurrencia')
plt.savefig('mejorajusteY.png')
plt.show()
plt.cla()

"""2)Asumir independencia de X y Y. Analíticamente, 
¿cuál es entonces la expresión de la función de densidad conjunta que modela los datos?
R/Si son independientes fx,y(x,y)=fx(x)fy(y)
"""
""""3) Hallar los valores de correlación, covarianza y coeficiente de correlación (Pearson) 
    para los datos y explicar su significado.
    3.1) Correlación: es la sumatoria de xy*f(x,y) para cada posición,se hace un doble for para el 
    recorrido:
"""
#Correlación
x1 = xyp["x"]
y1 = xyp["y"]
p1 = xyp["p"]
correlacion=0;
for i in range(231):
    correlacion = correlacion + x1[i]*y1[i]*p1[i];
print(f"La correlación entre x y y es: {correlacion}")
#Covarianza 
mux = 9.90484381
muy = 15.0794609
covarianza= correlacion-(mux*muy)
print(f"La covarianza entre x y y es: {covarianza}")
#Coeficiente de covarianza
sigmax = 3.29944288
sigmay = 6.02693775
coeficiente = covarianza/(sigmax*2*sigmay*2)
print(f"El coeficiente de covarianza es: {coeficiente}")
"""4) Graficar las funciones de densidad marginales (2D), la función de densidad conjunta (3D).
"""
#Funciones de densidad marginales ya se graficaron en el punto 1 para encontrar la curva de mejor ajuste
#Función de densidad conjunta:
#creamos la función:
def densidadc(x, y, mux1, muy1, sigmax1, sigmay1):
    return (1/2*np.pi*sigmax1*sigmay1)*np.exp((-(sigmay1*(x-mux)**2+sigmax1*(y-muy1)**2))/(2*sigmay1*sigmax1))
#Evaluamos la función en X y Y
conjunta = densidadc(x, y, mux, muy, sigmax, sigmay)
print(conjunta)










