
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
    
    def insertarEstudiante(self,estudiante):
        #Si el cuadrante no está dividido, se inserta el estudiante en el edificio correspondiente
        if(not self.dividido):
            #Se verifica que el cuadrante no esté vacío, en caso de que si esté vacío se toman los edificios de los cuadrantes vecinos
            if self.next  != None and self.before != None:
                areaSiguiente = self.next
                arearAnterior = self.before
                edificiosDisponibles = self.edificios
                while (len(edificiosDisponibles) <= 0):
                #puse los ifs porque a veces me daba error
                # a veces = cuando incremento los estudiantes
                    if areaSiguiente != None:
                        edificiosDisponibles = areaSiguiente.edificios
                        areaSiguiente = areaSiguiente.next
                    if arearAnterior != None:
                        edificiosDisponibles.extend(arearAnterior.edificios)
                        arearAnterior = arearAnterior.before
            
            #Se recorren los edificios del cuadrante con el fin de encontrar el más cercano
                edificioCercano = edificiosDisponibles[0]
                for e in self.edificios:
                #If es mas cercano se actuliza edificio cercano Falta hacerlo bien :v
                    sqrt((e.carrera -estudiante.carrera)**2 + (e.calle - estudiante.calle)**2)
            #Se agrega el estudiante al edificio más cercano
            #modificacion del atributo
                edificioCercano.listaEstudiantes.append(estudiante)

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
        #Función para imprimir los edificios del cuadrante
    def acomodarEdificios(self):
        if (not self.dividido):
            if (len(self.edificios) > 0):
                #primero ajustamos a todos los edificios a que tengan el minimo
                extraEstudiantes = []
                for edificio in self.edificios:
                    if(len(edificio.listaEstudiantes) > edificio.capMin):
                        #primero vamos a llenar la lista extra estudiantes
                        extraEstudiantes = edificio.listaEstudiantes
                        edificio.listaEstudiantes = []
                        break
                i = 0
                while(i < len(self.edificios) and len(extraEstudiantes)!=0):
                    if(len(edificio.listaEstudiantes) > edificio.capMin):
                        #calculamos la diferencia
                        dif = len(edificio.listaEstudiantes) - edificio.capMin
                        #sacamos a los estudiantes extras y los metemos en la lista
                        extraEstudiantes.extend(edificio.listaEstudiantes[:dif])
                        #actualizamos la lista del edificio al minimo
                        edificio.listaEstudiantes = edificio.listaEstudiantes[dif:]
                    elif (len(edificio.listaEstudiantes) < edificio.capMin and len(extraEstudiantes)> 0 ):
                        #metemos al minimo de estudiantes en el edificio pero primero calculamos la diferencia
                        dif = len(extraEstudiantes) - edificio.capMin
                        if(dif>0):
                            #hay suficientes estudiantes para meterlos y metemos solo el minimo
                            edificio.listaEstudiantes.extend(extraEstudiantes[:dif])
                            #actualizamos la lista de estudiantes extras
                            extraEstudiantes = extraEstudiantes[dif:]
                        else:
                            #solo podemos meter los estudiantes extras que haya
                            edificio.listaEstudiantes.extend(extraEstudiantes)
                    i+=1
                    

    #funcion para acomodar a los estudiantes al minimo de edificios y meterlos en salon
    def acomodarDesdeHoja(self):
        x = self
        while (x.dividido):
            x = x.no
        while (x.next != None):
            x.acomodarEdificios()
            x = x.next
        x.acomodarEdificios()
    


