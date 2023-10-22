from Edificio import Edificio, Salones

def run():
    #creacion de salones primero y luego de edificios
    edificios = [
    Edificio(cap_min=2, cap_max=15, cap_opt=25, numeroSalones=4, calle=130, carrera=75),
    Edificio(cap_min=5, cap_max=20, cap_opt=35, numeroSalones=8, calle=45, carrera=180),
    Edificio(cap_min=1, cap_max=12, cap_opt=22, numeroSalones=2, calle=85, carrera=120),
    Edificio(cap_min=7, cap_max=18, cap_opt=37, numeroSalones=6, calle=200, carrera=40),
    Edificio(cap_min=3, cap_max=25, cap_opt=38, numeroSalones=9, calle=150, carrera=55),
    Edificio(cap_min=0, cap_max=13, cap_opt=33, numeroSalones=1, calle=100, carrera=200),
    Edificio(cap_min=4, cap_max=22, cap_opt=39, numeroSalones=3, calle=70, carrera=125),
    Edificio(cap_min=9, cap_max=29, cap_opt=32, numeroSalones=7, calle=110, carrera=35),
    Edificio(cap_min=6, cap_max=21, cap_opt=36, numeroSalones=5, calle=220, carrera=65),
    Edificio(cap_min=8, cap_max=23, cap_opt=31, numeroSalones=0, calle=25, carrera=190),
    Edificio(cap_min=2, cap_max=14, cap_opt=26, numeroSalones=5, calle=75, carrera=170),
    Edificio(cap_min=3, cap_max=16, cap_opt=34, numeroSalones=7, calle=95, carrera=80),
    Edificio(cap_min=0, cap_max=11, cap_opt=27, numeroSalones=8, calle=120, carrera=30),
    Edificio(cap_min=5, cap_max=19, cap_opt=38, numeroSalones=4, calle=180, carrera=50),
    Edificio(cap_min=1, cap_max=17, cap_opt=35, numeroSalones=6, calle=40, carrera=100),
    Edificio(cap_min=7, cap_max=24, cap_opt=39, numeroSalones=9, calle=60, carrera=150),
    Edificio(cap_min=4, cap_max=20, cap_opt=31, numeroSalones=3, calle=85, carrera=220),
    Edificio(cap_min=9, cap_max=26, cap_opt=32, numeroSalones=2, calle=35, carrera=70),
    Edificio(cap_min=6, cap_max=18, cap_opt=33, numeroSalones=1, calle=195, carrera=15),
    Edificio(cap_min=8, cap_max=28, cap_opt=36, numeroSalones=0, calle=10, carrera=240),
    ]
    print(edificios)
    # luego insertamos los salones, al menos 5 por cada uno
if __name__=='__main__':
    run()