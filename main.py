from QuadTree import Area,Edificio,QuadTree

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