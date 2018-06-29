#!/usr/bin/python3

# lista de nome vazia
#ler nomes, adicionar na lista a digitar sair
# mostrar lista no final


while True:
    with open('cores.txt','a') as arquivo: 
        cor = input('Digite um nome ou  "sair" para finalizar:' ) 
        arquivo.write(cor + '\n')  
        if cor.strip().lower()  == 'sair':
            break
  
#print('nomes: {}'.format(nomes))
    
  