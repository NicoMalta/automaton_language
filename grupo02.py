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
        if gramatica_str[i] == "\n" or i == len(gramatica_str):
            lista_gramatica.append(Regla)
            Regla = ReglaGramatica()
        else:
            if band == False and gramatica_str[i] != " ":
                Regla.reglaGramatica.append(gramatica_str[i])
            elif gramatica_str[i] != " ":
                Regla.reglaGramatica.append(char)
                band = False
      
        char = gramatica_str[i]
        if char.isupper() == True:
            Regla.noTerminales.append(char)
        elif char != '' and char != ':' and char !=' ' and char !='\n':
            f = i+1
            if f == len(gramatica_str) and gramatica_str[f-2] != " ":
                char += gramatica_str[f] 
            elif f != len(gramatica_str):
                while gramatica_str[f] != ' ':
                    char += gramatica_str[f] 
                    f += 1
                    band = True
            if f <= len(gramatica_str):
                Regla.terminales.append(char)
                i += ((f-1) - i-1)
                if f == len(gramatica_str):
                    lista_gramatica.append(Regla)
                    Regla = ReglaGramatica()
                
        i += 1

    for gram in lista_gramatica:
        i=0
        
        while gram.reglaGramatica[i] != ":":
            i += 1
        if gram.reglaGramatica[i+1].isupper() == False:
            gram.firsts.append(gram.reglaGramatica[i+1])
        else:
            char_terminal = gram.reglaGramatica[i+1]
            f = 0
            for aux in lista_gramatica:
                if aux.reglaGramatica[f] == char_terminal:
                    while aux.reglaGramatica[f] != ":":
                        f += 1
                    if aux.reglaGramatica[f+1].isupper() == False:
                        gram.firsts.append(aux.reglaGramatica[f+1])
                        break


    x = 0
    for gramatica in lista_gramatica:
        print("R",x,") " "Terminal: ",gramatica.terminales, "No Terminal: ",gramatica.noTerminales)
        x = x + 1  


print(setear_gramatica("A : b A \n A : B \n A : A B c \n A : lambda \n B : c d"))
