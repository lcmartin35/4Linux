#!/usr/bin/python3
'''
Criar um dicionario de frutas e amarzenar nome e valor

'''
frutas = [
{'nome':'abacaxi','preco':10,'qtd':10},
{'nome':'abacate','preco':5,'qtd':20},
{'nome':'melao','preco':12,'qtd':2},
{'nome':'melancia','preco':20,'qtd':4},
{'nome':'mamao','preco':7,'qtd':11}
]

soma_fruta = 0

for fruta in frutas:
    soma_fruta += fruta['preco'] * fruta['qtd'] 
   # soma_fruta.append(fruta)
    #print(fruta)
print('O valor total da vendas sera R$ {} '.format(soma_fruta))