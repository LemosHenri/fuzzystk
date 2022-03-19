## sbrfuzzy

Instalação: pip install sbrfuzzy

versão = 1.0.0

**sbrfuzzy** é um módulo python para aplicações com base em sistemas baseados em regras fuzzy 

## Funções 

* `termolinguistico(nome,tipo,intervalo)` - método construtor para a criação de um termo linguistico onde receberá seu nome, que será usado na base de regras para chama-lo, seu tipo será o número fuzzy usado nesse termo e será definido como triangular, trapezoidal ou gaussiana, seu intervalo receberá uma lista contendo seu domínio discretizado. 

* `termolinguistico.pertinencia(valor)` - retornará o grau de pertinência do valor inserido com base no tipo definido na criação do termo linguistico através do seu construtor.

* `variavellinguistica(nome,universo)`- método construtor para a criação de um termolinguistico onde receberá seu nome e receberá seu universo que será o domínio discretizado onde está variavel se encontra.

* `variavellinguistica.adicionar(nome,tipo,intervalo)`- método usado para a adição de um termo linguistico para a variável em questão, seus parâmetros serão os mesmos da classe termolinguistico.

* `variavellinguistica.mostrarTermos(none)`- método usado para retornar uma lista com os nomes dos termos linguisticos adicionados.

* `variavellinguistica.grafico(none)`- método usado para plotar um gráfico com todos os seus termos linguísticos em seu domínio universo.

* `fuzzificador(inferencia,desfuzzificacao,regras,vetvariaveislinguisticas,valores)`- método construtor para a definir como o controlador fuzzy irá se comportar, recebe em inferência o nome do método de inferência que será usado (disponivel apenas Mamdani no momento), recebe em desfuzificacao o método de desfuzificacao que será usado (disponivel controide, media dos maximos, centro dos maximos), recebe em regras uma lista onde cada indice recebe uma regra da forma ( "baixo e alto então alto" ), recebe em vetvariaveislinguisticas uma lista com as variaveis linguisticas que serão usadas e recebe em valores os valores que serão calculados no controlador.

* `fuzzificador.mapeia(none)`-  método usado para retornar uma lista contendo o grau de pertinência de dos valores inseridos com base em cada regra inserida.

* `fuzzificador.ativarbase(none)`- método usado para retornar uma lista com o indice de cada regra ativada.

* `fuzzificador.iniciar(none)`- método usado para retornar o resultado gerado pelos valores inseridos no contrudor com base nos métodos de inferencia, desfuzificação e base de regras inseridos no construtor.



