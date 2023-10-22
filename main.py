import random
from QuadTree import Area,Edificio,QuadTree,Estudiante

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

arbol = QuadTree(Area(0,0,100,100))

arbol.insertarEdificio(Edificio(10,10,1))
arbol.insertarEdificio(Edificio(20,10,2))
arbol.insertarEdificio(Edificio(20,20,3))
arbol.insertarEdificio(Edificio(10,20,4))
arbol.insertarEdificio(Edificio(10,30,5))
arbol.insertarEdificio(Edificio(30,30,6))
arbol.insertarEdificio(Edificio(30,10,7))
arbol.insertarEdificio(Edificio(60,10,8))
arbol.insertarEdificio(Edificio(90,10,9))
arbol.insertarEdificio(Edificio(90,30,10))
arbol.insertarEdificio(Edificio(60,30,11))
arbol.insertarEdificio(Edificio(30,60,12))

#arbol.insertarEdificio(Edificio(30,30,6))

#arbol.no.no.imprimirEdificios()
arbol.recorrerDesdeHoja()
#arbol.so.imprimirEdificios()