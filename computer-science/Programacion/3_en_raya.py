A=[[" "," "," "],[" "," "," "],[" "," "," "]]
def mostra(A):
    C=[]
    K=len(A[0])
    for i in range(K):
     C.append(i)
    print(" "*2,C[0:])
    for i in range(len(A)):
        print(i,A[i])
A = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

def agregar(A, x, y, k):
    A[y][x] = k
    return "Hecho"
        
z=-1
while z!=0:
    if z==1:
     mostra(A)
    if z==2:
     k=input("Ingrese su x u o:") 
     x=int(input("Agregue su variable x: "))
     y=int(input("Agregue su variable y: "))
     print(agregar(A,x,y,k))
    z=int(input("\n 1.-Mostar el tres en raya \n 2.-Ingresar el número \nIngrese loo que desea hacer: "))
    if z==0:
     print("Saliendo...")
