import random

# Tu lista de palabras
palabras_dificiles = ["electrodomestico","esternocleidomastoideo",
                      "murcielago","xilofono","zanahoria","arquelogia",
                      "subterraneo","paralelepipedo","psicologia","algoritmo",]
# Python elige una por ti
palabra_secreta = random.choice(palabras_dificiles)


print("*"*5,"JUEGO DEL AHORCADO","*"*5)
p=int(input("Ingrese 1 para iniciar o 0 para Salir: "))
if p==0:
    print("Saliendo..")
elif p==1:
    Ahorcado=4
    manu=1

    print("_"*len(palabra_secreta))
    print(palabra_secreta)
    menu=input("Ingrese la letra de la palabra \n Ingrese Salir si desea terminar el juego:\n") 
    while manu!=0:
        if menu == "Salir" or menu == "salir":
            print("Saliendo...")
            break
        elif Ahorcado==0:
            print("Vidas acabadas \n Cortando el juego...")
            break
        if len(menu)>1:
            print("Solo puede poner una letra")
        elif menu in palabra_secreta:
            print(f"\n¡Correcto!, Usted tiene: {Ahorcado+1} vidas ")
        elif menu not in palabra_secreta:
            Ahorcado-=1
            print(f"\n¡Error!, menos una vida Usted tiene: {Ahorcado+1} vidas " )
        print("_"*len(palabra_secreta))
        menu=input("Ingrese la letra de la palabra \n Ingrese Salir si desea terminar el juego:\n")    
        