# Retorna a porção inteira de um número
from math import trunc
num = float(input('Digite um número decimal: '))
print('O número digitado é {0} e sua porção inteira é {1}'.format(num, trunc(num)))

''' Outra forma de fazer sem importar módulo'''

num = float(input('Digite um número decimal:' ))
print('O número digitado foi {0} e sua porção inteira é {1}'.format(num, int(num)))
