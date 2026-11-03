mapa = [
    [0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 1, 1, 0, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 1, 1, 0, 1, 0],
    [1, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 0, 1, 1, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 1, 1, 0],
    [0, 1, 0, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 0],
    [1, 1, 0, 0, 1, 0, 0, 0, 0]
]

filas = len(mapa)


def contarCaminos(f, c):

    
    if f >= filas or c >= filas:
        return 0

 
    if mapa[f][c] == 1:
        return 0


    if f == filas - 1 and c == filas - 1:
        return 1


    if f == filas - 1:
        return contarCaminos(f, c + 1) + 0


    elif c == filas - 1:
        return 0 + contarCaminos(f + 1, c)


    else:
        return contarCaminos(f, c + 1) + contarCaminos(f + 1, c)



print("*********************************************")
print("  BIENVENIDO AL EXPLORADOR DE RUTAS EXTREMAS ")
print("*********************************************\n")

print("Cargando el terreno de juego...")
print("(Recuerda: 0 es camino seguro, 1 es zona bloqueada)\n")

for f in mapa:
    print(f)

print("\nDesplegando al explorador en la casilla (0,0)...")
caminos = contarCaminos(0, 0)

print(f"\n¡Misión cumplida! El explorador tiene {caminos} maneras de llegar a la meta sin chocar.")