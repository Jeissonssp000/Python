import random
import collections
import copy

PALOS = ['Espada', 'Corazón', 'Pica', 'Trébol']
VALORES = ['As', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

def crear_baraja():
    barajas = []

    for palo in PALOS:
        for valor in VALORES:
            barajas.append((palo, valor))

    return barajas

def obtener_mano(baraja, tamano_mano):
    return random.sample(baraja, tamano_mano)
    
def hallar_probabilidad_corrida(manos, tamano_mano, cantidad_simulaciones):
    corridas = 0
    for mano in manos:
        valores = []

        # Obtener valor numerico de cada carta
        for carta in mano:
            try:
                valor = int(carta[1])
            except ValueError:
                switcher = {
                    'As': 1,
                    'J': 11,
                    'Q': 12,
                    'K': 13
                }
                valor = switcher[carta[1]]                
            valores.append(valor)
        
        valores.sort()

        # Comprobar si es una corrida
        anterior = valores[0]
        for valor in valores[1:]:
            esCorrida = (anterior + 1) == valor

            if not esCorrida:
                break
            else:
                anterior = copy.copy(valor)
        
        # Contar si es corrida
        if esCorrida:
            corridas += 1
    
    probabilidad = corridas / cantidad_simulaciones
    print(f'La probablilidad de tener una corrida de {tamano_mano} cartas es {probabilidad}')


        

def main(tamano_mano, cantidad_simulaciones):
    baraja = crear_baraja()

    manos = []
    for _ in range(cantidad_simulaciones):
        mano = obtener_mano(baraja, tamano_mano)
        manos.append(mano)

    hallar_probabilidad_corrida(manos, tamano_mano, cantidad_simulaciones)

if __name__ == '__main__':
    tamano_mano = int(input('Cuántas cartas tendrá cada mano: '))
    cantidad_simulaciones = int(input('Cuántas simulaciones debo correr? '))

    main(tamano_mano, cantidad_simulaciones)