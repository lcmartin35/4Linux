#!/usr/bin/python3

var = 10 #variavel Global

def escopo():
    global var #referencia a variavel Global
    var = 5  #variavel local
    print(var)

print(var)
escopo()
print(var)
