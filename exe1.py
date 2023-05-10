#Crie uma lista alphabet contendo todas as letras do alfabeto em inglês em ordem alfabética. 
alfabeto = {1:["A"],2:["B"],3:["C"],4:["D"],5:["E"],6:["F"],7:["G"],8:["H"],9:["I"],10:["J"],11:["K"],12:["L"], 13:["M"],14:["N"], 15:["O"], 16:["P"], 17:["Q"],18:["R"], 19:["S"], 20:["T"], 21:["U"],22:["V"], 23:["W"], 24:["X"], 25:["Y"], 26:["Z"]}


#1
#for index in range(0, 26):
#    print(alfabeto[index])


#2
alfabeto_rotor = ["F", "O", "N", "C", "T", "P", "J", "W", "U", "S", "L", "G", "Z", "K", "H", "M", "R", "D", "E", "I", "A", "Y", "X", "B", "V", "Q"]


#3
from random import shuffle
shuffle(alfabeto_rotor)
#print("refletor = " + str(alfabeto_rotor))


#4
#.....buscado por letra(por enquanto)
def buscar():
    mensagem = list(input("Digite uma mensagem: "))
    input(mensagem)
    #for index, lista in alfabeto.items():
    #    if index == lista[0]:
    #        print("\nPosição:..................", index-1)
buscar()


def msg():
    mensagem = input("Digite uma mensagem: ")
    for indexm in mensagem:
        print(indexm)
      
#msg()