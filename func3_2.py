#!/usr/bin/python3
# 
def boas_vindas(**kargs):
    print("Olá {} {}  seja bem vindo!".format(kargs['nome'],kargs['sobrenome']))
   

boas_vindas(nome='daniel',sobrenome='prata')

def valor_total(**frutas):
    return frutas['preco'] * frutas['qtd']

a = valor_total(preco=5, qtd=2 )
print(a)
