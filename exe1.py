#1
alfabeto = {1:["A"],2:["B"],3:["C"],4:["D"],5:["E"],6:["F"],7:["G"],8:["H"],9:["I"],10:["J"],11:["K"],12:["L"], 13:["M"],14:["N"], 15:["O"], 16:["P"], 17:["Q"],18:["R"], 19:["S"], 20:["T"], 21:["U"],22:["V"], 23:["W"], 24:["X"], 25:["Y"], 26:["Z"]}
#for index in range(0, 26):
#    print(alfabeto[index])

#2
alfabeto_rotor = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

#3
from random import shuffle
shuffle(alfabeto_rotor)
#print("rotor = " + str(alfabeto_rotor))

#4 - (A)
def buscar():
    mensagem = list(input("Digite uma mensagem: "))
    for index in mensagem:
        for indext, lista in alfabeto.items():
            if index == lista[0]:
                print("Posição:..................", indext-1, "(", lista, ")")
#buscar()

#4 - B
def buscar_two():
    mensagem = list(input("Digite uma mensagem: "))
    for index in mensagem:
        for indext, lista in alfabeto.items():
            if index == lista[0]:
                    print("Posição:..................", indext-1, "(", lista, ")")
                    i = indext
                    for indexr in alfabeto_rotor[i]:
                        print("Posição alterada:..................", i, "(", indexr, ")")
#buscar_two()

#4 - C
def buscar_three():
    mensagem = list(input("Digite uma mensagem: "))
    for index in mensagem:
        for indext, lista in alfabeto.items():
            if index == lista[0]:
                    #print("Posição:..................", indext-1, "(", lista, ")")
                    i = indext
                    for indexr in alfabeto_rotor[i]:
                        #print("Posição alterada:..................", i, "(", indexr, ")")
                        shuffle(alfabeto_rotor)
                        #print("retrato = " + str(alfabeto_rotor))
                        for indexthree in alfabeto_rotor[i]:
                            print("Posição alterada(NOVAMENTE):..................", indext, "(", indexthree, ")")
#buscar_three()

#4 - D
def mensagem_cifrada():
    mensagem = list(input("Digite uma mensagem: "))
    for index in mensagem:
        for indext, lista in alfabeto.items():
            if index == lista[0]:
                    #print("Posição:..................", indext-1, "(", lista, ")")
                    i = indext
                    for indexr in alfabeto_rotor[i]:
                        #print("Posição alterada:..................", i, "(", indexr, ")")
                        shuffle(alfabeto_rotor)
                        #print("retrato = " + str(alfabeto_rotor))
                        for indexthree in alfabeto_rotor[i]:
                            #print("Posição alterada(NOVAMENTE):..................", indext, "(", indexthree, ")")
                            print(indexthree)

#5
#mensagem_cifrada()


#6 - Processo ao contrario
def desifrar():
    mensagem = list(input("Digite uma mensagem: "))
    for index in mensagem:
        for indext, lista in alfabeto.items():
            if index == lista[0]:
                    print("\nPosição inicial:..................", indext-1, "(", lista, ")")
                    i = indext
                    for indexr in alfabeto_rotor[i]:
                        print("Posição alterada:..................", i, "(", indexr, ")")
                        shuffle(alfabeto_rotor)
                        #print("retrato = " + str(alfabeto_rotor))
                        for indexthree in alfabeto_rotor[i]:
                            print("Posição alterada(NOVAMENTE):..................", indext, "(", indexthree, ")")
                            print("\nMensagem cifrada: ", indexthree)
    for index in mensagem:
        for indexthree in alfabeto_rotor[i]:
            print("\nMSG CIFRADA:..................", indext, "(", indexthree, ")")
            for indexr in alfabeto_rotor[i]:
                print("MSG QUASE DECIFRADA:..................", i, "(", indexr, ")")
                shuffle(alfabeto_rotor)
                #print("retrato = " + str(alfabeto_rotor))
                for indext, lista in alfabeto.items():
                    if index == lista[0]:
                        print("MSG DECIFRADA:..................", indext-1, "(", lista, ")")
                        print("\nMensagem decifrada: ", lista)

#7
desifrar()


