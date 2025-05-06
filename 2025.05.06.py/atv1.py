# 1. Em um movimento retílineo uniformemente variado (MRUV), a fórmula para calcular a distância percorrida é dada po:
# Delta S = Velocidade inicial * tempo + Aceleração * tempo ao quadrado sobre 2 

import sys

velo_ini = int(input('Informe a velocidade inicial: '))
if velo_ini <= 0 :
    sys.exit('Informe uma velocidade positiva')

tempo = float(input('informe o tempo: '))

acel = int(input('Informe a aceleração: '))

delta_s = velo_ini * tempo + (acel * (tempo * tempo)) / 2

print(f'A velocidade do motorista é {delta_s}') 