'''
   Dados dois números inteiros positivos, determinar o Máximo Divisor 
   Comum (MDC) entre eles usando o Algoritmo de Euclides.
'''
import sys


try:
 num1 = int(input('Digite um número inteiro: '))
 num2 = int(input('Digite um outro numero número inteiro: '))

except ValueError:
    sys.exit('Erro: o valor não é inteiro.')
except Exception as e:
    sys.exit('Erro: {e}')

else:
    if num1 <= 0 or num2 <= 0:
        sys.exit('O valor deve ser inteiro')

MDC = 1

if num1 > num2:
for num2 in range (1, num1 + 1)
