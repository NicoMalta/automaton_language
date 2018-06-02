stack = ['E']
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
    print('Error')