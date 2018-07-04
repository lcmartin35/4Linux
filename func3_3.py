#!/usr/bin/python3
# 
from random import choice,randint
def sorteio(*sorteio):
    return choice(sorteio)

g = sorteio('daniel','maria', 'pedro','joao')
print(g)
    
with open ('nomes.txt', 'r') as arq:
    pessoas = arq.readlines()
    print(choice(pessoas))