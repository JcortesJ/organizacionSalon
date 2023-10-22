class Edificio:
    #metodo constructor:
    def __init__(self,id,calle=0,carrera=0,capMin=0,capMax=0,capOpt=0,numeroSalones=0):
        self.id = id
        self.capMin = capMin*numeroSalones
        self.capMax = capMax*numeroSalones
        self.capOpt = capOpt*numeroSalones
        self.numeroSalones = numeroSalones
        self.calle = calle
        self.carrera = carrera
        self.listaEstudiantes = []
        self.listaSalones = []
    
    def __str__(self):
        #a = f'Edificio: {self.id},numero estudiantes: {len(self.listaEstudiantes)},\n numero salones: {self.numeroSalones}, calle: {self.calle}, carrera:{self.carrera}'
        a = f'{self.id} est: {len(self.listaEstudiantes)} min: {self.capMin}, Opt:{self.capOpt}, Max:{self.capMax}'
        return a 
    
#Clase para identificar los salones
class Salon:
    def __init__(self, idSalon, capMin, capOpt, capMax): 
        self.idSalon = idSalon # Contiene el piso y el número de salon
        self.capMin = capMin
        self.capOpt = capOpt
        self.capMax = capMax
        self.estudiantes = []
        
        
            