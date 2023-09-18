# sbrfuzzy

## Instalação

Usando Pypi
```
pip install fuzzystk
```
versão = 0.0.2

## Descrição 

O **fuzzystk** é um módulo python desenvolvido para ser uma solução alternativa que possibilita a criação de aplicações que fazem uso da lógica fuzzy, com foco em sistemas baseados em regras fuzzy (SBRF).

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
import fuzzystk as fz
import numpy as np 

entrada = open('dados.dat', 'w')
n = 300

v1 = fz.ling_var("População",np.linspace(0,300,n))
v1.add("baixa","trapezoidal",[0,0,25,45])
v1.add("media-baixa","triangular",[30,50,70])
v1.add("media","triangular",[55,75,110])
v1.add("media-alta","triangular",[110,165,185])
v1.add("alta","triangular",[160,190,210])
v1.add("muito-alta","trapezoidal",[200,210,300,300])


v2 = fz.ling_var("Variação",np.linspace(-2,10,n))
v2.add("baixa-negativa","triangular",[-2,0,0])
v2.add("baixa-positiva","triangular",[0,0,3])
v2.add("media","triangular",[2,5,8])
v2.add("alta","trapezoidal",[6,9,10,10])

base_regras = ["baixa então baixa-positiva",
                "media-baixa então media",
                "media então alta",
                "media-alta então media",
                "alta então baixa-positiva",
                "muito-alta então baixa-negativa"]

#v1.plot()
#v2.plot()

h = 0.5
x0 = 2
it = 0

while it < 250:
    f = fz.controller(base_regras, [v1,v2], [x0])
    entrada.write(str(it) + '\t' + str(x0) + '\n')
    x0 = x0 + h*f.mamdani()
    it += 1

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
