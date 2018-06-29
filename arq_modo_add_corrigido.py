#!/usr/bin/python3

# abrir o arquivo uma unica vez
#l
with open('cores.txt','a') as arquivo: 
    while True:
        cor = input('Digite um nome ou  "sair" para finalizar:' ) 
        if cor.strip().lower()  == 'sair':
            break
        arquivo.write(cor + '\n')
#print('nomes: {}'.format(nomes))
    
  