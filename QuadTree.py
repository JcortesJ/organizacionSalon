
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
    
    def verificarEdificiosDisponibles (self, edificios):
        edificiosDisponibles = []
        for e in edificios:
            if e.disponible:
                edificiosDisponibles.append(e)
        return edificiosDisponibles

    def insertarEstudiante(self,estudiante:Estudiante):
        #Si el cuadrante no está dividido, se inserta el estudiante en el edificio correspondiente
        if(not self.dividido):
            #Se verifica que el cuadrante no esté vacío, en caso de que si esté vacío se toman los edificios de los cuadrantes vecinos
            if self.next  != None or self.before != None:
                areaSiguiente = self.next
                arearAnterior = self.before
                edificiosDisponibles = []
                edificiosDisponibles.extend(self.verificarEdificiosDisponibles(self.edificios))
                numAreasCercanas = 0
                while (len(edificiosDisponibles) <= 0 or numAreasCercanas <6):
                #puse los ifs porque a veces me daba error
                # a veces = cuando incremento los estudiantes
                    if areaSiguiente != None:
                        edificiosDisponibles.extend(self.verificarEdificiosDisponibles(areaSiguiente.edificios))
                        areaSiguiente = areaSiguiente.next
                        numAreasCercanas += 1
                    if arearAnterior != None:
                        edificiosDisponibles.extend(self.verificarEdificiosDisponibles(arearAnterior.edificios))
                        arearAnterior = arearAnterior.before
                        numAreasCercanas += 1   
            
            #Se recorren los edificios del cuadrante con el fin de encontrar el más cercano
                edificioCercanos = [edificiosDisponibles[0]]
                distanciaMinima = sqrt((edificioCercanos[0].carrera -estudiante.carrera)**2 + (edificioCercanos[0].calle - estudiante.calle)**2)
                
                # Ordena los edificios por distancia en comparación a la primera
                for e in edificiosDisponibles:
                    distancia = sqrt((e.carrera -estudiante.carrera)**2 + (e.calle - estudiante.calle)**2)
                    if ( distancia <= distanciaMinima and e.disponible):
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
                        estudiante.lugar = edificioCercano.id
                        estudiante.distancia = sqrt((edificioCercano.carrera -estudiante.carrera)**2 + (edificioCercano.calle - estudiante.calle)**2)
                        asignado = True
                        #print('Estudiante asignado: ',estudiante.id, 'lugar: ',estudiante.lugar, ' distancia: ',estudiante.distancia, 'CalleOri: ',estudiante.calle, 'carreraOri: ',estudiante.carrera)
                        return estudiante
                    elif (ocupacion == edificioCercano.capMax-1):
                        edificioCercano.listaEstudiantes.append(estudiante)
                        estudiante.lugar = edificioCercano.id
                        estudiante.distancia = sqrt((edificioCercano.carrera -estudiante.carrera)**2 + (edificioCercano.calle - estudiante.calle)**2)
                        asignado = True
                        edificioCercano.disponible = False  
                        #print('Estudiante asignado: ',estudiante.id)
                        return estudiante                 
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
            nEstAsignados= 0
            for i in range(0,len(edificio.listaSalones)):
                for j in range(0,ocupacion):
                    if (nEstAsignados< ocupacion):
                        edificio.listaSalones[i].estudiantes.append(edificio.listaEstudiantes[k])
                        edificio.listaEstudiantes[k].lugar = 'Edificio: '+ edificio.id ,'Piso-salon: ',edificio.listaSalones[i].idSalon
                        nEstAsignados+= 1     
                    else:
                        break      
        elif (ocupacion < edificio.capOpt):
            nEstAsignados= 0
            for i in range(0,len(edificio.listaSalones)):
                for j in range(0,edificio.listaSalones[i].capMin):
                    edificio.listaSalones[i].estudiantes.append(edificio.listaEstudiantes[k])
                    edificio.listaEstudiantes[k].lugar = edificio.listaSalones[i].idSalon
                    nEstAsignados+= 1
            for i in range(0,len(edificio.listaSalones)):
                for j in range(edificio.listaSalones[i].capMin,edificio.listaSalones[i].capOpt):
                    if (nEstAsignados< ocupacion):
                        edificio.listaSalones[i].estudiantes.append(edificio.listaEstudiantes[j])
                        edificio.listaEstudiantes[j].lugar = edificio.listaSalones[i].idSalon
                        k+=1
                    else:
                        break
        elif (ocupacion <= edificio.capMax):
            nEstAsignados= 0
            for i in range(0,len(edificio.listaSalones)):
                for j in range(0,edificio.listaSalones[i].capOpt):
                    edificio.listaSalones[i].estudiantes.append(edificio.listaEstudiantes[k])
                    edificio.listaEstudiantes[k].lugar = edificio.listaSalones[i].idSalon
                    nEstAsignados+= 1
            for i in range(0,len(edificio.listaSalones)):
                for j in range(edificio.listaSalones[i].capOpt,edificio.listaSalones[i].capMax):
                    if (nEstAsignados< ocupacion):
                        edificio.listaSalones[i].estudiantes.append(edificio.listaEstudiantes[j])
                        edificio.listaEstudiantes[j].lugar = edificio.listaSalones[i].idSalon
                        k+=1
                    else:
                        break

    def asignarSalonesV2(self,edificio:Edificio):
        ocupacion = len(edificio.listaEstudiantes)

        if (ocupacion < edificio.capMin):
            nEstAsignados = 0
            nSalones = len(edificio.listaSalones)
            salonActual = 0
            nEstEnSalon = 0

            for i in range(0,ocupacion):
                if (i < edificio.listaSalones[salonActual].capMin-nEstEnSalon+nEstAsignados):
                    edificio.listaSalones[salonActual].estudiantes.append(edificio.listaEstudiantes[nEstAsignados])
                    edificio.listaEstudiantes[nEstAsignados].lugar = 'Edificio: '+ edificio.id ,'Piso-salon: ',edificio.listaSalones[salonActual].idSalon
                    nEstAsignados+= 1    
                    nEstEnSalon+=1
                else:
                    salonActual+=1 
                    nEstEnSalon = 0
                
        elif (ocupacion < edificio.capOpt):
            nEstAsignados= 0
            nSalones = len(edificio.listaSalones)
            salonActual = 0
            nEstEnSalon = 0

            for i in range(0,ocupacion):
                if (i < edificio.listaSalones[salonActual].capMin-nEstEnSalon+nEstAsignados):
                    edificio.listaSalones[salonActual].estudiantes.append(edificio.listaEstudiantes[nEstAsignados])
                    edificio.listaEstudiantes[nEstAsignados].lugar = 'Edificio: '+ edificio.id ,'Piso-salon: ',edificio.listaSalones[salonActual].idSalon
                    nEstAsignados+= 1    
                    nEstEnSalon+=1
                else:
                    if (salonActual < nSalones): 
                        salonActual+=1 
                        nEstEnSalon = 0
                    else:
                        break

            for i in range(nEstAsignados,ocupacion):
                if (i < edificio.listaSalones[salonActual].capOpt-nEstEnSalon+nEstAsignados):
                    edificio.listaSalones[salonActual].estudiantes.append(edificio.listaEstudiantes[nEstAsignados])
                    edificio.listaEstudiantes[nEstAsignados].lugar = 'Edificio: '+ edificio.id ,'Piso-salon: ',edificio.listaSalones[salonActual].idSalon
                    nEstAsignados+= 1    
                    nEstEnSalon+=1
                else:
                    salonActual+=1 
                    nEstEnSalon = 0

        elif (ocupacion <= edificio.capMax):
            nEstAsignados= 0
            nSalones = len(edificio.listaSalones)
            salonActual = 0
            nEstEnSalon = 0

            for i in range(0,ocupacion):
                if (i < edificio.listaSalones[salonActual].capOpt-nEstEnSalon+nEstAsignados):
                    edificio.listaSalones[salonActual].estudiantes.append(edificio.listaEstudiantes[nEstAsignados])
                    edificio.listaEstudiantes[nEstAsignados].lugar = 'Edificio: '+ edificio.id ,'Piso-salon: ',edificio.listaSalones[salonActual].idSalon
                    nEstAsignados+= 1    
                    nEstEnSalon+=1
                else:
                    if (salonActual < nSalones): 
                        salonActual+=1 
                        nEstEnSalon = 0
                    else:
                        break

            for i in range(nEstAsignados,ocupacion):
                if (i < edificio.listaSalones[salonActual].capMax-nEstEnSalon+nEstAsignados):
                    edificio.listaSalones[salonActual].estudiantes.append(edificio.listaEstudiantes[nEstAsignados])
                    edificio.listaEstudiantes[nEstAsignados].lugar = 'Edificio: '+ edificio.id ,'Piso-salon: ',edificio.listaSalones[salonActual].idSalon
                    nEstAsignados+= 1    
                    nEstEnSalon+=1
                else:
                    salonActual+=1 
                    nEstEnSalon = 0

    #Función para imprimir los edificios del cuadrante
    def imprimirEdificios(self):
        edificiosNoUsados = []
        if (not self.dividido):
            if (len(self.edificios) <= 0):
                print("Ningun edificio en este cuadrante con limite: ")
                print(self.limite)

            else:
                #eliminar repetidos
                self.edificios = list(set(self.edificios))
                omitido = 0
                for edificio in self.edificios:
                    #solo mostramos los edificios con estudiantes
                    if len(edificio.listaEstudiantes)>0:
                        print(edificio)
                    else:
                        omitido += 1
                        edificiosNoUsados.append(edificio)
                print(f'Edificios omitidos {omitido}/{len(self.edificios)}')
                
        else:
            print("Cuadrante dividido")

        return edificiosNoUsados
    
    #Función para imprimir los edificios de cada cuadrante desde la hoja actual en adelante
    def recorrerDesdeHoja(self):
        edificiosNoUsados = [] 
        x = self
        while (x.dividido):
            x = x.no
        while (x.next != None):
            edificiosNoUsados.extend(x.imprimirEdificios())
            
            print("------------------")
            x = x.next
        edificiosNoUsados.extend(x.imprimirEdificios())
        return edificiosNoUsados

        
        #Función para imprimir los edificios del cuadrante
    #Funcion para acomodar los edificios a que cumplan el mínimo o lo más cercano a este
    def acomodarEdificios(self):
        if (not self.dividido):
 
            if (len(self.edificios) > 1):
                #primero ajustamos a todos los edificios a que tengan el minimo
                """
                print('**********************')
                print('Configuracion inicial del cuadrante:')
                for e in self.edificios:
                    print(e)   
                """
                extraEstudiantes = []
                for edificio in self.edificios:
                    #if(len(edificio.listaEstudiantes) > edificio.capMin):
                        #primero vamos a llenar la lista extra estudiantes
                        extraEstudiantes.extend(edificio.listaEstudiantes)
                        edificio.listaEstudiantes = []

                #luego reacomodamos la lista para que estén primero los salones que tienen capacidad minima mas baja
                #con el fin de llenarlos primero
                if(self.edificios[0].capMin > self.edificios[1].capMin ):
                    aux = self.edificios[0]
                    self.edificios[0] = self.edificios[1]
                    self.edificios[1] = aux 
                    
                for e in range(len(self.edificios)):
                    if self.edificios[e].capMin < len(extraEstudiantes):
                        if e+1<len(self.edificios):
                            if (len(extraEstudiantes)-self.edificios[e].capMin)-self.edificios[e+1].capMin < 0:
                            #si ya no hay sufucientes estudiantes para meterlos en el otro salon
                            #pues la diferencia es negativa, metelos todos
                                self.edificios[e].listaEstudiantes = extraEstudiantes
                                extraEstudiantes = None
                                break
                            else:
                            #si si, mete solo hasta el minimo
                                self.edificios[e].listaEstudiantes.extend(extraEstudiantes[:self.edificios[e].capMin])
                                extraEstudiantes = extraEstudiantes[self.edificios[e].capMin:]
                        else:
                        #insertamos lo que podamos si es el ultimo elemento
                            self.edificios[e].listaEstudiantes.extend(extraEstudiantes)
                            extraEstudiantes = None
                    elif e==0 and self.edificios[e].capMin > len(extraEstudiantes):
                        #si estamos en el primer elemento y los estudiantes extra no alcanzan
                        #los metemos todos en el primero que es el del minimo mas bajo
                        self.edificios[e].listaEstudiantes = extraEstudiantes
                        extraEstudiantes = None
                        break
                #finalmente recorremos el cuadrante de nuevo para saber 
                #si hay alguno que supere la capacidad máxima, que lo mueva al otro edificio
                
                if len(self.edificios[0].listaEstudiantes) >= self.edificios[0].capMax:
                    #movemos al siguiente edificio (index 1)
                    dif = abs(len(self.edificios[0].listaEstudiantes) - self.edificios[0].capMax)
                    if (len(self.edificios[1].listaEstudiantes)+dif) < self.edificios[1].capMax:
                    #creamos la lueva lista
                        moverEstudiantes = self.edificios[0].listaEstudiantes[self.edificios[0].capMax:]
                        self.edificios[1].listaEstudiantes.extend(moverEstudiantes)
                        #actualizamos la lista
                        self.edificios[0].listaEstudiantes = self.edificios[0].listaEstudiantes[:self.edificios[0].capMax]
                elif len(self.edificios[1].listaEstudiantes) >= self.edificios[1].capMax:
                    #movemos al siguiente edificio (index 1)
                    dif = abs(len(self.edificios[1].listaEstudiantes) - self.edificios[1].capMax)
                    if (len(self.edificios[0].listaEstudiantes)+dif) < self.edificios[0].capMax:
                    #creamos la lueva lista
                        moverEstudiantes = self.edificios[1].listaEstudiantes[self.edificios[1].capMax:]
                        self.edificios[0].listaEstudiantes.extend(moverEstudiantes)
                        #actualizamos la lista
                        self.edificios[1].listaEstudiantes = self.edificios[1].listaEstudiantes[:self.edificios[1].capMax]
                        
                #Una vez hemos revisado el cuadrante asignamos los salones
                for e in self.edificios:
                    if len(e.listaEstudiantes)>0:
                        self.asignarSalones(edificio=e)
                            
    #funcion para acomodar a los estudiantes al minimo de edificios y meterlos en salon
    def acomodarDesdeHoja(self):
        x = self
        while (x.dividido):
            x = x.no
        while (x.next != None):
            x.acomodarEdificios()
            x = x.next
        x.acomodarEdificios()
    


#calculando el centroide ude una región se puedee contruir un grafioadpproximado