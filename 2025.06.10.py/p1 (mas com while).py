'''
   Programa para ao digitar uma palavra ela seja escrita da seguinte forma 
   (como exemplo iremos usar a palavra PROGRAMAÇÃO).

   p
   R
   O
   G
   ...
   O  
'''

texto =  input('Digite um texto: ')
'''
for letra in texto:
    print(letra)
'''

posiçao = 0

while posiçao < len(texto):
    print(texto[posiçao])
    posiçao += 1