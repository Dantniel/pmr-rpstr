import sys

try:
  intdividendo = int(input('Digite o dividendo: '))
  intdivisor   = int(input('Digite um divisor'))
  fltresultado = intdividendo / intdivisor
except Exception as tipoexceçao:
    print(f'Erro: {tipoexceçao}')
    print(f'Erro: {sys.exc_info()}')
else: 
    print(fltresultado)