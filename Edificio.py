class Edificio:
    #metodo constructor:
    def __init__(self,listaEstudiantes=None,cap_min=0,cap_max=0,cap_opt=0,numeroSalones=0,calle=0,carrera=0):
        self.cap_min = cap_min*numeroSalones
        self.cap_max = cap_max*numeroSalones
        self.cap_opt = cap_opt*numeroSalones
        self.numeroSalones = numeroSalones
        self.calle = calle
        self.carrera = carrera
        self.listaEstudiantes = listaEstudiantes
        
class Salones:
    def __init__(self,cap_minS,cap_optS,cap_maxS,piso,listaEstudiantesS=None):
        self.cap_minS = cap_minS
        self.cap_optS = cap_optS
        self.cap_maxS =cap_maxS
        self.piso = piso
        self.listaEstudiantes = listaEstudiantesS
        
        
            