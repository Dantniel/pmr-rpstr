# progama para executar um produto de 2 números inteiro
# positivos utilizando apenas o operador soma (+)
import sys

multiplicador = int(input('Informer o multiplicador'))
if multiplicador <= 0:
    sys.exit('O valor deve ser positivo')
multiplicando = int(input('Informe o multiplicando'))
if multiplicando <= 0:
    sys.exit('O valor deve ser positivo')
while multiplicando <= 10:
    print(f'multiplicando')

    
