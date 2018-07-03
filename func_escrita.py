#!/usr/bin/python3

def ler_lista(nome_arquivo,itens):
    with open('lista_nova.txt','a') as arquivo:
        dados = input('digite o conteudo :') 

        arquivo.write(dados)
ler_lista(nome_arquivo,itens)

