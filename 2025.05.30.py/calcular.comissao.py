# Fazer um programa para solicitar o valor de uma venda e
# o percentual da comissão e exibir o valor da comissão

valor_venda = float(input(' Dgite o valor da venda (R$): '))
percentual = float(input('Informe a comissão (R$)......:'))

comissao = valor_venda * percentual / 100

print(f'O valor da comissão é R$ {comissao:.2f}')