lista_gramatica = []

class ReglaGramatica():

    def __init__(self):
        self.reglaGramatica = []
        self.terminales = []
        self.noTerminales = []
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
                        Regla.terminales.append(char)
                    else:
                        Regla.noTerminales.append(char)
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
            for aux in lista_gramatica:
                f = 0
                if aux.reglaGramatica[f] == char_terminal:
                    while aux.reglaGramatica[f] != ":":
                        f += 1
                    if aux.reglaGramatica[f+1].isupper() == False:
                        gram.firsts.append(aux.reglaGramatica[f+1])
                        
    for gram in lista_gramatica:
        terminal = gram.terminales[0]
        for gram_aux in lista_gramatica:
            i=2
            while i < len(gram_aux.reglaGramatica):
                if gram_aux.reglaGramatica[i] == terminal:
                    if i+1 == len(gram_aux.reglaGramatica):
                        gram.follows.append("$")
                    elif gram_aux.reglaGramatica[i+1].isupper() == False:
                        gram.follows.append(gram_aux.reglaGramatica[i+1])
                    else:
                        for aux in lista_gramatica:
                            if aux.reglaGramatica[0] == gram_aux.reglaGramatica[i+1]:
                                for firsts in aux.firsts:
                                    gram.follows.append(firsts)
                i += 1
        

    x = 0
    for gramatica in lista_gramatica:
        print("R",x,") " "Terminal: ",gramatica.terminales, "No Terminal: ",gramatica.noTerminales)
        x = x + 1  


"""print(setear_gramatica("A : b A \n A : a \n A : A B c \n A : lambda \n B : b c"))"""
print(setear_gramatica("S : X Y Z \n X : a \n X : b \n X : lambda \n Y : a \n Y : d \n Y : lambda \n Z : e \n Z : f \n Z : lambda"))