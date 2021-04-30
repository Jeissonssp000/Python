import random

PALOS = ['♠','❤','🔶','🍀']
VALORES = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']

def crear_baraja():
    barajas = []
    for palo in PALOS:
        for valor in VALORES:
            barajas.append((valor, palo))

    return barajas

def obtener_mano(barajas, tamano_mano):
    mano= random.sample(barajas, tamano_mano)

    return mano

def main(tamano_mano, intentos)
    barajas = crear_baraja()
    manos = []
    for _ in range(intentos):
        mano = obtener_mano(barajas, tamano_mano)
        manos.append(mano)

if __name__ == '__main__':
    tamano_mano = int(input('De cuantas barajas sera la mano: '))
    intentos = int(input('Cuantos intentos para calcular la probabilidad: '))
    
    main(tamano_mano, intentos)
