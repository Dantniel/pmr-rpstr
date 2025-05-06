# 1. Em um movimento retílineo uniformemente variado (MRUV), a fórmula para calcular a distância percorrida é dada po:
# Delta S = Velocidade inicial * tempo + Aceleração * tempo ao quadrado sobre 2 

velo_ini = float(input('Informe a velocidade inicial: '))

tempo = float(input('informe o tempo: '))

acel = float(input('Informe a aceleração: '))

delta_s = velo_ini * tempo + (acel * (tempo * tempo)) / 2

print(f'A velocidade do motorista é {delta_s}')