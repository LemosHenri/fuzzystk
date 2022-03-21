import numpy as np
from sbrfuzzy import *

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
