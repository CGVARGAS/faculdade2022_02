# Manipulação de Dados em Arquivos

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

---



