#!/usr/bin/python3
'''
Ler  o numero e verificar se ele   é par ou impar
e adicionar ele em uma lista com o resultado
exemplo:
[2, 'par']
[3, ímpar']
'''
numero = int(input('Numero: '))

resultado  = [] #lista vazia
if numero % 2 == 0:
    resultado.append('par')
else:
    resultado.append('impar')

print(resultado) 
