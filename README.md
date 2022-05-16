# sbrfuzzy

## Instalação

Usando Pypi
```
pip install sbrfuzzy
```
versão = 1.0.0

## Descrição 

O **sbrfuzzy** é um módulo python desenvolvido para ser uma solução alternativa que possibilita a criação de aplicações que fazem uso da lógica fuzzy, com foco em sistemas baseados em regras fuzzy (SBRF).

## Funções 

* `termolinguistico(nome,tipo,intervalo)` - método construtor para a criação de um termo linguistico onde receberá seu nome, que será usado na base de regras para chama-lo, seu tipo será o número fuzzy usado nesse termo e será definido como triangular, trapezoidal ou gaussiana, seu intervalo receberá uma lista contendo seu domínio discretizado. 

* `termolinguistico.pertinencia(valor)` - retornará o grau de pertinência do valor inserido com base no tipo definido na criação do termo linguistico através do seu construtor.

* `variavellinguistica(nome,universo)`- método construtor para a criação de um termolinguistico onde receberá seu nome e receberá seu universo que será o domínio discretizado onde está variavel se encontra.

* `variavellinguistica.adicionar(nome,tipo,intervalo)`- método usado para a adição de um termo linguistico para a variável em questão, seus parâmetros serão os mesmos da classe termolinguistico.

* `variavellinguistica.mostrarTermos(none)`- método usado para retornar uma lista com os nomes dos termos linguisticos adicionados.

* `variavellinguistica.grafico(none)`- método usado para plotar um gráfico com todos os seus termos linguísticos em seu domínio universo.

* `controlador(regras,vetvariaveislinguisticas,valores)`- método construtor para a definir como o controlador fuzzy irá se comportar, recebe em regras uma lista onde cada indice recebe uma regra da forma ( "baixo e alto então alto" ), recebe em vetvariaveislinguisticas uma lista com as variaveis linguisticas que serão usadas e recebe em valores os valores que serão calculados no controlador.

* `controlador.mapeia(none)`-  método usado para retornar uma lista contendo o grau de pertinência de dos valores inseridos com base em cada regra inserida.

* `controlador.mamdani(defuzzificacao)`- método usado para retornar um valor real correspondente ao resultado calculado pelo controlador aplicando o método de inferência de Mamdani. Este método recebe como parâmetro o método de defuzzificação que será utilizado, podendo ser escolhido o método do centroide, média dos máximos e centro dos máximos. Por padrão, caso nada seja inserido, será usado o método do centroide.

* `controlador.tsk(vet_regras)`- método usado para retornar um valor real correspondente ao resultado calculado pelo controlador aplicando o método de inferência de Takagi-Sugeno-Kang. Este método recebe como parâmetro uma lista contendo as funções que serão agregadas aos consequentes da base de regras, ordenadamente.

## Exemplos 
Malthus.py

```
import numpy as np
from controlador import fuzzificador,variavellinguistica

entrada = open("dados.txt","a")
v = np.arange(0,300.1,0.1)

v1 = variavellinguistica("População",np.arange(0,300.5,0.5))
v1.adicionar("muito-baixa","trapezoidal",[0,0,18,40])
v1.adicionar("baixa","triangular",[30,50,65])
v1.adicionar("media","triangular",[55,80,110])
v1.adicionar("alta","trapezoidal",[90,120,250,250])

v2 = variavellinguistica("Variação",np.arange(0,110.5,0.5))
v2.adicionar("muito-baixa","trapezoidal",[0,0,6,16])
v2.adicionar("baixa","triangular",[5,18,23])
v2.adicionar("media","triangular",[20,30,41])
v2.adicionar("alta","trapezoidal",[28,55,110,110])

br = ["muito-baixa então muito-baixa",
             "baixa então baixa",
             "media então media",
             "alta então alta"]
h = 0.5
x0 = 2
interacao = 0

while interacao < 30:
    f = controlador(br,[v1,v2],[x0])    
    entrada.write(str(interacao) + "\t" + str(x0) + "\n")
    x1 = x0 + h*f.mamdani() 
    interacao += 1 
    
entrada.close()
```
tsk.py

```
from sbrfuzzy import *
import numpy as np

def f1(vet): return 1.4329 * vet[0] - 0.0757 
def f2(vet): return 1.4357 * vet[0] - 0.0744
def f3(vet): return 1.0728 * vet[0] + 0.0724 
def f4(vet): return 0.9702 * vet[0] + 0.1341
def f5(vet): return 0.4968 * vet[0] + 0.5114

v1 = variavellinguistica("EAS",np.arange(0,1.001,0.001))
v1.adicionar("a1","trapezoidal",[0,0,0.1,0.3])
v1.adicionar("a2","triangular",[0.1,0.3,0.5])
v1.adicionar("a3","triangular",[0.3,0.5,0.7])
v1.adicionar("a4","triangular",[0.5,0.7,0.9])
v1.adicionar("a5","trapezoidal",[0.7,0.9,1.0,1.0])

bs = ["a1 então f1",
    "a2 então f2",
    "a3 então f3",
    "a4 então f4",
    "a5 então f5"]

vet = [f1,f2,f3,f4,f5]

arquivo = open("saida.txt","a")

entradas = np.arange(0,1,0.01)
for i in entradas:
    f = controlador(bs,[v1],[i])
    arquivo.write(str(i) + "\t" + str(f.tsk(vet)) + "\n")

arquivo.close()
```
## Observações
1. No método tsk() é recomendado utilizar funções que recebem listas como parâmetro. 
