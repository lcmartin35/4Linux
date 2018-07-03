#!/usr/bin/python3
import pdb

def e_par(num):

    if num % 2 == 0:
        return 'par'
    else:
        return 'impar'

# num = int(input('Numero: '))
a = e_par(11)
print(a.upper())

