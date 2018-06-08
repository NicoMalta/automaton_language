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
    band = False
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
                        


    x = 0
    for gramatica in lista_gramatica:
        print("R",x,") " "Terminal: ",gramatica.terminales, "No Terminal: ",gramatica.noTerminales)
        x = x + 1  


print(setear_gramatica("A : id gg \n A : a \n A : A B c \n A : lambda \n B : b ccc"))
