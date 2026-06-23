#Ejercios matrices y funciones

#Ejercicio 1
A=[[1,2,3],[-1,2,6],[1,2,5]]
def suma_total(A):
    sumat=0
    for i in range(len(A)):
        for j in range(len(A[0])):
           sumat+=A[i][j]
    return sumat
print(suma_total(A)) 

#Ejercicio 2

def num_par(A):
    par=0
    for i in range(len(A)):
        for j in range(len(A[0])):
            if A[i][j]%2==0:
                par+=1
    return par
print(num_par(A))

#Ejercicio 3

def max(A):
    max=A[0][0]
    for i in range(len(A)):
        for j in range(len(A[0])):
            if A[i][j]>max:
                max=A[i][j]
    return max
print(max(A)) 

#Ejercicio 4

def min(A):
    min=A[0][0]
    for i in range(len(A)):
        for j in range(len(A)):
            if A[i][j]<min:
                min=A[i][j]
    return min
print(min(A))

#Ejercicio 5
def prom(A):
    suma=0
    prom=0
    for i in range(len(A)):
        for j in range(len(A[0])):
            suma+=A[i][j]
            prom+=1
    return suma/prom            
print(prom(A))

#Ejercicio 6
def suma_fil(A,b):
    suma=0
    for j in range(len(A[b])):
        suma+=A[b][j]
    return suma
print(suma_fil(A,1))

#Ejercicio 7
def suma_col(A,b):
    suma=0
    for i in range(len(A)):
        suma+=A[i][b]
    return suma
print(suma_col(A,1))

#Ejercicio 8
def fil_may(A):
    max_fila=0
    indice=0
    for i in range(len(A)):
        max=0  
        for j in range(len(A[0])):
            max+=A[i][j]
        if max>max_fila:
                max_fila=max
                indice=i
    return max_fila, indice
print(fil_may(A))

#Ejercicio 9
def col_men(A):
    colu_men=float('inf')
    indice=0
    for j in range(len(A[0])):
        suma_col=0
        for i in range(len(A)):
            suma_col+=A[i][j]
        if suma_col<colu_men:
                colu_men=suma_col
                indice=j
    return colu_men, indice
print(col_men(A))

#Ejercicio 10

def num_men(A):
    num_men=0
    for i in range(len(A)):
        for j in range(len(A[0])):
            if A[i][j]<0:
                num_men+=1
    return num_men
print(num_men(A))

#Ejercicio 11
# Configuración del tablero
tablero = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
FILAS = len(tablero)
COLUMNAS = len(tablero[0])

# --- Funciones de movimiento ---

def moverDerecha(posicion):
    fila, columna = posicion[0], posicion[1]
    if columna < COLUMNAS - 1:
        columna += 1
        print("\n-> Te moviste a la derecha.")
    else:
        print("\n¡Muro! No puedes moverte más a la derecha.")
    return [fila, columna]

def moverIzquierda(posicion):
    fila, columna = posicion[0], posicion[1]
    if columna > 0:
        columna -= 1
        print("\n-> Te moviste a la izquierda.")
    else:
        print("\n¡Muro! No puedes moverte más a la izquierda.")
    return [fila, columna]

def moverAbajo(posicion):
    fila, columna = posicion[0], posicion[1]
    if fila < FILAS - 1:
        fila += 1
        print("\n-> Te moviste hacia abajo.")
    else:
        print("\n¡Muro! No puedes moverte más abajo.")
    return [fila, columna]

def moverArriba(posicion):
    fila, columna = posicion[0], posicion[1]
    if fila > 0:
        fila -= 1
        print("\n-> Te moviste hacia arriba.")
    else:
        print("\n¡Muro! No puedes moverte más arriba.")
    return [fila, columna]


# --- Menú interactivo ---

posicion_jugador = [0, 0]  # Posición inicial del jugador

while True:
    print("\n" + "="*30)
    print(f" Posición actual del jugador: {posicion_jugador}")
    print("="*30)
    print("1. Mover Arriba  (W)")
    print("2. Mover Abajo   (S)")
    print("3. Mover Izquierda (A)")
    print("4. Mover Derecha (D)")
    print("5. Salir del juego")
    print("="*30)
    
    opcion = input("Elige una opción (número o letra): ").upper()
    
    if opcion == "1" or opcion == "W":
        posicion_jugador = moverArriba(posicion_jugador)
    elif opcion == "2" or opcion == "S":
        posicion_jugador = moverAbajo(posicion_jugador)
    elif opcion == "3" or opcion == "A":
        posicion_jugador = moverIzquierda(posicion_jugador)
    elif opcion == "4" or opcion == "D":
        posicion_jugador = moverDerecha(posicion_jugador)
    elif opcion == "5" or opcion == "SALIR":
        print("\n¡Gracias por jugar! Fin de la partida.")
        break  # Rompe el bucle 'while' y termina el programa
    else:
        print("\nOpción no válida. Intenta de nuevo.")

