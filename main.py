import random
from QuadTree import Area,QuadTree
from Estudiante import Estudiante
from prueba import run
from Edificio import Edificio,Salon

def generar_estudiantes(n):
    estudiantes = []
    for i in range(n):
        id = random.randint(1000000000, 9999999999)
        calle = random.randint(0, 250)
        carrera = random.randint(0, 250)
        estudiante = Estudiante(id, calle, carrera)
        estudiantes.append(estudiante)
    return estudiantes

nEst = 10
listaEstudiantes = generar_estudiantes(nEst)
for i in range(nEst):
    print(listaEstudiantes[i])


raiz = QuadTree(Area(0,0,250,250))

edificios = run()
for i in edificios:
    raiz.insertarEdificio(i)

#raiz.insertarEdificio(Edificio(30,30,6))

#raiz.no.no.imprimirEdificios()
raiz.recorrerDesdeHoja()
#raiz.so.imprimirEdificios()