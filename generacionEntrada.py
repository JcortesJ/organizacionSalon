# Generación de datos para N
import random
from Edificio import Edificio
from Estudiante import Estudiante


N = 250
print('N <- 250')
for i in range(N):
    id_N = random.randint(10000, 99999)
    x_N = random.randint(0, 250)
    y_N = random.randint(0, 250)
    loc_N = random.choice(['Norte', 'Centro', 'Sur', 'Oriente', 'Occidente'])
    #print(f"{id_N}, {x_N}, {y_N}, {loc_N}")

# Generación de datos para M
M = 20
ids_edificios = []
print('M <- 20')
for i in range(M):
    id_M = random.randint(1000, 9999)
    x_M = random.randint(0, 250)
    y_M = random.randint(0, 250)
    loc_M = random.choice(['Norte', 'Centro', 'Sur', 'Oriente', 'Occidente'])
    #print(f"{id_M}, {x_M}, {y_M}, {loc_M}")
    ids_edificios.append(id_M)

# Generación de datos para K
K = 50
print('K <- 50')
for i in range(K):
    id_K = random.randint(100, 999)
    id_M = random.choice(ids_edificios)
    piso_K = random.randint(0, 10)
    max_K = random.randint(0, 40)
    opt_K = random.randint(0, 30)
    min_K = random.randint(0, 10)
    #print(f"{id_K}, {id_M}, {piso_K}, {max_K}, {opt_K}, {min_K}")

#en esta funcion debo hacer los datos de edificio 
def generarEdificios():
    #creacion de salones primero y luego de edificios
    edificios = [
    Edificio(id = 1,capMin=2, capOpt=15, capMax=25, numeroSalones=4, calle=130, carrera=75,pisos=2),
    Edificio(id = 2,capMin=5, capOpt=20, capMax=35, numeroSalones=8, calle=45, carrera=180,pisos=2),
    Edificio(id = 3,capMin=1, capOpt=12, capMax=22, numeroSalones=2, calle=85, carrera=120,pisos=2),
    Edificio(id = 4,capMin=7, capOpt=18, capMax=37, numeroSalones=6, calle=200, carrera=40,pisos=6),
    Edificio(id = 5,capMin=3, capOpt=25, capMax=38, numeroSalones=9, calle=150, carrera=55,pisos=2),
    Edificio(id = 6,capMin=1, capOpt=13, capMax=33, numeroSalones=1, calle=100, carrera=200,pisos=3),
    Edificio(id = 7,capMin=4, capOpt=22, capMax=39, numeroSalones=3, calle=70, carrera=125,pisos=2),
    Edificio(id = 8,capMin=9, capOpt=29, capMax=32, numeroSalones=7, calle=110, carrera=35,pisos=2),
    Edificio(id = 9,capMin=6, capOpt=21, capMax=36, numeroSalones=5, calle=220, carrera=65,pisos=1),
    Edificio(id = 10,capMin=8, capOpt=23, capMax=31, numeroSalones=2, calle=25, carrera=190,pisos=1),
    Edificio(id = 11,capMin=2, capOpt=14, capMax=26, numeroSalones=5, calle=75, carrera=170,pisos=4),
    Edificio(id = 12,capMin=3, capOpt=16, capMax=34, numeroSalones=7, calle=95, carrera=80,pisos=2),
    Edificio(id = 13,capMin=10, capOpt=11, capMax=27, numeroSalones=8, calle=120, carrera=30,pisos=1),
    Edificio(id = 14,capMin=5, capOpt=19, capMax=38, numeroSalones=4, calle=180, carrera=50,pisos=3),
    Edificio(id = 15,capMin=1, capOpt=17, capMax=35, numeroSalones=6, calle=40, carrera=100,pisos=2),
    Edificio(id = 16,capMin=7, capOpt=24, capMax=39, numeroSalones=9, calle=60, carrera=150,pisos=2),
    Edificio(id = 17,capMin=4, capOpt=20, capMax=31, numeroSalones=3, calle=85, carrera=220,pisos=2),
    Edificio(id = 18,capMin=9, capOpt=26, capMax=32, numeroSalones=2, calle=35, carrera=70,pisos=2),
    Edificio(id = 19,capMin=6, capOpt=18, capMax=33, numeroSalones=1, calle=195, carrera=15,pisos=1),
    Edificio(id = 20,capMin=8, capOpt=28, capMax=36, numeroSalones=3, calle=10, carrera=240,pisos=1),
    Edificio(id = 21,capMin=8, capOpt=28, capMax=36, numeroSalones=2, calle=210, carrera=240,pisos=1),
    Edificio(id = 22,capMin=8, capOpt=28, capMax=36, numeroSalones=4, calle=100, carrera=120,pisos=2),
    Edificio(id = 23,capMin=8, capOpt=28, capMax=36, numeroSalones=2, calle=115, carrera=130,pisos=3),
    Edificio(id = 24,capMin=8, capOpt=28, capMax=36, numeroSalones=3, calle=160, carrera=170,pisos=2),
    Edificio(id = 25,capMin=13, capOpt=50, capMax=70, numeroSalones=2, calle=227, carrera=121,pisos=4),
    Edificio(id = 26,capMin=8, capOpt=28, capMax=36, numeroSalones=4, calle=180, carrera=128,pisos=2),
    Edificio(id = 27,capMin=8, capOpt=28, capMax=36, numeroSalones=2, calle=144, carrera=219,pisos=2),
     #Edificio(id = 28,capMin=8, capOpt=28, capMax=36, numeroSalones=2, carrera=150, calle=220,pisos=2)
    ]
    return edificios

# Generamos los datos de los estudiantes
def generarEstudiantes(n):
    estudiantes = []
    for i in range(n):
        id = random.randint(1000000000, 9999999999)
        calle = random.randint(0, 250)
        carrera = random.randint(0, 250)
        estudiante = Estudiante(id, calle, carrera)
        estudiantes.append(estudiante)
    return estudiantes