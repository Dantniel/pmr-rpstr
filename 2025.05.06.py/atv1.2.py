import sys

distancia = int(input('Informe a distância Km'))
if distancia <= 0:
    sys.exit('Informe uma velocidade POSITIVA')

v_ini = int(input('Informe a velocidade inicial em Km/h'))
if v_ini <= 0:
    sys.exit('Informe uma velocidade inicial POSITIVA')

acel = int(input('Informe a aceleração em m/s2'))
if acel <= 0 :
    sys.exit('Informe uma aceleração POSITIVA')

distancia *= 1000

v_ini /= 3.6

delta = v_ini ** 2 - 4 * acel * distancia
if delta < 0 :
    sys.exit("Não é possivel calcular o delta")

tempo = (- v_ini + delta ** 0.5) / (2 * acel)

hora = tempo // 3600

tempo = tempo % 3600

minuto = tempo // 60

segundo = tempo % 60

print(f'Tempo = {hora}:{minuto}:{segundo}')