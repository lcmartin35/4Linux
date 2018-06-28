#!/usr/bin/python3
'''
Criar um dicionario de frutas e amarzenar nome e valor

'''
frutas = [
{'nome':'abacaxi','preco':10},
{'nome':'abacate','preco':5},
{'nome':'melao','preco':12},
{'nome':'melancia','preco':20},
{'nome':'mamao','preco':7}
]

frutas2 = []
for fruta in frutas:
    fruta['preco'] +=  0.5
    frutas2.append(fruta)
    #print(fruta)
print(frutas2)