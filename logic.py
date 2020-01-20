import re

code_file = open('InputProg.c','r')
builtin_file = open('builtin.txt', 'r')
keywords_file = open('keywords.txt', 'r')
operators_file = open('operators.txt', 'r')
special_file = open('special.txt', 'r')

code = code_file.read()
builtin = builtin_file.read()
keywords = keywords_file.read()
operators = operators_file.read()
special = special_file.read()

count = 0
code_lines = code.split('\n')
builtin = builtin.split('\n')
keywords = keywords.split('\n')
operators = operators.split('\n')
special = special.split('\n')
sym = list()

for code_line in code_lines:
    count += 1
    colon = False

    if code_line[-1] == ';':
        colon = True
        code_line = code_line[:-1] + ' ' + ';'

    if '(' in code_line or ')' in code_line:
        code_line = code_line[:code_line.index('(')]
        if colon == True:
            code_line += ' ;'
    
    code_tokens = code_line.split(' ')
    # print(code_tokens)
    
    for code_token in code_tokens:
        if code_token[-1] == ',':
            code_token = code_token[:-1] 
        if code_token in builtin:
            print('Bfun#{}'.format(builtin.index(code_token) +1), end=' ')
        elif code_token in keywords:
            print('keyword#{}'.format(keywords.index(code_token)+1), end=' ')
        elif code_token in operators:
            print('oper#{}'.format(operators.index(code_token)+1), end=' ')
        elif code_token in special:
            print('spl#{}'.format(special.index(code_token)+1), end=' ')
        else:
            if code_token in sym:
                print('sym#{}'.format(sym.index(code_token)+1), end=' ')
            else:
                sym.append(code_token)
                print('sym#{}'.format(len(sym) - 1),  end=' ')

    print('\n\n')
print(sym)
string = '\n'.join(sym)
print(string)

symbols_file = open("symbols.txt","w+")
symbols_file.write(string)


code_file.close()
builtin_file.close()
keywords_file.close()
operators_file.close()
special_file.close()
symbols_file.close()
