'''
Programa para calcular a média de uma disciplina semestral no IFRN.

As notas devem ser inteiras e entre 0 e 100 (inclusive).

Caso a média seja igual ou superior a 60 o aluno estará aprovado;
Caso a média seja igual ou superior a  20 o aluno estará em prova final e os demais casos estará reprovado.
'''
import sys


etapa1 = int(input('Informe a nota da etapa 1: '))
if etapa1 < 0 or etapa1 > 100:
    sys.exit('Erro: Nota inválida, isso aí ta certo mesmo?')

etapa2 = int(input('informe a nota da etapa 2: '))
if etapa2 < 0 or etapa2 > 100:
    sys.exit('Erro: nota inválida, tem um bagulho errado aí')

media = int(round( (etapa1 * 2 + etapa2 * 3) / 5, 0))
print(f'Média do aluno: {media}')

if media >= 60:
    print('Aluno aprovado.')
elif media >= 20:
    print('O aluno ira fazer a prova final.')
else:
    print('Aluno reprovado, que feio em.')