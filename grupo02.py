seguir = True
lista_gramatica = []

class ReglaGramatica():
    reglaGramatica = []
    terminales = []
    noTerminales = []
    follows = []
    firsts = []
    selects = []



def setear_gramatica(gramatica_str):
    objeto = ReglaGramatica()
    objeto.reglaGramatica.append("A : b C")
    objeto.reglaGramatica.append("A : D")
    lista_gramatica.append(objeto.reglaGramatica)


    return lista_gramatica


while seguir == True:
    param_gramatica = input()
    print(setear_gramatica(param_gramatica))
    seguir_str = input("Seguir ") 
  
    if seguir_str.upper() == "SI":
        seguir = True
    else:
        seguir = False


'''stack = ['E']
look = yylex()

while stack:
    s = stack.pop()
    if s in NT:
        l = tale[(s, look)]
        l = l[::-1]
        sack.extend(1)
    elif s == look:
        look = yylex()
    else:
        print('Error')
if look == '$':
    print('OK')
else:
    print('Error')'''
