class Carro():
    
    def __init__(self, car):
        self.car = car
        self.ligar = False
        self.acelerador = False
        self.velocidade = 0

    def partida (self):
        if not self.ligar:
            print(f"O carro {self.car} acabou de ligar")
            self.ligar = True

        elif self.ligar:
            print ("O carro ja está ligado!")

    def desliga(self):
        if self.ligar:
            print(f"O carro {self.car} acabou de ser desligado!")
            self.ligar = False
        
        else:
            print(f"O carro {self.car} ja foi desligado")

    def acelerar(self):
        if self.ligar:
            print("Seu carro esta acelerando")
            self.velocidade += 10
            print(f"{self.velocidade}Km/h")
        else:
            print(f"O seu {self.car} precisa estar ligado para funcionar")

    def frear(self):
        if self.ligar:
            if self.velocidade >= 0:
                print("Seu carro ja esta fereiando!")
                self.velocidade -= 10
                print(f"{self.velocidade}Km/h")
            else:
                print(f"O carro {self.car} esta parado!")
        else:
            print(f"O seu {self.car} precisa estar ligado para funcionar")


car = Carro(input("Input your car: "))
while True:

    acao = input("O que deseja fazer? (partida, acelerar, freiar, desligar): ")
    if acao == "partida":
        car.partida()
    elif acao == "acelerar":
        car.acelerar()
    elif acao == "freiar":
        car.freiar()
    elif acao == "desligar":
        car.desliga()
    else:
        print("Ação inválida. Tente novamente.")
