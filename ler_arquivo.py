import numpy as np
import matplotlib.pyplot as plt

#Ler arquivo (Numpy)
data = np.genfromtxt('iris.data', delimiter=',', usecols=(0,1,2,3))

#Abrir arquivo (Nativo)
saida = open('saida.data', 'w')

#Consultar dados do arquivo lido
#print(data[0][0])

#Gerar gráfico
#plt.plot(data[:50,0], c='Red', ls=':', marker='s', ms=8, label='Comp. Sépala Iris-Setosa')
#plt.plot(data[50:100,0], c='Blue', ls=':', marker='s', ms=8, label='Comp. Sépala Iris-Versicolor')

#Colocar o label
#plt.legend()

#Mostrar o gráfico
#plt.show()

#Salvar gráfico
#plt.savefig('teste.png')

#Gerar SQL (Exemplo)
saida.write('-- ELEM_VIA\n')
for linha in data:
    saida.write('INSERT INTO TABELA (COLUNA01, COLUNA02) VALUES (' + str(linha[0]) + ', ' + str(linha[1]) + ');\n')

#Necessário fechar arquivo para salvar
saida.close()
