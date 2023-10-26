# Generación de datos para N
import random


N = 250
print('N <- 250')
for i in range(N):
    id_N = random.randint(10000, 99999)
    x_N = random.randint(0, 250)
    y_N = random.randint(0, 250)
    loc_N = random.choice(['Norte', 'Centro', 'Sur', 'Oriente', 'Occidente'])
    print(f"{id_N}, {x_N}, {y_N}, {loc_N}")

# Generación de datos para M
M = 20
ids_edificios = []
print('M <- 20')
for i in range(M):
    id_M = random.randint(1000, 9999)
    x_M = random.randint(0, 250)
    y_M = random.randint(0, 250)
    loc_M = random.choice(['Norte', 'Centro', 'Sur', 'Oriente', 'Occidente'])
    print(f"{id_M}, {x_M}, {y_M}, {loc_M}")
    ids_edificios.append(id_M)

# Generación de datos para K
K = 50
print('K <- 50')
for i in range(K):
    id_K = random.randint(100, 999)
    id_M = random.choice(ids_edificios)
    piso_K = random.randint(0, 10)
    max_K = random.randint(0, 40)
    opt_K = random.randint(0, 30)
    min_K = random.randint(0, 10)
    print(f"{id_K}, {id_M}, {piso_K}, {max_K}, {opt_K}, {min_K}")
