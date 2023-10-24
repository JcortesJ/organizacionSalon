import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import random
from QuadTree import Area,QuadTree
from Estudiante import Estudiante
from prueba import run
from Edificio import Edificio,Salon
personas_x = []
personas_y = []

def generar_estudiantes(n):
    estudiantes = []
    for i in range(n):
        id = random.randint(1000000000, 9999999999)
        calle = random.randint(0, 250)
        #esto es para graficar su ubicacion
        personas_x.append(calle)
        carrera = random.randint(0, 250)
        personas_y.append(carrera)
        estudiante = Estudiante(id, calle, carrera)
        estudiantes.append(estudiante)
    return estudiantes

nEst = 500
listaEstudiantes = generar_estudiantes(nEst)

#for i in range(nEst):
#    print(listaEstudiantes[i])
print('++++++++++++++++++++++')

raiz = QuadTree(Area(0,0,250,250))

edificios = run()
for i in edificios:
    raiz.insertarEdificio(i)

#raiz.insertarEdificio(Edificio(30,30,6))
for j in listaEstudiantes:
    raiz.insertarEstudiante(j)
#raiz.no.no.imprimirEdificios()
#raiz.acomodarDesdeHoja()
raiz.recorrerDesdeHoja()
#raiz.so.imprimirEdificios()

#generacion del grafico para entender:
# Datos de personas y edificios

edificios_x =[]
edificios_y =[]
for e in edificios:
    edificios_x.append(e.calle)
    edificios_y.append(e.carrera)

# Cargar una imagen de fondo
img = mpimg.imread('map.png')  

# Crear el gráfico con la imagen de fondo centrada
fig, ax = plt.subplots()
ax.imshow(img, extent=[min(personas_x + edificios_x), max(personas_x + edificios_x),
                       min(personas_y + edificios_y), max(personas_y + edificios_y)])

# Agregar elementos gráficos
ax.scatter(personas_x, personas_y, color='blue', label='Personas', marker='o',s=10)
ax.scatter(edificios_x, edificios_y, color='red', label='Edificios', marker='s', s=100, alpha=0.5)

# Personalizar el gráfico
ax.set_xlabel('Calles')
ax.set_ylabel('Carreras')
ax.set_title('Gráfico de Personas y Edificios')
ax.legend()
plt.legend().set_visible(False)
# Mostrar o guardar el gráfico
plt.show()