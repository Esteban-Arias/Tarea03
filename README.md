# Universidad de Costa Rica
## Escuela de Ingeniería Eléctrica
## IE-0405 Modelos Probabilísticos de Señales y Sistemas  
## Tarea 03
### Estudiante: Esteban Arias Vásquez
### B50677
# Solución:
## 1) (25 %) A partir de los datos, encontrar la mejor curva de ajuste (modelo probabilístico) para las funciones de densidad marginales de X y Y.
Primero se deben importar los datos de 'xy.csv' dentro de una matriz con la librería pandas, es importante tener en cuenta las posiciones de cada vector dentro de esta matriz y conocer que se deben ignorar la primer fila y la primer colunma que no tiene valores numéricos. Luego, se crean dos vectores: x = [5,15] y y=[5,25], esto se hace observando los datos del archivo xy.csv y notando que los valores para x y para y son esos. A partir de esto se realiza una sumatoria de filas y otra sumatoria de colunmas. La sumatoria de filas se realiza para obtener un vector de y con la suma de todos los valores de x para ese punto, y la sumatoria de colunmas para obtener un vector para x con la sumatoria de todos los y's sobre ese punto. Al obtener estos vectores se deben graficar el vector resultante de la sumatoria con su respectivo vector de puntos, para obtener la curva de la función de densidad marginal para X y para Y. 
Al obtener las gráficas se analiza y concluye que ambas funciones de densidad marginales corresponden a una forma Gaussiana, entonces para obtener la curva de mejor ajuste primero se debe crear una función que devuelva la función Gaussiana (en su forma general), luego de esto se utiliza la función curve_fit la cuál devuelve los parámetros de la función de mejor ajuste que en este caso son mu y sigma para cada función de densidad Marginal de X y de Y (ambos valores se imprimen en el .py).
Al obtener estos valores se utilizan directamente dentro de la función Gaussiana creada y el resultado se muestra en las figuras adjuntas dentro de la carpeta. El resultado no es del todo satisfactorio pues para ambos casos crea la campana gaussiana dentro de los límites que corresponden sin embargo se pierde un poco de forma en los valores alejados del centro de la campana. 
## 2)  Asumir independencia de X y Y. Analíticamente, ¿cuál es entonces la expresión de la función de densidad conjunta que modela los datos?
Al asumir que existe independecia estadística de X y de Y, la expresión de la función de densidad conjunta es simplemente la multiplicación de la función de densidad marginal de X por la función de densidad marginal de Y:
$$f_{x,y}(x,y)=f_x(x)*f_y(y) $$
Por lo que sería la multiplicación de la función Gaussiana de X por la función Gaussiana de Y, como sigue:
$$ f_{x,y}=\frac{1}{2 \pi \sigma_x \sigma_y}*exp[\frac{-(\sigma_y (x-\mu_x)^2)+\sigma_x (y - \mu_y)^2}{2\sigma_y \sigma_x}]
$$
## 3) Hallar los valores de correlación, covarianza y coeficiente de correlación (Pearson) para los datos y explicar su significado.
Para encontrar la correlación se utilizan los vectores dados en el archivo 'xyp.csv', se crea un recorrido que realize un recorrido por cada elemento dentro de cada vector y vaya sumando la multiplicación de éstos: $$Correlación = correlación +x[i]*y[i]*p[i]$$ El resultado es: \
La correlación entre x y y es: 149.54281000000012 \
Para la covarianza se utilizan los parámetros mu encontrados de la mejor curva de ajuste: $$ covarianza= correlacion-(mux*muy)$$ El resultado es: \ 
La covarianza entre x y y es: 0.183105046498099 \
Para el coeficiente de covarianza se utilizan los parámetros sigma encontrados de la mejor curva de ajuste: $$ coeficiente = covarianza/(sigmax*2*sigmay*2)$$ 

El coeficiente de covarianza es: 0.0023019877198043152
Al observar estos resultados vemos que cómo ya sabemos la covarianza es una medida que indica cuanto y cómo cambian conjuntamente dos variables aleatorias, en este caso la covarianza es de 0.1831, al ser positiva se tiende a decir que los valores altos de X están asociados con los valores altos de Y, y viceversa, si la covarianza es cero las variables aleatorias son independientes y en este caso es un valor cercano a 0. Analizando el coeficiente de correlación vemos que es un valor positivo muy cercano a 0 lo que indica que existe muy poca correlación entre X y Y (casi independencia), al ser positivo indica que cuando X aumenta Y también lo hace. 



## 4) Graficar las funciones de densidad marginales (2D), la función de densidad conjunta (3D). 
Las gráficas de funciones de densidad marginales (2D) se graficaron en el punto 1 para obtener la curva de mejor ajuste, para la gráfica 3d





```python

```
