#!/usr/bin/python3
'''
Ler  o numero e verificar se ele   é par ou impar
e adicionar ele em uma lista com o resultado
exemplo:
[2, 'par']
[3, ímpar']
'''
num = int(input('Numero: '))

for x in range(num):        
    if x % 2 == 0:
        print('{} par'.format(x))
    else:
        print('{} impar'.format(x))

