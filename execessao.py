#!/usr/bin/python3
while True:
    try:
        num = int(input("Digite um numero: "))
        print(num)
        break
    except ValueError as e:
        print("Nao e um inteiro:{}".format(e))
        pass
        
    except Exception as e:
         print("Nao e um inteiro:{}".format(e))