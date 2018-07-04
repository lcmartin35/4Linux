#!/usr/bin/python3

#codigo sem funcao
#with open('nome.txt','r') as arquivo:   
   # conteudo = arquivo.readlines()

#o mesmo codigo acima com a funcao definida
def manipular_arquivo(nome, modo, conteudo=None):
    if modo == 'r':
        with open(nome, modo) as arquivo:
            return arquivo.readlines()
    elif modo == 'a':
        with open(nome, modo) as arquivo:
            arquivo.write(conteudo+'\n')
            return True
a = manipular_arquivo('nomes.txt','r')
manipular_arquivo('nomes.txt', 'a', 'josevaldo')

print(a)

'''
while True:
    arq = input('Digite o nome do arquico ou sair:')
    if arq == 'sair':
        break
    print(manipular_arquivo(arq))
'''
