## sbrfuzzy

Instalação: pip install sbrfuzzy

versão = 1.0.0

**sbrfuzzy** é um módulo python para aplicações com base em sistemas baseados em regras fuzzy.

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



