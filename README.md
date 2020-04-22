# Conway's Game Of Life 🔲
Implementación gráfica del juego de la vida de Conway. Creado en Python 3.8.2 mediante el uso de las siguientes dependencias:

- PyGame

- Thorpy

- PIL

- NumPy

- Matplotlib

## ¿Qué hace?

El programa consiste en una interfaz gráfica inicial que pide los argumentos de la simulación, aquí usted debe digitar el tamaño de la grilla, el número de células iniciales (Si se desea colocar manualmente la células, escribir 0. De lo contrario el programa colocará aleatoriamente el número ingresado) y el número de generaciones que se quieran ver. Una vez se tengan digitados estos datos, podrá dar comenzar.

Una vez haya dado en comenzar, existen dos escenarios posibles:

1. **Usted digitó "0" en el número de células iniciales:** si hizo esto, debe aparecer en su pantalla una grilla llena de celdas negras, en este momento usted puede elegir cuáles células (celdas) estarán vivas presionando el click izquierdo, si se equivoca solo deberá volver a dar click izquierdo sobre la célula y volverá a su estado anterior. Una vez termine de arma la configuración de células que desea podrá dar click derecho para empezar la simulación.
2. **Usted digitó un número mayor que cero:** si hizo esto, de inmediato empezará a correr la simulación. Podrá notar que en la parte inferior central, se encuentran un botón verde que le servirá para pausar la simulación, una vez pausada usted tendrá la opción de ir avanzando las generaciones uno a uno de forma manual. Note que cuando la simulación está des-pausada, si no mueve el ratón por más de un segundo el control de pausa se ocultará, para des-ocultarlo solo mueva el mouse.

En el momento que desee terminar la ejecución solo deberá dar click en la x que se encuentra en la esquina superior derecha, al hacer esta acción el programa se cerrará y una imagen con las estadísticas de las generaciones le será mostrada.

## A tener en cuenta ⚠

El programa no se encuentra muy optimizado por lo que al aumentar el número de celdas puede sufrir con seguridad parones en la ejecución.