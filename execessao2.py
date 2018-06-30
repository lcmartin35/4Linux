#!/usr/bin/python3

from datetime import datetime

users = ['daniel','pedro','maria','joao']


while True:
    try:
        num = input('''
        USER
        0 - daniel
        1 - pedro
        2 - maria
        3 - joao
        S - sair ''')

        if num.lower() == 's':
            break
        print("O usuario {} esta logado".format(users[int(num)]))
    except IndexError as e:
        d = datetime.now()
        with open('python.log','a') as arquivo:
            result = "{},{} ".format(e, d.strftime("%Y-%m-%d %H:%H"))
            arquivo.write(result)
      break
    except  KeyboardInterrupt as e:
        
 

