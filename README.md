# Manipulação de Dados em Arquivos com Python
## Leitura (read())

![piton]

[piton]: piton.jpg 

---

### Operações básicas de manipulação de arquivos:

_A primeira operação básica é **abrir arquivo**._

_Para abrir um arquivo, o Python disponibiliza a função interna chamada "open". Essa função está disponível globalmente, 
ou seja, não é preciso importá-la._

_A função **open** retorna um objeto do tipo arquivo. Sua forma de utilização tem a seguinte sintaxe:_

```doctest
with open('texto.txt', 'w') as arquivo:
    receb.arquivo = arquivo.write('Texto a ser escrito!')
```

_Ao utilizar desta função o Python criará um arquivo ".txt" na pasta atual._

>_A instrução **"with"** é utilizada para realizar de forma simples e garantida o encerramento dos recursos abertos._

>_A sintaxe **"as"** serve para criar um **"aliás"** para um módulo que tenha um nome muito grande, dando a opção de 
> criar um nome mais significativo e de fácil memorização._    

_Se houver a necessidade de impressão dos caminhos absolutos ou relativos veja o exemplo abaixo:_

```doctest
import os

arquivo1 = open('texto.txt', 'r')
print(os.path.relpath(arquivo1.name))  # 'relpath' -> Imprime o caminho relativo.
```

```doctest
import os

arquivo2 = open('documentos/dados2.txt')
print(os.path.abspath(arquivo2.name))  # 'abspath' -> Imprime o caminho absoluto.
```
>_**Obs.** Para fechar os arquivos abertos sem utilizar a instrução **with** usa-se o: "nome_do_arquivo.close()"._

```doctest
import os

arquivo1 = open('texto.txt', 'r')
print(f'Caminho relativo -> {os.path.relpath(arquivo1.name)}')
arquivo1.close() 
print(f'Arquivo fechado? {arquivo1.closed}\n')

```

>_**Obs.** Após a utilização do **.close()** utiliza-se do "print(f'Arquivo fechado? {arquivo1.closed}\n')" para verificar
> se o arquivo encontra-se fechado ou aberto. A resposta será impressa no console como: "False" ou "True"._

---

### Modos de acesso ao arquivo:

_Ao abrirmos um arquivo precisamos informar ao Python qual modo de acesso, sendo assim, cada modo é representado por 
uma "string"._

| String | Função |
|--------|--------|
| 'w'    | write  |
| 'r'    | read   |
| 'a'    | append |    

_Acima temos os modos principais, lembrando que o modo padrão é o de leitura ('r')!_ 

_Segue link do site onde consta mais detalhes quanto aos modos utilizados:_

[Modos da função open.](https://docs.python.org/3/library/functions.html#open)

---

### Lendo o conteúdo do arquivo:

Métodos para leitura do conteúdo de arquivo texto:

| Método      | Função                                                                                                                           |
|-------------|----------------------------------------------------------------------------------------------------------------------------------|
| read()      | Retorna todo o conteúdo de um arquivo como uma única string.                                                                     |
| readline()  | Retorna uma linha de um arquivo, incluindo os caracteres de final de linha (\n ou \r\n), e avança o cursor para a próxima linha. |
| readlines() | Retorna uma lista onde cada item da lista é uma linha do arquivo.                                                                |

>_**Obs.** Para mostrar o conteúdo real contido na variável basta utilizar a função -> "print(repr(variável))"._ 

>_**Obs.** Além dos três métodos apresentados anteriormente, os objetos do tipo arquivo são **iteráveis**. Com isso, podemos 
> utilizar o laço **"for"** diretamente sobre os objetos desse tipo._
 
### Iterando sobre um arquivo texto:

```doctest
arquivo = open('dados.txt', 'r')

print('Iterando sobre o arquivo')
for linha in arquivo:
   print(repr(linha))

arquivo.close()
```

>**Dica:**
> 
>_1 — Quando precisamos abrir um arquivo muito grande, é inviável utilizar os métodos read e readlines, pois eles retornam
> todo o conteúdo do arquivo de uma só vez, seja na forma de 'string', seja na forma de lista. Isso pode consumir todos os
> recursos do computador, travando seu programa._
> 
>_Nesses casos, precisamos chamar o método readline inúmeras vezes até o final do arquivo ou iterar diretamente 
> sobre o objeto do tipo arquivo._

>2 - Após utilizar qualquer um dos métodos para leitura dos arquivos apresentados anteriormente, não podemos utilizá-los 
> novamente. Isso acontece porque o cursor estará posicionado ao final do arquivo, e as chamadas aos métodos read, 
> readline ou readlines retornarão vazias.

Para situações em que precisamos ler o conteúdo de um arquivo mais de uma vez, temos duas opções:

1) Fechar e abrir novamente o arquivo.

2) Utilizar o método seek(n), passando como argumento o número da linha onde desejamos posicionar o cursor. 
A chamada seek(0) retorna o cursor para o início do arquivo.

#### Para ler todo arquivo é: seek(-1)

_O script8.py demonstra na prática a situação acima!_ 

