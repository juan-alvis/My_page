persona=("Carlos", 28, "Madrid")
nombre, edad, ciudad = persona
print(nombre,edad,ciudad)

numeros = (10, 20, 30, 40, 50, 60, 70, 80)
print(numeros[0],numeros[-1])
sub_tupla=numeros[2:6]
print(sub_tupla)

colores = ("rojo", "verde", "azul", "verde", "amarillo")
print("El verde aparece:", colores.count("verde"), "veces.")

print("El azul está en el índice:", colores.index("azul"))

if "morado" not in colores:
    print("El color morado no se encuentra en la tupla.")

frutas = ("manzana", "pera", "plátano")

# Convertir a lista
lista_frutas = list(frutas)
print(frutas)
# Modificar la lista
lista_frutas.append("naranja")
lista_frutas[1] = "mango"

# Convertir de vuelta a tupla
frutas_modificadas = tuple(lista_frutas)

print(frutas_modificadas)  # Resultado: ('manzana', 'mango', 'plátano', 'naranja')

t1=(1, 2, 3)
t2=(4, 5, 6)

t_combi=t1+t2
t_repetida=t1*3
print("Combinada", t_combi)
print("Repetida", t_repetida)

print("-"*20)

def calcular_figura(A):
    return A**2,4*A
resultado=calcular_figura(5)
print(resultado)

print("-"*20)

matriz = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
jola=matriz[1][1]
hola=matriz[-1][-1]
for i in matriz:
    print(i)
print(jola, hola)

print("-"*20)

no_es_tupla=(10)
si_es_tupla=(10,)
print(type(no_es_tupla))
print(type(si_es_tupla))

print("-"*20)

valores = (40, 10, 50, 20, 30)
C=[]