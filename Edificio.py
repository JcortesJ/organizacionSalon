class Edificio:
    #metodo constructor:
    def __init__(self,id,calle=0,carrera=0,capMin=0,capMax=0,capOpt=0,numeroSalones=0,pisos=0):
        self.id = id
        self.pisos = pisos
        self.capMin = capMin*numeroSalones
        self.capMax = capMax*numeroSalones
        self.capOpt = capOpt*numeroSalones
        self.numeroSalones = numeroSalones
        self.calle = calle
        self.carrera = carrera
        self.listaEstudiantes = []
        self.listaSalones = []
        self.disponible = True
    
    def __str__(self):
        #a = f'Edificio: {self.id},numero estudiantes: {len(self.listaEstudiantes)},\n numero salones: {self.numeroSalones}, calle: {self.calle}, carrera:{self.carrera}'
        a = f'{self.id} est: {len(self.listaEstudiantes)} min: {self.capMin}, Opt:{self.capOpt}, Max:{self.capMax}  calle: {self.calle}, carrera:{self.carrera}'
        return a 
    
    def crearSalones(self):
        #primero tomamos los valores para cada salon
        capMin = self.numeroSalones/self.capMin 
        capMax = self.numeroSalones/self.capMax
        capOpt = self.numeroSalones/self.capOpt
        cambioPisos = self.numeroSalones/self.pisos
        i = 0
        for s in range(self.numeroSalones):
            if(s % cambioPisos == 0):
                piso = int(str(i)+str(s))
                #Aniadimos 
                self.listaSalones.append(Salon(capMax=capMax,idSalon=piso,capMin=capMin,capOpt=capOpt))
    
#Clase para identificar los salones
class Salon:
    def __init__(self, idSalon, capMin, capOpt, capMax): 
        self.idSalon = idSalon # Contiene el piso y el número de salon
        self.capMin = capMin
        self.capOpt = capOpt
        self.capMax = capMax
        self.estudiantes = []
        
    def __str__(self) -> str:
        return f'El salon {self.idSalon} tiene {len(self.estudiantes)}. Min {self.capMin} Max {self.capMax}'
        
        
        
            