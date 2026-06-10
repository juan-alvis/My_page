A=[[1,2,3],[1,4,3],[3,4,5]]
def suma_dg_princi(A):
    suma=0
    for i in range(len(A)):
        for j in range(len(A[0])):
            if i==j:
                suma+=A[i][j]
    return suma
print("-"*5)

def suma_dp_efici(A):
    suma=0
    for i in range(len(A)):
        suma+=A[i][i]
    return(suma)

print(suma_dp_efici(A))
print(suma_dg_princi(A))