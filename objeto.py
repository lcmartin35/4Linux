#!/usr/bin/python3

class Dog():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.energia = 5
        self.dormir = 10

    def latir(self):
        print('Au au!')

    def andar(self):
        if self.energia > 0: 
            self.energia -= 1
            print('andando.....energia: {}'.format(self.energia))
        else:
            print('ZZzzzz...')
            self.dormir()

    def dorme(self):
        self.dormir = 5
        print('Dormindo ....zzzZZZZ!-->   Energia recuperada! agora seu cao possui: {}'.format(self.dormir))

        
dog1 = Dog('bilu',2) ## criando objeto
dog2 = Dog('Python',3)
print(dog1.idade)


dog1.andar()
dog1.andar()
dog1.andar()
dog1.andar()
dog1.andar()
dog1.dorme()
