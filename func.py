#!/usr/bin/python3
# 
def boas_vindas(nome,idade=24):
    #print("Oi sou {} tenho {} anos".format(nome,idade))
    return "Oi sou {} tenho {} anos".format(nome,idade)



a = boas_vindas('daniel',24)

print(a)
#boas_vindas('jose',25)
#boas_vindas('maria',43)