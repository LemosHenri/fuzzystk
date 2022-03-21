import numpy as np
from sbrfuzzy import *

entrada = open("dados.txt","a")
v = np.arange(0,300.5,0.5)

v1 = variavellinguistica("População",np.arange(0,300.5,0.5))
v1.adicionar("baixa","trapezoidal",[0,0,25,45])
v1.adicionar("media-baixa","triangular",[30,50,70])
v1.adicionar("media","triangular",[55,75,110])
v1.adicionar("media-alta","triangular",[110,165,185])
v1.adicionar("alta","triangular",[160,190,210])
v1.adicionar("muito-alta","trapezoidal",[200,210,300,300])


v2 = variavellinguistica("Variação",np.arange(-2,10.5,0.5))
v2.adicionar("baixa-negativa","triangular",[-2,0,0])
v2.adicionar("baixa-positiva","triangular",[0,0,3])
v2.adicionar("media","triangular",[2,5,8])
v2.adicionar("alta","trapezoidal",[6,9,10,10])

h = 0.5
x = [2,4,8,16]
br =        ["baixa então baixa-positiva",
                "media-baixa então media",
                "media então alta",
                "media-alta então media",
                "alta então baixa-positiva",
                "muito-alta então baixa-negativa"]

aux = []
retornos=[]
it=[i for i in range(250)]

for i in x:
    x0 = i
    for i in it:
        f = controlador(br,[v1,v2],[x0])    
        aux.append( x0 )
        x0 = x0 + h*f.mamdani()  
    retornos.append(aux)
    aux=[]

for i in range( len(retornos[0]) ):entrada.write(str(it[i]) + "\t" + str(retornos[0][i]) + "\t" 
                                                  + str(retornos[1][i]) + "\t" + str(retornos[2][i]) 
                                                  + "\t" + str(retornos[3][i]) + "\n")
  
entrada.close()
