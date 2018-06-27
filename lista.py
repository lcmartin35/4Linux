#!/usr/bin/python3
# Criar chibang
'''
echo \#\!$(which python3) > lista.py &&   chmod +x    lista.py
'''
nomes = ['daniel','luiz','maria','jose']

copia = nomes[:]
nomes[0] = 'pedro' # substitui o nome qqque esta no indice 0
#nomes.append(['Carlos','Martins']) # adiciona um nome no final da lista
nomes.insert(0,'martins') # Insere no indice 0 (primeiro) inicio da lista
nomes.remove('martins') #   remove um elemento especifico da lista
nomes.pop() # delete o ultimo da lista


#print(nomes[-1][0])
print(nomes)
#print(copia) 