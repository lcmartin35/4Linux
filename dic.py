#!/usr/bin/python3

pessoas = [
{'nome':'Daniel','idade':24},
{'nome':'joao','idade':20,},
{'nome':'maria','idade':45,},
{'nome':'pedro','idade':22,},


]

for x in pessoa.keys():  #retorn as chaves
    print(x)

for x in pessoa.values(): #retorna valores
    print(x)




print(type(pessoas)) # utilizar a funcao "type" para   saber se lista ou  classe
print(pessoas[3]['idade'])