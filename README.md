# Manipulação de Dados em Arquivos com Python

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
