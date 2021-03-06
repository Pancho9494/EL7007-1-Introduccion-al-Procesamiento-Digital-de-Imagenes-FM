# EL7007-1--Francisco-Molina

## Tarea 1 - Detección de objetos en imágenes basado en el modelo de Hubel y Wiesel

El objetivo de esta tarea es desarrollar un sistema simple de detección de objetos en imágenes, basado en la teoría de campos receptivos de Hubel y Wiesel.

En pocas palabras, se genera un detector de patrones convolucionando un kernel balanceado de 3x3 junto al patrón deseado, luego al convolucionar la imágen de búsqueda con el detector se pueden encontrar los objetos.

Considere el siguiente ejemplo, se desea detectar los rombos de un naipe inglés:

<img src="Tarea_1/seis.png" alt="Seis de diamantes" width="271" height="316"/>

Se toma un recorte de un diamante y se convoluciona con un kernel balanceado para así obtener el detector:

<img src="Tarea_1/filtroDetector.png" alt="Filtro detector de diamantes" width="216" height="144"/>

Finalmente se convoluciona el detector con la imagen de búsqueda, se filtran los resultados según un umbral y se detectan los patrones:

<img src="Tarea_1/deteccion.png" alt="Filtro detector de diamantes" width="379" height="212"/>

El informe detallando la implementación se encuentra en [Tarea 1](Tarea_1/Tarea_1_EL7007.pdf) y el código se encuentra en el [Notebook de la Tarea 1](Tarea_1/Tarea_1.ipynb)


## Tarea 2 - Compensación de iluminación y mejoramiento de contraste

El objetivo de esta tarea es explorar distintas alternativas para la corrección de la iluminación y la mejora del contraste.

Se estudia desde métodos clásicos hasta dos de los modelos más modernos de redes convolucionales, en particular se implementa:

1. Métodos clásicos

	1. Extensión de contraste

	2. Ecualización de histograma

	3. Ecualización adaptativa de histograma CLAHE

2. Redes modernas

	1. [Retinex Net](https://github.com/weichen582/RetinexNet)
	
	2. [MIRNet](https://github.com/soumik12345/MIRNet)

A continuación se presentan los mejores resultados para cada imagen de prueba:

Para el edificio el mejor resultado se obtuvo con MIRNet:

<img src="Tarea_2/edificioMIR.png" alt="Edificio mejorado con MIRNet" width="537" height="207"/>

Para el rostro el mejor resultado se obtuvo con CLAHE:

<img src="Tarea_2/rostroCLAHE.png" alt="Rostro mejorado con CLAHE" width="527" height="261"/>

Para la playa el mejor resultado se obtuvo con MIRNet:

<img src="Tarea_2/playaMIR.png" alt="Playa mejorada con MIRNet" width="542" height="332"/>

Y para el vestido el mejor resultado se obtuvo con ecualización de histogramas:

<img src="Tarea_2/vestidoEQ.png" alt="Vestido mejorado con ecualización de histograma" width="548" height="290"/>

El informe detallando la implementación se encuentra en [Tarea 2](Tarea_2/Tarea_2_EL7007.pdf) y el código se encuentra dividido en:

1. [Notebook de métodos clásicos](Tarea_2/Tarea_2_clasicos.ipynb)

2. [Notebook MIRNet](Tarea_2/Tarea_2_MIRNet.ipynb)

3. [Notebook RetinexNet](Tarea_2/Tarea_2_RetinexNet.ipynb)