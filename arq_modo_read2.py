#!/usr/bin/python3
'''
Criar uma copia do arquivo .txt, acrescentando indice em cada linha
exemplo 1-Daniel
'''
try:
    with open('tintas.txt','r') as arquivo:
        var = arquivo.readlines()

    
    alterado  = []
    cont = 1
    for linha in var:
        linha = linha.replace('\n', '-{}\n'.format(cont))
        alterado.append(linha)
    #alterado.append('{}-{}'.format(cont, linha))
        cont += 1

        with open('cores_copia.txt','w') as arquivo:
            for linha in alterado:
                arquivo.write(linha)
except FileNotFoundError as e:
        print("Arquivo nao existe") 
  