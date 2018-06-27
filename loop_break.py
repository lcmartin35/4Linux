#!/usr/bin/python3

# lista de nome vazia
#ler nomes, adicionar na lista a digitar sair
# mostrar lista no final

nomes = []
while True:
    nome = str(input('Digite um nome ou  "sair" para finalizar: ' ))
    if nome.strip().lower()  == 'sair':
        break
    nomes.append(nome)
print('nomes: {}'.format(nomes))
    
  