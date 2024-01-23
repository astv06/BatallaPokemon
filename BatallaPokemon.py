import math
import random

#El primer número de cada uno es la vida y el segundo la defensa
InfoJugador = [ 100 , 100 ]
InfoOponente = [ 100 , 100 ]

#Desición de movimiento por parte del jugador 
print("inicio de la batalla")
while InfoJugador[0] > 0 and InfoOponente[0] > 0:
    print("malisioso    placaje     ascuas")
    atJugador = input().lower()
    if atJugador == "malisioso" or atJugador == "placaje" or atJugador == "ascuas":
        if atJugador == "malisioso":
            if InfoJugador[1] > 10:
                InfoJugador[1] -= 10
                print("la defensa del oponente ahora es de " + str(InfoJugador[1]))
            else:
                print("el oponente tiene la defensa al minimo")
        elif atJugador == "placaje":
            InfoOponente[0] -= 35 * (100 / InfoOponente[1])
            print("el PS del oponente es de " + str(InfoOponente[0]))
        elif atJugador == "ascuas":
            InfoOponente[0] -= 20 * (100 / InfoOponente[1])
            print("el PS del oponente es de " + str(InfoOponente[0]))
    else:
        print("no posees el ataque " + str(atJugador))
    if InfoOponente[0] <= 0:
        print("ha ganado el jugador")
        quit()

#Desición del movimiento por parte del oponente 
    atOponente = random.randrange(1,4)
    if atOponente == 1:
        print("latigo")
        if InfoJugador[1] > 10: 
            InfoJugador[1] -= 10
            print("la defensa del jugador ahora es de " + str(InfoJugador[1]))
        else:
            print("el jugador tiene la defensa al minimo")
    elif atOponente == 2:
        print("placaje")
        InfoJugador[0] -= 35 * (100 / InfoJugador[1])
        print("el PS del jugador es de " + str(InfoJugador[0]))
    elif atOponente == 3:
        print("pistola de agua")
        InfoJugador[0] -= 20 * (100 / InfoJugador[1])
        print("el PS del jugador es de " + str(InfoJugador[0]))
    if InfoJugador[0] <= 0:
        print("el jugador ha perdido")
        quit()