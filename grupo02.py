import re

lista_gramatica = []

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

    lista_gramatica[0].follows.append("$")      
    for gram in lista_gramatica:
        no_terminal = gram.NoTerminal[0]
        agregarFo = False
        c = 0
        for gram_aux in lista_gramatica:
            i=2
            while i < len(gram_aux.reglaGramatica):
                if gram_aux.reglaGramatica[i] == no_terminal: 
                    if i+1 < len(gram_aux.reglaGramatica) and gram_aux.reglaGramatica[0] != gram_aux.reglaGramatica[i+1]:
                        if gram_aux.reglaGramatica[i+1].isupper() == True:
                            for aux in lista_gramatica:
                                if aux.reglaGramatica[0] == gram_aux.reglaGramatica[i+1]:
                                    if "lambda" in aux.firsts:
                                        agregarFo = True
                                        i += 1
                                        c += 1
                                        if i+1 == len(gram_aux.reglaGramatica):
                                            break
                                       
                    if i+1 == len(gram_aux.reglaGramatica):
                        for aux in lista_gramatica:
                            if aux.reglaGramatica[0] == gram_aux.reglaGramatica[0] or agregarFo == True:
                                for follows in aux.follows:
                                    if follows not in gram.follows:
                                        gram.follows.append(follows)
                                if agregarFo == True:
                                    while c > 0:
                                        i -= 1
                                        for aux in lista_gramatica:
                                            if aux.reglaGramatica[0] == gram_aux.reglaGramatica[i+1]:
                                                for firsts in aux.firsts:
                                                    if firsts not in gram.follows and firsts != "lambda":
                                                        gram.follows.append(firsts)                                          
                                        c -= 1
                                    agregarFo = False
                    elif gram_aux.reglaGramatica[i+1].isupper() == False:
                       gram.follows.append(gram_aux.reglaGramatica[i+1])
                    elif gram_aux.reglaGramatica[i+1].isupper() == True:
                        for aux in lista_gramatica:
                            if aux.reglaGramatica[0] == gram_aux.reglaGramatica[i+1]:
                                for firsts in aux.firsts:
                                    if firsts not in gram.follows and firsts != "lambda":
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
        print("R",contador,") " "\x1b[1;33m"+"Gramatica:"+'\033[0;m', mylist[contador], "\x1b[1;32m"+" First: "+'\033[0;m',gramatica.firsts, "\033[1;31m"" Folows:"+'\033[0;m', gramatica.follows, "\x1b[1;36m"" Selects: "+'\033[0;m', gramatica.selects)
        contador = contador + 1 
    
    tabla = []
    renglon = []
    
    renglon.append(' ')
    cantidadReglas = 0
    letrasReglas = []

    for gramatica in lista_gramatica:
        if gramatica.reglaGramatica[0] not in letrasReglas:
            letrasReglas.append(gramatica.reglaGramatica[0])
            cantidadReglas += 1
    
        for caracter in gramatica.Terminal:
            if caracter not in renglon and caracter != "lambda":
                renglon.append(caracter)

    renglon.append('$')
    tabla.append(renglon)
    
    posicion = 0
    regla = 0

    while regla < cantidadReglas:
        linea = []
        for terminal in renglon:
            linea.append(' ')
        linea[0] = letrasReglas[posicion]
        posicion += 1 
        tabla.append(linea)  
        regla += 1 
        
    for gramatica in lista_gramatica:
        for select in gramatica.selects:
            indiceA = 1
            while indiceA < len(tabla):
                if tabla[indiceA][0] == gramatica.reglaGramatica[0]:
                    break
                indiceA += 1
            
            indiceB = 1
            while indiceB < len(tabla[0]):
                if tabla[0][indiceB] == select:
                    break
                indiceB += 1
            

            for caracter in gramatica.reglaGramatica[2:len(gramatica.reglaGramatica)]:
                if caracter == 'lambda':
                    tabla[indiceA][indiceB] = '#'
                else:
                    tabla[indiceA][indiceB] += caracter
            
    
    print()
    print('The Table')
    print()
    for x in tabla:
        print(x)
    



"""print(setear_gramatica("A : b A \n A : a \n A : A B c \n A : lambda \n B : b"))"""
"""print(setear_gramatica("E : T G \n G : + T G \n G : - T G \n G : lambda \n T : F W \n W : * F W \n W : / F W \n W : lambda \n F : num \n F : ( E )"))"""
"""print(setear_gramatica("S : X Y Z \n X : a \n X : b \n X : lambda \n Y : a \n Y : d \n Y : lambda \n Z : e \n Z : f \n Z : lambda"))"""
"""print(setear_gramatica("E : T G \n G : + T G \n G : lambda \n T : F W \n W : * F W \n W : lambda \n F : ( E ) \n F : id"))"""
print(setear_gramatica("E : T W \n W : + T W \n W : - T W \n W : lambda \n T : F G \n G : * F G \n G : / F T \n G : lambda \n F : num \n F : ( E )"))