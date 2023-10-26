def obtenerStringArchivo(raiz_archivo):
    lineas = ''
    try:
        with open(raiz_archivo) as arhivoPlano:
            lineas = arhivoPlano.read()
            #esta funcion solo existe para no repetir tanto este codigo
            

    except FileNotFoundError:
        print('al parecer has escrito mal la direccion del archivo.')
    return lineas

"""
N <- Número de aspirantes
id_1, x_1, y_1, loc_1 <- Información aspirante 1 (separados por coma y uno por línea)
...
id_N, x_N, y_N, loc_N <- Información aspirante N
M <- Número de edificios
id_1, x_1, y_1, loc_1 <- Información edificio 1 (separados por coma y uno por línea)
...
id_M, x_M, y_M, loc_M <- Información edificio M
K <- Número de salones 
id_1, edificio_1, piso_1,  max_1, opt_1, max_1 (separados por coma y uno por línea)
 ...
id_K, edificio_K, piso_K,  max_K, opt_K, max_K
"""
def leerDatos():
    texto = obtenerStringArchivo('./formatoEntrada.txt')
    if texto != '':
        lineas =texto.splitlines()
    #ya que tengo la string en una lista con varios strings separo la informacion
    #primero los estudiantes
    infoEstudiante = []
    nEstudiantes = 0
    nEdificios = 0
    nSalones = 0
    infoEdificio = []
    infoSalon = []
    nEstudiante = False
    nEdificio = False
    nSalon = False
    for i in range(len(lineas)):
        if lineas[i][0]=='N':
            #obtenemos el numero de estudiantes
            nEstudiantes = int(lineas[0][5:])
            nEstudiante= True
        elif nEstudiante and lineas[i][0]!='M':
            infoEstudiante.append(lineas[i].split(', '))
        if lineas[i][0]=='M':
            nEstudiante = False
            nEdificios = int(lineas[i][5:])
            nEdificio = True
        elif nEdificio and lineas[i][0]!='K':
            infoEdificio.append(lineas[i].split(', '))
        if lineas[i][0]=='K':
            nSalon = True
            nEdificios = int(lineas[i][5:])
            nEdificio = False
        elif nSalon:
            infoSalon.append(lineas[i].split(', '))
    #regresamos toda la informacion, primero los estudiantes en el indice 0
    #edificios indice 1
    #salones indice 2
    
    #en este momento ya tenemos identificados los estudiantes, ahora debemos enlazar los salones a los edificios
    #en el indice 2 de cada lista de infoSalon está la id del edificio. Creamos un diccionario que tenga esta informacion
    salonesYedificios = dict()
    for edificio in infoEdificio:
        salonesYedificios[edificio[0]] = []


    for salon in infoSalon:
        l = salonesYedificios[salon[1]]
        l.append(salon)
        salonesYedificios[salon[1]] = l
        #actualizamos el diccionario
    infoSalon = None
    respuesta = [infoEstudiante,infoEdificio,salonesYedificios]

    return respuesta
        
if __name__ == '__main__':
    lista = leerDatos()

    print('salones y edificios')
    for l in lista[2]:
        print(f'***  {l}')
