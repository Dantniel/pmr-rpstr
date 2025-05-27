# Programa para executar uma potenciação de 2 números inteiros
# utilizando apenas o operador produto.
import sys

multiplicador = int(input('Informer o multiplicador'))
if multiplicador <= 0:
    sys.exit('O valor deve ser positivo')
multiplicando = int(input('Informe o multiplicando'))
if multiplicando <= 0:
    sys.exit('O valor deve ser positivo')
while multiplicando <= 10:
    print(f'multiplicando')

    
