#Clase para identificar los estudiantes
class Estudiante:
    def __init__(self, id, calle, carrera): 
        self.id = id
        self.calle = calle 
        self.carrera = carrera 
    
    def __str__(self):
        return "id: " + str(self.id) + " calle: " + str(self.calle) + " carrera: " + str(self.carrera)