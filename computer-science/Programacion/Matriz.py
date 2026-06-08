def Mostar_matriz(A):
    C=[]
    for j in range(len(A[0])):
        C.append(j)
    print("  ",C)
    for i in range(len(A)):
        print(i,A[i])

#def ponerer_en_matriz(A):


A=[[" ",2," "," ",3," "," ",4," "],[6," "," "," "," "," "," "," ",3],[" "," ",4," "," "," ",5," "," "],[" "," "," ",8," ",6," "," "," "],[8," "," "," ",1," "," "," ",6],[" "," "," ",7," ",5," "," "," "], 
                 [" "," ",7," "," "," ",6," "," "],[4," "," "," "," "," "," "," ",8],[" ",4," "," ",4," "," ",2," "]]
o=-1
while o != 0:
    print("\n1.- Mostrar matriz \n2.- Ingresar coordenadas \n0.- Salir")
    o = int(input("Ingrese lo que quiere hacer: "))
    if o==1:
        print(Mostar_matriz(A))
    elif o==2:
        z=int(input("Ingrese el que quiere poner (debe ser entero y no mayor a 9): "))
        x=int(input("Ingrese la coordenada x: "))
        y=int(input("Ingrese la coordenada y: "))
    elif o==0:
        print("Saliendo...")
    else:
        print("Opción no válida.")
