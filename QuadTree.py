
from math import sqrt
from Edificio import Edificio,Salon
from Estudiante import Estudiante


#Clase para identificar el área que cubre el cuadrante en el mapa
class Area:
    def __init__(self,x,y,ancho,alto):
        self.x = x
        self.y = y
        self.ancho = ancho
        self.alto = alto
    def __str__(self):
        a = f' Ancho: {self.ancho}, Alto: {self.alto}'
        return a
        

#Clase del quadtree
class QuadTree:
    capacidad = 2 #Cantidad máxima de edificios que puede contener un cuadrante

    def __init__(self, area):
        self.edificios = []
        self.limite = area
        self.dividido = False
        self.tipo = 1
        self.before = None
        self.next = None

    #Función para subdividir un cuadrante si se excedió la cantidad de edificios que puede contener
    def subdividir(self):
        x = self.limite.x
        y = self.limite.y
        ancho = self.limite.ancho/2
        alto = self.limite.alto/2

        #Se crean los nuevos 4 cuadrantes
        self.no = QuadTree(Area(x, y, ancho, alto)) #Zona noroeste
        self.so = QuadTree(Area(x, y+alto, ancho, alto)) #Zona suroeste
        self.ne = QuadTree(Area(x+ancho, y, ancho, alto)) #Zona noreste
        self.se = QuadTree(Area(x+ancho, y+alto, ancho, alto)) #Zona sureste
        
        #Se entrelazan los cuadrantes del arbol siguiendo una curva de hilbert
        
        #Tipos de cuadrantes
        # 1 = abrir izquierda
        # 2 = abrir derecha
        # 3 = abrir arriba
        # 4 = abrir abajo

        if (self.tipo == 1):
            self.no.tipo = 3
            self.no.next = self.ne
            self.no.before = self.before
            self.ne.tipo = 1
            self.ne.next = self.se
            self.ne.before = self.no
            self.se.tipo = 1
            self.se.next = self.so
            self.se.before = self.ne
            self.so.tipo = 4
            self.so.next = self.next
            self.so.before = self.se
            if(self.next != None):
                self.next.before = self.so
            if(self.before != None):
                self.before.next = self.no
        elif (self.tipo == 2):
            self.no.tipo = 2
            self.no.next = self.so
            self.no.before = self.ne
            self.ne.tipo = 3
            self.ne.next = self.no 
            self.ne.before = self.before
            self.se.tipo = 4
            self.se.next = self.next
            self.se.before = self.so
            self.so.tipo = 2
            self.so.next = self.se
            self.so.before = self.no
            if(self.next != None):
                self.next.before = self.se
            if(self.before != None):
                self.before.next = self.ne
        elif (self.tipo == 3):
            self.no.tipo = 1
            self.no.next = self.so
            self.no.before = self.before
            self.ne.tipo = 2
            self.ne.next = self.next
            self.ne.before = self.se
            self.se.tipo = 3
            self.se.next = self.ne
            self.se.before = self.so
            self.so.tipo = 3
            self.so.next = self.se
            self.so.before = self.no
            if(self.next != None):
                self.next.before = self.ne
            if(self.before != None):
                self.before.next = self.no
        elif (self.tipo == 4):
            self.no.tipo = 4
            self.no.next = self.ne
            self.no.before = self.so
            self.ne.tipo = 4
            self.ne.next = self.se
            self.ne.before = self.no
            self.se.tipo = 2
            self.se.next = self.next
            self.se.before = self.ne
            self.so.tipo = 1
            self.so.next = self.no
            self.so.before = self.before
            if(self.next != None):
                self.next.before = self.se
            if(self.before != None):
                self.before.next = self.so

        #Se insertan los edificios de este cuadrante en el nuevo cuadrante correspondiente
        for e in self.edificios:
            if (e.calle < x+ancho):
                if(e.carrera < y+alto):
                    self.no.insertarEdificio(e)
                else:
                    self.so.insertarEdificio(e)
            else:
                if(e.carrera < y+alto):
                    self.ne.insertarEdificio(e)
                else:
                    self.se.insertarEdificio(e)
        
        #Se vacía la lista de edificios del cuadrante
        self.edificios = None
        #Se elimina las referencias a los cuadrantes vecinos
        self.next = None
        self.before = None

    #Función para insertar un edificio dentro del cuadrante
    def insertarEdificio(self,edificio):
        #Si el cuadrante no está dividido, se inserta el edificio en el cuadrante correspondiente
        if(not self.dividido):
            #Se verifica que el cuadrante no ha sobrepasado su capacidad
            self.edificios.append(edificio)
            if (len(self.edificios) > self.capacidad):
                #Si el nuevo cuadrante sobrepasa su capacidad, se subdivide el cuadrante
                self.subdividir()
                self.dividido = True
        else:
            #Si el cuadrante ya está dividido, se inserta el edificio en el cuadrante correspondiente
            if (edificio.calle < self.limite.x + self.limite.ancho/2):
                if(edificio.carrera < self.limite.y + self.limite.alto/2):
                    self.no.insertarEdificio(edificio)
                else:
                    self.so.insertarEdificio(edificio)
            else:
                if(edificio.carrera < self.limite.y + self.limite.alto/2):
                    self.ne.insertarEdificio(edificio)
                else:
                    self.se.insertarEdificio(edificio)
    
    def verificarEdificiosDisponibles (edificios):
        edificiosDisponibles = []
        for e in edificios:
            if e.disponible:
                edificiosDisponibles.append(e)
        return edificiosDisponibles
    
    def insertarEstudiante(self,estudiante):
        #Si el cuadrante no está dividido, se inserta el estudiante en el edificio correspondiente
        if(not self.dividido):
            #Se verifica que el cuadrante no esté vacío, en caso de que si esté vacío se toman los edificios de los cuadrantes vecinos
            if self.next  != None and self.before != None:
                areaSiguiente = self.next
                arearAnterior = self.before
                edificiosDisponibles = self.verificarEdificiosDisponibles(self.edificios)
                while (len(edificiosDisponibles) <= 0):
                #puse los ifs porque a veces me daba error
                # a veces = cuando incremento los estudiantes
                    if areaSiguiente != None:
                        edificiosDisponibles = self.verificarEdificiosDisponibles(areaSiguiente.edificios)
                        areaSiguiente = areaSiguiente.next
                    if arearAnterior != None:
                        edificiosDisponibles.extend(arearAnterior.edificios)
                        arearAnterior = arearAnterior.before
            
            #Se recorren los edificios del cuadrante con el fin de encontrar el más cercano
                edificioCercanos = edificiosDisponibles[0]
                distanciaMinima = sqrt((edificioCercanos[0].carrera -estudiante.carrera)**2 + (edificioCercanos[0].calle - estudiante.calle)**2)
                
                # Ordena los edificios por distancia en comparación a la primera
                for e in edificiosDisponibles:
                    distancia = sqrt((e.carrera -estudiante.carrera)**2 + (e.calle - estudiante.calle)**2)
                    if ( distancia < distanciaMinima and e.disponible):
                        edificioCercanos.insert(0,e)
                        distanciaMinima = distancia
                
                # Agrega los edificios que no estan en la lista de edificios cercanos
                for e in edificiosDisponibles:
                    if (e not in edificioCercanos and e.disponible):
                        edificioCercanos.append(e)
                
                asignado = False
                i = 0
                #Se agrega el estudiante al edificio más cercano
                #modificacion del atributo
                while (not asignado and i < len(edificioCercanos)):
                    edificioCercano = edificioCercanos[i]
                    ocupacion = len(edificioCercano.listaEstudiantes)
                    if  ( ocupacion < edificioCercano.capMax-1):
                        edificioCercano.listaEstudiantes.append(estudiante)
                        estudiante.lugar = Edificio.id.toString()
                        estudiante.distancia = sqrt((edificioCercano.carrera -estudiante.carrera)**2 + (edificioCercano.calle - estudiante.calle)**2)
                        asignado = True
                    elif (ocupacion == edificioCercano.capMax-1):
                        edificioCercano.listaEstudiantes.append(estudiante)
                        estudiante.lugar = Edificio.id.toString()
                        estudiante.distancia = sqrt((edificioCercano.carrera -estudiante.carrera)**2 + (edificioCercano.calle - estudiante.calle)**2)
                        asignado = True
                        edificioCercano.disponible = False                   
                    i += 1

        #Si el cuadrante está dividido, se inserta el estudiante en el cuadrante correspondiente
        elif (estudiante.calle < self.limite.x + self.limite.ancho/2):
            if(estudiante.carrera < self.limite.y + self.limite.alto/2):
                self.no.insertarEstudiante(estudiante)
            else:
                self.so.insertarEstudiante(estudiante)
        else:
            if(estudiante.carrera < self.limite.y + self.limite.alto/2):
                self.ne.insertarEstudiante(estudiante)
            else:
                self.se.insertarEstudiante(estudiante)

    def asignarSalones(self,edificio:Edificio):
        ocupacion = len(edificio.listaEstudiantes)
        if (ocupacion < edificio.capMin):
            return None
        elif (ocupacion < edificio.capOpt):
            k = 0
            for i in range(0,len(edificio.listaSalones)):
                for j in range(0,edificio.listaSalones[i].capMin):
                    edificio.listaSalones[i].estudiantes.append(edificio.listaEstudiantes[k])
                    edificio.listaEstudiantes[k].lugar = edificio.listaSalones[i].idSalon
                    k += 1
            for i in range(0,len(edificio.listaSalones)):
                for j in range(edificio.listaSalones[i].capMin,edificio.listaSalones[i].capOpt):
                    edificio.listaSalones[i].estudiantes.append(edificio.listaEstudiantes[j])
                    edificio.listaEstudiantes[j].lugar = edificio.listaSalones[i].idSalon
        elif (ocupacion < edificio.capMax):
            k = 0
            for i in range(0,len(edificio.listaSalones)):
                for j in range(0,edificio.listaSalones[i].capOpt):
                    edificio.listaSalones[i].estudiantes.append(edificio.listaEstudiantes[k])
                    edificio.listaEstudiantes[k].lugar = edificio.listaSalones[i].idSalon
                    k += 1
            for i in range(0,len(edificio.listaSalones)):
                for j in range(edificio.listaSalones[i].capOpt,edificio.listaSalones[i].capMax):
                    edificio.listaSalones[i].estudiantes.append(edificio.listaEstudiantes[j])
                    edificio.listaEstudiantes[j].lugar = edificio.listaSalones[i].idSalon
                

    #Función para imprimir los edificios del cuadrante
    def imprimirEdificios(self):
        if (not self.dividido):
            if (len(self.edificios) <= 0):
                print("Ningun edificio en este cuadrante con limite: ")
                print(self.limite)
            else:
                #eliminar repetidos
                self.edificios = list(set(self.edificios))
                for edificio in self.edificios:
                    print(edificio)
                
        else:
            print("Cuadrante dividido")
    
    #Función para imprimir los edificios de cada cuadrante desde la hoja actual en adelante
    def recorrerDesdeHoja(self):
        
        x = self
        while (x.dividido):
            x = x.no
        while (x.next != None):
            x.imprimirEdificios()
            print("------------------")
            x = x.next
        x.imprimirEdificios()
       


