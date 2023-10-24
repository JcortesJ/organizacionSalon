# Proyecto de Organización de Puntos con Quadtree

Este proyecto tiene como objetivo la organización de una serie de puntos en una cuadrícula de 250x250 que representa las calles y carreras de una región de Bogotá. Utilizaremos un Quadtree para lograr una estructura eficiente de almacenamiento y búsqueda de los puntos en esta región.

## Descripción del Proyecto

El Quadtree es una estructura de datos jerárquica que divide el espacio en cuatro subregiones en cada nivel. En nuestro caso, cada nodo del Quadtree representará una región de la cuadrícula y contendrá información sobre los puntos dentro de esa región. Esto permitirá una búsqueda eficiente de puntos en la cuadrícula.

### Funcionalidades del Proyecto

1. **Inserción de Puntos:** Los usuarios podrán insertar puntos en la cuadrícula, y el Quadtree se encargará de organizarlos en las regiones correspondientes.

2. **Búsqueda de Puntos:** Se podrá buscar puntos en una región específica de la cuadrícula de manera rápida gracias al Quadtree.

3. **Visualización del Mapa:** Los usuarios podrán ver una representación gráfica de la cuadrícula con los puntos y divisiones del Quadtree.

### Visualizacion del mapa 
"mapaOrganizado.png"