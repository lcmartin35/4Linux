#!/usr/bin/python3

class Car(): #classe pais
    """ Tentando abstrairum carro"""

    def __init__(self,ano, marca, modelo):
        self.ano = ano 
        self.marca = marca
        self.modelo = modelo
        self.velocidade = 0  
        self.combustivel = 'gasolina'    
 
    def acelerar(self):
        self.velocidade += 10
        print('acelerando...')

    def freiar(self):
        self.velocidade -= 10
        print('freiando...')
    
    def __str__(self):
        return 'ano: {} modelo: {}'.format(self.ano, self.modelo)

class Car_electric(Car): # Classe filho
    def __init__(self):
       super().__init__()

car1 = Car_electric()
#car1.ano = 2005
#car1.modelo = 'BMW'
#car2 = Car(2018,'c200','mercedes')

  
