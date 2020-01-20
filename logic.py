import re

code_file = open('c_prog.c','r')
built_in_file = open('built_in.txt', 'r')
keywords_file = open('keywords.txt', 'r')
operators_file = open('operators.txt', 'r')
special_symbol_file = open('special_symbol.txt', 'r')

code = code_file.read()
built_in = built_in_file.read()
keywords = keywords_file.read()
operators = operators_file.read()
special_symbol = special_symbol_file.read()

count = 0
code_lines = code.split('\n')
built_in = built_in.split('\n')
keywords = keywords.split('\n')
operators = operators.split('\n')
special_symbol = special_symbol.split('\n')
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
    
    for code_token in code_tokens:
        if code_token[-1] == ',':
            comma = True
        if code_token in built_in:
            print('Bfun#{}'.format(built_in.index(code_token) +1), end=' ')
        elif code_token in keywords:
            print('keyword#{}'.format(keywords.index(code_token)+1), end=' ')
        elif code_token in operators:
            print('oper#{}'.format(operators.index(code_token)+1), end=' ')
        elif code_token in special_symbol:
            print('spl#{}'.format(special_symbol.index(code_token)+1), end=' ')
        else:
            if code_token in sym:
                print('sym#{}'.format(sym.index(code_token)+1), end=' ')
            else:
                sym.append(code_token)
                print('sym#{}'.format(len(sym) - 1),  end=' ')

    print('\n\n')

code_file.close()
built_in_file.close()
keywords_file.close()
operators_file.close()
special_symbol_file.close()
