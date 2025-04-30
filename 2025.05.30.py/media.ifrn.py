# Calcular média da disciplina do IFRN
#
# 1) Solicitar ao usuário que informe duas notas (As notas são inteiras)
# 2) Calcular a média do IFRN
# 3) Exibir a média 
# A média é = (E1 * 2 + E2 * 3) / 5

Etp1 = float(input(f'Digite a nota da primeira etapa: '))

Etp2 = float(input(f'Digite sua nota da segunta etapa: '))

media = (Etp1 * 2 + Etp2 * 3) / 5

print(f'Sua média foi:. {media:.0f}')