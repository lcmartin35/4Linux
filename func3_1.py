#!/usr/bin/python3
# 
def boas_vindas(*nomes):
   for item in nomes: 
       print("Olá {} seja bem vindo!".format(item))
    
   

boas_vindas('daniel', 'rafael', 'lucia')