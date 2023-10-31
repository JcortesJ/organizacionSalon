# Generación de datos para N
import random
from Edificio import Edificio, Salon
from Estudiante import Estudiante


N = 500
#print('N <- 250')
for i in range(N):
    id_N = random.randint(10000, 99999)
    x_N = random.randint(0, 250)
    y_N = random.randint(0, 250)
    loc_N = random.choice(['Norte', 'Centro', 'Sur', 'Oriente', 'Occidente'])
    #print(f"{id_N}, {x_N}, {y_N}, {loc_N}")

# Generación de datos para M
M = 20
ids_edificios = []
#print('M <- 20')
for i in range(M):
    id_M = random.randint(1000, 9999)
    x_M = random.randint(0, 250)
    y_M = random.randint(0, 250)
    loc_M = random.choice(['Norte', 'Centro', 'Sur', 'Oriente', 'Occidente'])
    #print(f"{id_M}, {x_M}, {y_M}, {loc_M}")
    ids_edificios.append(id_M)

# Generación de datos para K
K = 50
#print('K <- 50')
for i in range(K):
    id_K = random.randint(100, 999)
    id_M = random.choice(ids_edificios)
    piso_K = random.randint(0, 10)
    max_K = random.randint(0, 40)
    opt_K = random.randint(0, 30)
    min_K = random.randint(0, 10)
    #print(f"{id_K}, {id_M}, {piso_K}, {max_K}, {opt_K}, {min_K}")

#en esta funcion debo hacer los datos de edificio 
def generarEdificios(lista,diccionario):
    #creacion de salones primero y luego de edificios
    
    edificios = []
    for i in range(len(lista)):
    #id_1, x_1, y_1, loc_1 <- Información edificio 1 (separados por coma y uno por línea)
        id = int(lista[i][0])
        capMin = 0
        capMax = 0
        capOpt = 0
        numeroSalones = len(diccionario[id])
        calle = int(lista[i][1])
        carrera= int(lista[i][2])
        listaSalones =[]
        for salon in diccionario[id]:
            s = Salon(capMax=int(salon[3]),capOpt=int(salon[4]),capMin=int(salon[5]),idSalon=int(salon[0]))
            #id_K, edificio_K, piso_K,  max_K, opt_K, max_K
            capMax +=int(salon[3])
            capOpt +=int(salon[4])
            capMin +=int(salon[5])
            listaSalones.append(s)
        
        edificios.append(Edificio(id=id,calle=calle,carrera=carrera,capMin=capMin,capMax=capMax,capOpt=capOpt
        ,numeroSalones=numeroSalones,listaSalones=listaSalones))
    
    return edificios

# Generamos los datos de los estudiantes
def generarEstudiantes(lista):
    estudiantes = []
    
    for i in range(len(lista)):
        #id_1, x_1, y_1, loc_1 <- Información aspirante 1 (separados por coma y uno por línea)
        estudiantes.append(Estudiante(id=int(lista[i][0]),calle=int(lista[i][1]),carrera=int(lista[i][2])))

    return estudiantes