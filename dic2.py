#!/usr/bin/python3

pessoa = {'nome':'Daniel','idade':24}

for x in pessoa.keys():  #retorn as chaves
    print(x)

for x in pessoa.values(): #retorna valores
    print(x)

for x in pessoa.items(): #retorna o item
    print(x)

# pessoa.get('idade'), por default ele retorna "none", pode  passa parametros
print(pessoa.get('email','Nao achei :('))

