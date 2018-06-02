seguir = True
gramatica = []

def setear_gramatica(cadena):
    i = 0
    terminal = []
    no_terminal = []
    while i < len(cadena):
        f = i
        char = ''
        while cadena[f] != ' ':
            char += cadena[f]
            f += 1
        if char.isupper() == True:
            no_terminal.append(char)
        elif char != ' ' and char != ':' and char != '':
            terminal.append(char)
        i += 1
    gramatica.append(cadena)
    gramatica.append(no_terminal)
    gramatica.append(terminal)
    return gramatica

while seguir == True:
    param_cadena = input()
    print(setear_gramatica(param_cadena))
    seguir_str = input("Seguir ") 
  
    if seguir_str.upper() == "SI":
        seguir = True
    else:
        seguir = False