#!/usr/bin/python3
# pip3 install   pymongo
from pymongo import MongoClient 
from random import choice as sorteio

ids = list(range(999))


try:
    client = MongoClient()
    db = client['4linux']
except Exception as e:
    print('ERRO:{}'.format(e))

frutas = [
    {'preco':6, 'fruta':'melao', 'qtd':12},
    {'preco':8, 'fruta':'melancia', 'qtd':12},
    {'preco':10, 'fruta':'laranja', 'qtd':12},
    {'preco':15, 'fruta':'caqui', 'qtd':12},
    {'preco':3, 'fruta':'pera', 'qtd':12},
    {'preco':9, 'fruta':'uva', 'qtd':12},
]
db.frutas.remove()
for fruta in frutas:
    a = sorteio(ids)
    ids.remove(a)
    fruta['_id'] = a
    db.frutas._insert(fruta)
    



'''
db.pessoas.remove({'_id':6})
db.pessoas.insert({'_id':6, 'nome':'joaozinho'})
db.pessoas.update({'_id':6},{'$set': {'sobrenome':'peralta'}})
db.pessoas.update({'_id':6},{'$set': {'idade':11}})
'''

#dados = db.pessoas.find()

#list compression
#dados = [x for x in dados]

#print(dados)