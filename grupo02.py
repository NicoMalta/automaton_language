import re

lista_gramatica = []
tabla = []

class ReglaGramatica():

    def __init__(self):
        self.reglaGramatica = []
        self.NoTerminal = []
        self.Terminal = []
        self.follows = []
        self.firsts = []
        self.selects = []


def setear_gramatica(gramatica_str):
    Regla = ReglaGramatica()
    i = 0 
    char = ""
    while i < len(gramatica_str):
        char = gramatica_str[i]
        f = i + 1
        if f > len(gramatica_str):
            pass
        else:
            while f < len(gramatica_str) and gramatica_str[f] != " " and char != " ":
                char += gramatica_str[f]
                f = f + 1
            i = f
            if char == "\n":
                lista_gramatica.append(Regla)
                Regla = ReglaGramatica()
            elif char != " ":
                Regla.reglaGramatica.append(char)
                if char != ":":
                    if char.isupper() == True:
                        Regla.NoTerminal.append(char)
                    else:
                        Regla.Terminal.append(char)
                if i == len(gramatica_str):
                    lista_gramatica.append(Regla)


    for gram in lista_gramatica:
        i=0
        while gram.reglaGramatica[i] != ":":
            i += 1
        if gram.reglaGramatica[i+1].isupper() == False:
            gram.firsts.append(gram.reglaGramatica[i+1])
        else:
            char_terminal = gram.reglaGramatica[i+1]
            g = i + 1
            for aux in lista_gramatica:
                f = 0
                if aux.reglaGramatica[f] == char_terminal:
                    while aux.reglaGramatica[f] != ":":
                        f += 1
                    if aux.reglaGramatica[f+1].isupper() == False and aux.reglaGramatica[f+1] != "lambda":
                        if aux.reglaGramatica[f+1] not in gram.firsts:
                            gram.firsts.append(aux.reglaGramatica[f+1])
                    elif aux.reglaGramatica[f+1] == "lambda":
                        g += 1
                        if "lambda" not in gram.firsts:
                            gram.firsts.append("lambda")
                        if g < len(gram.reglaGramatica):
                            char_terminal = gram.reglaGramatica[g]

                        
    for gram in lista_gramatica:
        terminal = gram.NoTerminal[0]
        for gram_aux in lista_gramatica:
            i=2
            while i < len(gram_aux.reglaGramatica):
                if gram_aux.reglaGramatica[i] == terminal:
                    if i+1 == len(gram_aux.reglaGramatica):
                        if ("$") not in gram.follows:
                            gram.follows.append("$")
                    elif gram_aux.reglaGramatica[i+1].isupper() == False:
                        if (gram_aux.reglaGramatica[i+1]) not in gram.follows:
                            gram.follows.append(gram_aux.reglaGramatica[i+1])
                    else:
                        for aux in lista_gramatica:
                            if aux.reglaGramatica[0] == gram_aux.reglaGramatica[i+1]:
                                for firsts in aux.firsts:
                                    if firsts not in gram.follows:
                                        gram.follows.append(firsts)
                i += 1
        


    """SELECTS"""
    for gramatica in lista_gramatica:
        TodosLosFollows = False
        if "lambda" in gramatica.firsts:
            gramatica.selects += gramatica.follows
        else:
            gramatica.selects += gramatica.firsts

   
   
    x = 0
    for gramatica in lista_gramatica:
        print("R",x,") " "NoTerminal: ",gramatica.NoTerminal, "Terminal: ",gramatica.Terminal)
        x = x + 1  
    
    print("-  -  -  -  -  -  -  -  -  -  -  -  -  -   -  -  -  -  -  -  -  -  -  -")

    mylist = re.split("\n", gramatica_str)

    contador = 0
    for gramatica in lista_gramatica:
        print("R",contador,") " "\x1b[1;33m"+"Gramatica:"+'\033[0;m', mylist[contador], "\x1b[1;32m"+" First: "+'\033[0;m',gramatica.firsts, "\033[1;31m"" Follows:"+'\033[0;m', gramatica.follows, "\x1b[1;36m"" Selects: "+'\033[0;m', gramatica.selects)
        contador = contador + 1 

    tabla.append(["||"])
    for x in lista_gramatica:
        if x.Terminal not in tabla:
            tabla.append(x.Terminal)
    
    contador2 = 0
    while contador2 < len(lista_gramatica):
        if lista_gramatica[contador2].reglaGramatica[0] not in tabla[0]:
            tabla[0].append(lista_gramatica[contador2].reglaGramatica[0])
        contador2 = 1 + contador2
    

print(setear_gramatica("A : b A \n A : a \n A : B c \n A : lambda \n B : b"))

print()
print("\x1b[1;37m"+"Tabla:"+'\033[0;m')
for x in tabla:
    print(x)

"""print(setear_gramatica("S : X Y Z \n X : a \n X : b \n X : lambda \n Y : a \n Y : d \n Y : lambda \n Z : e \n Z : f \n Z : lambda"))"""
"""print(setear_gramatica("S : a S \n S : b \n S : T J \n S : lambda \n T : c T \n T : d \n J : j J \n J : k"))"""


""" ponemos lambda cuando no viene mas nada a la derecha"""

