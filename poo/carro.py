class Carro():
    
    def __init__(self, car):
        self.car = car
        self.ligar = False
        self.desligar = True
        self.acelerador = False
        self.breque = False
        self.velocidade = 0

    def partida (self):

        if not self.ligar and self.desligar:
            print(f"O carro {self.car} acabou de ligar")
            self.ligar = True
            self.desligar = False

        elif self.ligar and not self.desligar:
            print ("O carro ja está ligado!")

    def desliga(self):
        if self.ligar and not self.desligar:
            print(f"O carro {self.car} acabou de ser desligado!")
            self.ligar = False
            self.desligar = True
        
        else:
            print(f"O carro {self.car} ja foi desligado")

    def acelerar(self):
        if self.ligar:
            print("Seu carro esta acelerando")
        else:
            print(f"O seu {self.car} precisa estar ligado para funcionar")

    def freiar(self):
        if self.ligar:
            if self.velocidade == 0:
                print("Seu carro ja esta fereiado!")

        else:
            print(f"O seu {self.car} precisa estar ligado para funcionar")

bmw = Carro("BMW 320i")
bmw.partida()
bmw.acelerar()
bmw.partida()
bmw.desliga()
bmw.acelerar()
bmw.desliga()
