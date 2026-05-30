def matri_transpuest(A):#Ejercicio 2
    C=[]
    for i in range (len(A)):
        C.append([])
    print(C)

    nuevo_val=0
    for i in range (len(A)):
        for j in range (len(A)):
            nuevo_val=A[j][i] #Si se cambia estos indices se obtierne la matriz transpuesta
            C[i].append(nuevo_val)
    print(C)

matri_transpuest([[1,2,3],[4,5,6],[7,8,9]])

print("_"*20)

def identi(A): #Ejercicio 5
    for i in range(len(A)):
         for j in range (len(A)):
             if i==j and A[i][j]!=1: #Esto indica que si el elemento de la diagonal no es 1, entonces no es una matriz identidad
                 return False
             elif i!=j and A[i][j]!=0:#Esto indica que si el elemento fuera de la diagonal no es 0, entonces no es una matriz identidad
                 return False
    return True
print(identi([[1,0,0],[0,1,0],[0,0,1]]))
print(identi([[1,1,10],[0,1,0],[0,0,1]]))

print("_"*20)

def suma_bords(A):#Ejercicio 6
    suma=0
    for i in range(len(A)):
        for j in range(len(A)):
            if i==j:
              continue
            elif i!=j:
                suma+=A[i][j]
    return suma
print(suma_bords([[1,2,3],[4,5,6],[7,8,9]]))

print("_"*20)

def may_prom(A):#Ejercicio 7
    mayor=A[0][0]
    menor=A[0][0]
    for i in range(len(A)):
        for j in range (len(A)):
            if A[i][j]>mayor:
                mayor=A[i][j]
            if A[i][j]<menor:
                menor=A[i][j]
    print("El numero mas grande en la matriz" , A , "es:",mayor ,"y el menor fue:",menor)

may_prom([[1,2,3],[4,5,6],[7,8,20]])

print("_"*20)

