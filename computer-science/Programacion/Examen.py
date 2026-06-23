#Nombre Juan Fernando Alvis León
#Fecha 20/06/2026

#Pregunta 1
#Respuesta B

#Pregunta 2
#Respuesta C

#Pregunta 3
#Respuesta A


#Ejercicio 1
peliculas = [
 ["Intensamente", 25],
 ["Shrek", 40],
 ["Toy Story", 18],
 ["Coco", 35],
 ["Mario Bros", 40]
]

#a) Obtener la película o películas más vistas.
#b) Obtener la película o películas menos vistas.
#c) Calcular el promedio de visualizaciones.
#d) Mostrar las películas cuya cantidad de visualizaciones sea mayor al promedio

def mas_vi(A):
    C=[]
    maxim=0
    for i in range(len(A)):
        if A[i][1]>maxim:
            maxim=A[i][1]
    for i in range (len(A)):
        if maxim==A[i][1]:
            C.append(A[i][0])
        
    return C

def min_vi(A):
    C=[]
    minin=A[0][1]
    for i in range(len(A)):
        if minin>A[i][1]:
            minin=A[i][1]
    for i in range (len(A)):
        if minin==A[i][1]:
            C.append(A[i][0])
    return C

def prm_vi(A):
    prom=0
    for i in range(len(A)):
        prom+=A[i][1]
    return prom/len(A)

def may_prm(A):
    C=[]
    prom=prm_vi(A)
    for i in range(len(A)):
        if A[i][1]>=prom:
            C.append(A[i][0])
    return C
print("1) Obtener la película o películas más vistas. \n 2) Obtener la película o películas menos vistas. \n 3) Calcular el promedio de visualizaciones. \n 4) Mostrar las películas cuya cantidad de visualizaciones sea mayor al promedio. \n 0) Salir")
x=int(input("Ingrese lo que desee realizar: "))

while x!=0:
    if x==1:
        print("La(s) pelicula(s) más vista(s) es(son): ", mas_vi(peliculas))
    if x==2:
        print("La(s) pelicula(s) menos vista(s) es(son): ",min_vi(peliculas))
    if x==3:
        print("El promedio de las peliculas es: ",prm_vi(peliculas))
    if x==4:
        print("La(s) pelicula(s) mayor(es) al promedio es(son) ",may_prm(peliculas))
    print("1) Obtener la película o películas más vistas. \n 2) Obtener la película o películas menos vistas. \n 3) Calcular el promedio de visualizaciones. \n 4) Mostrar las películas cuya cantidad de visualizaciones sea mayor al promedio. \n 0) Salir")
    x=int(input("Ingrese lo que desee realizar: "))

print("-"*20)

#Ejercicio 2

def decimal_a_octal(A):
    if A<8:
        return str(A)
    else:
        return decimal_a_octal(A//8)+str(A%8)

print(decimal_a_octal(83))

print("-"*20)

#Ejercicio 3

palabra = "Python"

def ocultar_palabra(palabra):
    C=[]
    for i in range(len(palabra)):
       C.append("_")
    return C
oculto=ocultar_palabra(palabra)

def actualizar_palabra(palabra, oculto, letra):
    for i in range(len(palabra)):
        if letra==palabra[i]:
            oculto[i]=letra
    return oculto 

def gano(oculto):

    if "_" not in oculto:
        return True
    else:
        return False
print(*oculto)           
P=False
while P!=True:
    letra=input("Ingrese su letra: ")
    oculto = actualizar_palabra(palabra, oculto, letra)
    print(*oculto)
    P = gano(oculto)
print("¡Felicidades! Has descubierto la palabra")