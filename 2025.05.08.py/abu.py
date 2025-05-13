'''
Programa para classificar um triângulo quanto aos ângulos.

- O programa deverá solicitar 3 ângulos inteiros positivos;
- Para ser um triângulo, a soma dos ângulos deve ser igual a 180;

- Retângulo: Possui un ângulo interno reto (igual a 180).
- Obtusângulo: Possui um ângulo interno obtuso (maior do que 90)
- Acutângulo: Possui todos os ângulos interno agudos (menores de 90)
'''
import sys

cat_a = input('Qual o ângulo do cateto adjacente? ')
if cat_a <= 0 or cat_a >= 180:
    sys.exit('Tá de zuera com minha cara, é pegadinha.')

cat_o = input('Qual o Angulo do cateto oposto?')
if cat_o <= 0 or cat_o >= 180:
    sys.exit('Ha ha, muito engraçado')

hip = input('Qual o ângulo da hipotenusa')
if hip <= 0 or hip >= 180:
    sys.exit('Volta pro fundamental')

trian = cat_a + cat_o + hip
if trian > 180:
    sys.exit('Isso é tudo, menos um triângulo')
 
