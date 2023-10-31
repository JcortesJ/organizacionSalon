import random
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

#Función para generar el gráfico de los estudiantes y edificios
def generarGrafico(raiz, estudiantes, edificios):
    
    # Cargar una imagen de fondo
    img = mpimg.imread('map.png')  

    # Crear el gráfico con la imagen de fondo centrada
    fig, ax = plt.subplots()
    ax.imshow(img, extent=[raiz.limite.x, raiz.limite.x + (raiz.limite.x+raiz.limite.ancho),
                        raiz.limite.y, raiz.limite.y + (raiz.limite.y+raiz.limite.alto)])

    # Agregar los puntos al gráfico
    for i in estudiantes:
        #Imprimimos los estudiantes como puntos azules
        ax.plot(i.calle, i.carrera, color='blue', marker='.', markersize=5)
    for e in edificios:
        if (len(e.listaEstudiantes)<=0):
            #Imprimos los edificios que no se usan en rojo
            ax.plot(e.calle, e.carrera, color='red', marker='o', markersize=5, alpha=1)
        else:
            #Imprimimos la linea de unión entre estudiantes con su edificio
            for s in e.listaEstudiantes:
                x = [e.calle, s.calle]
                y = [e.carrera, s.carrera]
                ax.plot(x, y, color='purple', linestyle='-', linewidth=0.7, alpha=0.5)
            #Imprimimos los edificios que si se usarán en verde
            ax.plot(e.calle, e.carrera, color='green', marker='o', markersize=5, alpha=1)
    
    # Imprimimos los limites de los cuadrantes del arbol
    n = raiz
    while (n.dividido):
        n = n.no
    while (n.next != None):
        x = [n.limite.x, n.limite.x+n.limite.ancho,n.limite.x +n.limite.ancho,n.limite.x, n.limite.x]
        y = [n.limite.y,n.limite.y, n.limite.y + n.limite.alto, n.limite.y + n.limite.alto, n.limite.y]
        ax.plot(x, y, color='black', linestyle='-', linewidth=0.7, alpha=0.5)
        n = n.next

    # Personalizar el gráfico con los ejes y el título
    ax.set_xlabel('Carrera')
    ax.set_ylabel('Calle')
    ax.set_title('Gráfico de Personas y Edificios')
    ax.legend(bbox_to_anchor = (0.95, 0.6))

    # Mostrar y guardar el gráfico
    plt.savefig('mapaOrganizado.jpg')
    plt.show()