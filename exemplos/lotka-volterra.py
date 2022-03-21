import numpy as np
from sbrfuzzy import *

arquivo = open("saida.txt","a")

#declaração das variáveis e termos linguisticos
v1 = variavellinguistica("População 1",np.arange(0,250.5,0.5))
v1.adicionar("a1","trapezoidal",[0,0,10,35])
v1.adicionar("a2","triangular",[10,40,125])
v1.adicionar("a3","triangular",[35,125,210])
v1.adicionar("a4","trapezoidal",[125,210,250,250])
#v1.grafico()

v2 = variavellinguistica("População 2",np.arange(0,7,0.01))
v2.adicionar("b1","triangular",[0,0,2.2])
v2.adicionar("b2","triangular",[0,2.2,4.8])
v2.adicionar("b3","triangular",[2.2,4.8,7])
v2.adicionar("b4","triangular",[4.8,7,7])
#v2.grafico()

v3 = variavellinguistica("variação 1",np.arange(-0.05,0.05,0.0001))
v3.adicionar("va1","trapezoidal",[-0.05,-0.05,-0.043,0.005])
v3.adicionar("va2","triangular",[-0.045,0.005,0.005])
v3.adicionar("va3","triangular",[0.005,0.005,0.05])  
v3.adicionar("va4","trapezoidal",[0.005,0.05,0.05,0.05])
#v3.grafico()

v4 = variavellinguistica("variação 2",np.arange(-0.03,0.045,0.0001))
v4.adicionar("vb1","trapezoidal",[-0.03,-0.03,-0.03,0.005])
v4.adicionar("vb2","triangular",[-0.03,0.005,0.005])
v4.adicionar("vb3","triangular",[0.005,0.005,0.035])  
v4.adicionar("vb4","trapezoidal",[0.005,0.045,0.045,0.045])


#base de regras 1
br1 = ["a1 e b1 então va4",
      "a2 e b1 então va4",
      "a3 e b1 então va4",
      "a4 e b1 então va4",
      "a1 e b2 então va3",
      "a2 e b2 então va3",
      "a3 e b2 então va3",
      "a4 e b2 então va3",
      "a1 e b3 então va2",
      "a2 e b3 então va2",
      "a3 e b3 então va2",
      "a4 e b3 então va2",
      "a1 e b4 então va1",
      "a2 e b4 então va1",
      "a3 e b4 então va1",
      "a4 e b4 então va1"]

#base de regras 2
br2 = ["a1 e b1 então vb1",
       "a2 e b1 então vb2",
       "a3 e b1 então vb3",
       "a4 e b1 então vb4",
       "a1 e b2 então vb1",
       "a2 e b2 então vb2",
       "a3 e b2 então vb3",
       "a4 e b2 então vb4",
       "a1 e b3 então vb1",
       "a2 e b3 então vb2",
       "a3 e b3 então vb3",
       "a4 e b3 então vb4",
       "a1 e b4 então vb1",
       "a2 e b4 então vb2",
       "a3 e b4 então vb3",
       "a4 e b4 então vb4"]

#inicialização dos valores iniciais
x0 = 100
y0 = 3
h = 0.1 

for it in range(10000):
  f = controlador(br1,[v1,v2,v3],[x0,y0])
  g = controlador(br2,[v1,v2,v4],[x0,y0])

  arquivo.write(str(it) + "\t" + str(x0) + "\t" + str(y0) + "\n")
  x0 = x0 + h*(x0*f.mamdani()) 
  y0 = y0 + h*(y0*g.mamdani())

arquivo.close()

