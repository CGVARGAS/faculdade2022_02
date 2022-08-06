import os

arquivo1 = open('texto.txt', 'r')
print(f'Caminho relativo -> {os.path.relpath(arquivo1.name)}')  # 'relpath' -> Imprime o caminho relativo.
print(f'Nome do arquivo: {arquivo1.name}')
print(f'Modo do arquivo: {arquivo1.mode}')
arquivo1.close()  # O arquivo foi fechado desta forma, pois não foi utilizado a instrução with.
print(f'Arquivo fechado? {arquivo1.closed}\n')

arquivo2 = open('documentos/dados2.txt')
print(f'Caminho absoluto -> {os.path.abspath(arquivo2.name)}')  # 'abspath' -> Imprime o caminho absoluto.
print(f'Nome do arquivo: {arquivo2.name}')
print(f'Modo do arquivo: {arquivo2.mode}')
print(f'Arquivo fechado? {arquivo2.closed}')

