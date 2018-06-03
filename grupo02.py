seguir = True
lista_gramatica = []

class ReglaGramatica():
    reglaGramatica = []
    terminales = []
    noTerminales = []
    follows = []
    firsts = []
    selects = []
    EsLL1 = bool



def setear_gramatica(gramatica_str):
    Reglas = ReglaGramatica()
    



param_gramatica = input()
print(setear_gramatica(param_gramatica))



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
