#!/usr/bin/python3
# pip3 install psycopg2

import psycopg2 
import os

os.system('clear')

try:
    con = psycopg2.connect('host=localhost dbname=projeto user=admin password=4linux port=5432')
    cur = con.cursor()
    print('Conectado com sucesso')
    resp = input("Deseja inserir Dados;  Sim ou Nao ? ")
    if  resp == 'Sim':
        cur.execute("insert into pessoas(nome,email,idade,telefone)values('teste','teste@teste.com.br', 99, '96789999')")
    else:
        print("Vou apenas listar")    
    cur.execute("select * from pessoas")

    conteudo = cur.fetchall()
#percorrendo a lista    
    for item in conteudo:
        print(item)
    #print(conteudo)    
    #fetchall fetchone

   
    con.commit()
    cur.close()  #fecha o cursor
    cur.close()  #encerra a conexao 
    print('Conexao fechado com sucesso')
    #Boas praticas == tratamento de excecao 
except Exception as e:
    cur.roolback()   
    print('Erro conexao: {}'.format(e))


