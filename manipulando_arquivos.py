"""
Manipulando arquivos textos:

"""
with open('texto.txt', 'w') as arquivo:
    escrita = input('Escreva uma frase: ')
    receb_arq = arquivo.write(escrita)

print('Arquivo criado com sucesso!')

