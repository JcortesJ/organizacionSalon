from Edificio import Edificio

def run():
    #creacion de salones primero y luego de edificios
    edificios = [
    Edificio(id = 1,capMin=2, capMax=15, capOpt=25, numeroSalones=4, calle=130, carrera=75),
    Edificio(id = 2,capMin=5, capMax=20, capOpt=35, numeroSalones=8, calle=45, carrera=180),
    Edificio(id = 3,capMin=1, capMax=12, capOpt=22, numeroSalones=2, calle=85, carrera=120),
    Edificio(id = 4,capMin=7, capMax=18, capOpt=37, numeroSalones=6, calle=200, carrera=40),
    Edificio(id = 5,capMin=3, capMax=25, capOpt=38, numeroSalones=9, calle=150, carrera=55),
    Edificio(id = 6,capMin=0, capMax=13, capOpt=33, numeroSalones=1, calle=100, carrera=200),
    Edificio(id = 7,capMin=4, capMax=22, capOpt=39, numeroSalones=3, calle=70, carrera=125),
    Edificio(id = 8,capMin=9, capMax=29, capOpt=32, numeroSalones=7, calle=110, carrera=35),
    Edificio(id = 9,capMin=6, capMax=21, capOpt=36, numeroSalones=5, calle=220, carrera=65),
    Edificio(id = 10,capMin=8, capMax=23, capOpt=31, numeroSalones=0, calle=25, carrera=190),
    Edificio(id = 11,capMin=2, capMax=14, capOpt=26, numeroSalones=5, calle=75, carrera=170),
    Edificio(id = 12,capMin=3, capMax=16, capOpt=34, numeroSalones=7, calle=95, carrera=80),
    Edificio(id = 13,capMin=0, capMax=11, capOpt=27, numeroSalones=8, calle=120, carrera=30),
    Edificio(id = 14,capMin=5, capMax=19, capOpt=38, numeroSalones=4, calle=180, carrera=50),
    Edificio(id = 15,capMin=1, capMax=17, capOpt=35, numeroSalones=6, calle=40, carrera=100),
    Edificio(id = 16,capMin=7, capMax=24, capOpt=39, numeroSalones=9, calle=60, carrera=150),
    Edificio(id = 17,capMin=4, capMax=20, capOpt=31, numeroSalones=3, calle=85, carrera=220),
    Edificio(id = 18,capMin=9, capMax=26, capOpt=32, numeroSalones=2, calle=35, carrera=70),
    Edificio(id = 19,capMin=6, capMax=18, capOpt=33, numeroSalones=1, calle=195, carrera=15),
    Edificio(id = 20,capMin=8, capMax=28, capOpt=36, numeroSalones=0, calle=10, carrera=240),
    ]
    return edificios

    # luego insertamos los salones, al menos 5 por cada uno
if __name__=='__main__':
    run()