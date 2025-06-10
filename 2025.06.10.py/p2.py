'''
   Programa para ao digitar uma palavra ela seja escrita da seguinte forma 
   (como exemplo iremos usar a palavra PROGRAMAÇÃO).

   p
   PR
   PRO
   PROG
   ...
   PROGRAMAÇÃO  
'''

texto = input('Digite uma palavra: ')

posicao = 0
while posicao < len(texto):
    print(texto[0:posicao + 1])
    posicao +=1
