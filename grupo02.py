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
    while i < len(gramatica_str):
        if gramatica_str[i] == "\n" or i == len(gramatica_str)-1:
            lista_gramatica.append(Regla)
            Regla = ReglaGramatica()
            print(len(lista_gramatica))
        else:
            Regla.reglaGramatica.append(gramatica_str[i])
        
        char = gramatica_str[i]
        if char.isupper() == True:
            Regla.noTerminales.append(char)
        elif char != '' and char != ':' and char !=' ' and char !='\n':
            f = i+1
            while gramatica_str[f] !=' ' and f < len(gramatica_str):
                char += gramatica_str[f] 
                f += 1
            if f < len(gramatica_str):
                Regla.terminales.append(char)
                i += (f - i)
        i += 1
    input()

    



'''param_gramatica = input()'''
print(setear_gramatica("A : b A \n A : a \n A : A B c \n A : lambda \n B : b"))
