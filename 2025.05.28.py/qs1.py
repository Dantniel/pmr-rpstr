# Programa que solicite ao usúario números inteiros
# aleatoriamente até que seja informado o valor 0.
# Quando for digitado o valor 0, o programa deverá informar:
# A) Quantos números inteiro foram digitado;
# B) A soma dos números inteiros positivos;
# C) A média dos números inteiros positivos;
# O valor 0 digitado não deve ser considerado em nenhum dos iten acima.
import sys

valor = None
somaposi = 0
qtval = 0
qtvalposi = 0

while valor != 0:
    try:
        valor = int(input('Informe um valor inteiro: '))
    except ValueError:
        print('Erro: valor inteiro inválido')
    except Exception as e:
        print(f"Erro: {e}")
    else:
        if valor > 0:
            somaposi += valor
            qtvalposi += 1
        
    qtval += 1

print(f'Quantos números inteiro foram digitados: {qtval}')
print(f'Soma dos números inteiros positivos: {somaposi}')
print(f'Média dos números inteiros positivos: {somaposi/qtvalposi}')
