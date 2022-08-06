arquivo = open('documentos/dados2.txt', 'r')

conteudo = arquivo.readlines()
for lista in conteudo:
    print(repr(lista))

arquivo.close()
