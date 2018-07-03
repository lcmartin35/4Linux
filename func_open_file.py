#!/usr/bin/python3
# 
def ler_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo,'r') as arq:
            return arq.readlines()
    except Exception as e:
        return "Erro: {}".format(e)

arquivo = ler_arquivo('cores.txt')
#print(arquivo)


def escr_arq(nome_arq,conteudo):
    try:
        with open(nome_arq,'w') as arq:
            arq.writelines(conteudo)
            return True

    except Exception as e:
        return 'Erro:{}'.format(e)

conteudo = ler_arquivo('frutas.txt')
print(conteudo)

def alterar_lista(lista):
    lista1 = []
    for x in lista:
        lista1.append('{}\n'.format(x))
    return lista1



nomes = ['daniel','pedro','joao','julio']
nomes1 = []
for x in nomes:
    nomes1.append('{}\n'.format(x))

#escr_arq('nomes.txt',ler_arquivo('frutas.txt'))

