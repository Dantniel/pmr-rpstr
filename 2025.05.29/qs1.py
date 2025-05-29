'''
Dado que um número primo é um números que só possui dois divisores (1 e ele mesmo),
faça um programa que solicite ao usuário um número inteiro e informe se ele é primo ou não.
 (n - 1)! + 1
'''
import sys

try:
    ni= int(input('Digite um número inteiro positivo: '))
except ValueError:
 sys.exit('Erro: Digite um valor inteiro positivo.')

except Exception as e :
    sys.exit('Erro: {e}.')

else:
    if ni <= 0 :
        sys.exit('Digite um número maior que 0, ok?')

cntdiv = 1
divisor = 2
while divisor <= ni:
    if ni % divisor == 0:
        cntdiv += 1
    
    divisor += 1
print(cntdiv)
if cntdiv == 2:
    print('Primo')
else:
    print('Não é primo')