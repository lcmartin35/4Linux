#!/usr/bin/python3

#codigo sem funcao
#with open('nome.txt','r') as arquivo:   
   # conteudo = arquivo.readlines()

#o mesmo codigo acima com a funcao definida
def ler_arquivo(nome):
    with open(nome, 'r')as arquivo:
        conteudo = arquivo.readlines()
        return conteudo

variavel1 = ler_arquivo('frutas.txt')
variavel2 = ler_arquivo('nomes.txt')
variavel3 = ler_arquivo('cores.txt')

print(variavel1)
print(variavel2)
print(variavel3)


