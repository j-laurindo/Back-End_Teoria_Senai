import time 
from tamagoshi import Tamagoshi

class Garfield(Tamagoshi):
    def __init__(self, nome):
        super().__init__(nome)
        self.saude = 200
        self.fome = 20
        self.tedio = 30
        self.sono = 30

    def roubarLasanha(self):
        if(self.tedio > 20):
            print("-----------")
            print("-> O Tamagoshi Garfield está entediado, ele tá afim de bater uma boquinha")
            print("-----------")
            time.sleep(1)
            print("\n-> Escolha uma comida para dar uma 'animada' no Tamagoshi Garfield")
            print("\n-> 1 - Lasanha 🥘")
            print("\n-> 2 - Churrasco 🍖")
            print("\n-> 3 - Maçã 🍎")
            
            escolha = int(input("\nResposta: "))

            if(escolha == 1):
                self.fome -= 60
                self.tedio -= 30
                print(f"\n-> O Tamagoshi Garfield achou massa esse lanchinho! <3")
            elif(escolha == 2):
                self.fome -= 40
                self.tedio -= 20
                print(f"\n-> O Tamagoshi Garfield até achou legalzinho esse petisco")
            elif(escolha == 3):
                self.fome += 30
                self.tedio += 30
                print(f"\n-> TÁ MALUCO? O Tamagoshi Garfield quase passou mal, ele >>>odeia<<< maçã!!!!!!😤😤")
            else:
                print("-> Valor inválido")
        else:
            print("O Garfield tá de boa!")
    
    def irritarTod(self):
        print("-> O Tamagoshi Garfield está entediado, o Tod dormindo parece tãaaao tranquilo...")
        time.sleep(2)
        print("-> Bem tranquilo mesmo...")
        time.sleep(2)
        print("-> Tãaaaaaaaao irritante...")
        time.sleep(2)
        print(".")
        time.sleep(1)
        print("..")
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("....")
        time.sleep(1)
        print("-> 🤦‍♂️ AAAAU")
        print("-> Tamagoshi Garfield arranhou 'acidentalmente' o braço de Tod :D")
        print("-> Tamagoshi Garfield se sente mais feliz")
        
        self.getHumor += 10

    def brincar(self, quantidade):
        print("-> O cachorro Odie chama o Tamagoshi Garfield para brincar")
        escolha = int(input("1 - SIM  |  2 - NÃO  \n -> Resposta: "))

        if(escolha == 1):
            self.tedio -= self.tedio * (quantidade / 100)
            self.fome += 15
            
            print("-> O Tamagoshi Garfield brincou (um pouco)")
        elif(escolha == 2):
            print("-> O Tamagoshi Garfield fingiu que não ouviu")

    
    

garfield = Garfield("Garfield")
garfield.brincar()




