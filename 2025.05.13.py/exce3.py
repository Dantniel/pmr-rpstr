from logging import exception
import sys

try:
  intdividendo = int(input('Digite o dividendo: '))
  intdivisor   = int(input('Digite um divisor'))
  fltresultado = intdividendo / intdivisor
except ValueError:
   print('Erro: informe um valor que possa ser convertido em inteiro.')
except ZeroDivisionError:
  print('Não é possivel dividir por zero')
except:
    print(f'Erro: {sys.exc_info()}')
else: 
    print(fltresultado)