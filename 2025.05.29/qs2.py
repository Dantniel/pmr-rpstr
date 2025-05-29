'''

'''
import sys

try:
    valor = int(input('Digite um valor inteiro positivo: '))
except ValueError:
    sys.exit('Valor não correspondente.')
except Exception as e:
    sys.exit('Valor não correspondente.')
else:
    if valor < 0:
        print('Não é possivel um fatorial negativo.')
    elif valor < 2 :
        print(f'{valor}! = 1')
    else:
        fatorial = valor
        avx = valor
        while avx <= 2:
            avx -= 1
            fatorial *= avx
print(f'{valor}! = {fatorial}')