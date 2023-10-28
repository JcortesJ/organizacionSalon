def imprimirFinal(raiz,estudiantes,edificios): 
        x = raiz
        #Buscamos el area de 0, 0
        while (x.dividido):
            x = x.no
        #Recorremos cada edificio del area
        while (x.next != None):
            for e in x.edificios:
                print("EDIFICIO:"+ e.id)
                #if (len(e.salones)<=0):
                #    print("Edificio no utilizado")
                #else:
                for i in e.salones:
                    print("   SALON: "+ i.id )
                    for j in i.estudiantes:
                        print("    Estudiante: "+j.id+" distancia a edificio: "+ j.distancia)
            x = x.next