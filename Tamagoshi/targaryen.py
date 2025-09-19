import time
import random
from tamagoshi import Tamagoshi

class Targaryen(Tamagoshi):
    def __init__(self, saude: int):
        super().__init__(saude)
        self.dragao = ""
        self.saude = 300
        self.valiriano = 0
        self.montaria = 0
        self.luta = 0
    
    def nomearDragao(self):
        print("Seu ovo de dragão finalmente rachou, revelando um lindo filhote de dragão. Gostaria de nomea-lo?")
        resposta = int(input("1 = SIM  |  2 = NÃO \nResposta: "))

        if(resposta == 1):
            self.dragao = input("\n-> Digite o nome do seu dragãozinho: ")
            print(f"-> Seja bem-vindo, {self.dragao} 🐉")
        elif(resposta == 2):
            print("-> Seu dragão não foi nomeado")
        else:
            print("-> Digite um valor válido")
    
    def voarDragao(self, tempo):
        print(".........")
        time.sleep(0.3)
        print("........")
        time.sleep(0.3)
        print(".......")
        time.sleep(0.3)
        print("......")
        time.sleep(0.3)
        print(".....")
        time.sleep(0.3)
        print(f"{self.nome} Targaryen está voando... 🐉")
        print(".....")
        time.sleep(0.3)
        print("......")
        time.sleep(0.3)
        print(".......")
        time.sleep(0.3)
        print("........")
        time.sleep(0.3)
        print(".........")

        if(tempo > 0 and tempo <= 2):
            self.montaria += tempo / 0.8
            self.tedio = self.tedio - self.tedio * ((tempo * 0.8) / 100)
            print(f"{self.nome} voaram por {tempo} hora(s)")
        elif(tempo > 2 and tempo <= 4):
            self.montaria += tempo / 0.6
            self.tedio = self.tedio - self.tedio * ((tempo * 0.6) / 100)
            print(f"{self.nome} voaram por {tempo} hora(s)")
        elif(tempo > 4 and tempo <= 10):
            self.montaria += tempo / 0.4
            self.tedio = self.tedio - self.tedio * ((tempo * 0.4) / 100)
            print(f"{self.nome} voaram por {tempo} hora(s)")
        elif(tempo > 10):
            self.montaria += tempo / 0.2
            self.tedio = self.tedio - self.tedio * ((tempo * 0.2) / 100)
            print(f"{self.nome} voaram por {tempo} hora(s)")
            print(f"Seu tedio diminuiu para: {self.tedio}")
        else:
            print(f"{self.dragao} não voou muito, ele(a) ficou triste :(")

    def treinarValiriano(self):
        estudo = int(input("-> Adicione o tempo de estudo de conhecimento [1 - 100]: "))
        print("\n--------")
        time.sleep(2)
        print("Estudando valíriano...📖")
        time.sleep(2)
        print("--------\n")

        self.valiriano += (estudo / 10)

        print(f"-> {self.nome} Targaryen está falando {self.valiriano}% de valiriano! ")
    
    def lutarTrono(self):
        dano = random.randint(0, 300)
        print("\n>>>>>> Uma batalha pelo trono de ferro está começando! <<<<<<")
        escolha = int(input("1 - Recuar  |  2 - LUTAR! \nResposta: "))
        
        if(escolha == 1):
            print("\n-----------------")
            time.sleep(1)
            print(f"{self.nome} Targaryen recuou da batalha, preservando sua saude!")
            time.sleep(1)
            print("-----------------\n")
        elif(escolha == 2):
            print("\n-----------------")
            time.sleep(1)
            print(f"{self.nome} Targaryen foi à luta! DRACARYS {self.dragao} 🐉🔥")
            print("-----------------\n")
            time.sleep(1)

            self.saude -= dano

            if(self.saude <= 0):
                print("-----------------")
                time.sleep(1)
                print(f"{self.nome} Targaryen morreu...")
                print("........")
                time.sleep(0.7)
                print(".......")
                time.sleep(0.7)
                print("......")
                time.sleep(0.7)
                print(".....")
                time.sleep(0.7)
                print("....")
                time.sleep(1)
                print("...")
                time.sleep(1)
                print("..")
                time.sleep(1)
                print(".")
                time.sleep(3)
                exit()
            else:
                print(f"{self.nome} Targaryen está com {self.saude} de vida")
        else:
            print("-> Digite um valor válido")

            

    


targaryen1 = Targaryen("Daenerys")
targaryen1.voarDragao(20)


    
