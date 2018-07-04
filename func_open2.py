#!/usr/bin/python3

#codigo sem funcao
#with open('nome.txt','r') as arquivo:   
   # conteudo = arquivo.readlines()

#o mesmo codigo acima com a funcao definida
def ler_arquivo(nome,modo='r'):
    if modo == 'r':
        with open(nome, 'r')as arquivo:
            conteudo = arquivo.readlines()
            return conteudo

while True:
    arq = input('Digite o nome do arquico ou sair:')
    if arq == 'sair':
        break
    print(ler_arquivo(arq))

