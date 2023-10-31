from QuadTree import Area,QuadTree
from generarGrafico import generarGrafico
from generacionEntrada import generarEdificios, generarEstudiantes
from formatoEntrada import leerDatos

# Generamos los datos de los estudiantes y edificios
estudiantes = generarEstudiantes(500)
edificios = generarEdificios()

#Creamos el mapa inicial (la raiz del arbol)
raiz = QuadTree(Area(0,0,250,250))

# Insertamos los edificios en el arbol
for i in edificios:
    raiz.insertarEdificio(i)

# Insertamos los estudiantes en su edificio más cercano
for j in estudiantes:
   raiz.insertarEstudiante(j)

# Reacomodamos los estudiantes ubicados en los edificios
raiz.acomodarDesdeHoja()

generarGrafico(raiz,estudiantes,edificios)


