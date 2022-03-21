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
