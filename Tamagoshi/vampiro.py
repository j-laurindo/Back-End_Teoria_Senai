import time
import random
from tamagoshi import Tamagoshi

class Vampiro(Tamagoshi):
    def __init__(self, saude):
        super().__init__(saude)
        self.saude = 1000
        self.transformacao = 0
        self.conhecimento_vampirico = 0

    def alimentar(self, quantidade):
        if (quantidade >= 0 and quantidade <= 100):
            print(f"-> O Tamagoshi {self.nome} está bebendo sangue")
            time.sleep(1)
            print("...")
            time.sleep(1)
            print("..")
            time.sleep(1)
            print(".")
            time.sleep(1)
            print("🩸")

            self.fome -= self.fome * (quantidade / 100)
        elif (self.fome == 0):
            print(f"{self.nome} já está cheio!")

    def hipnose(self):
        if(self.conhecimento_vampirico <= 20):
            print(f"-> {self.nome} tentou hipnotizar você, mas aparentemente não funcionou!")
            self.transformacao += 5
        elif(self.conhecimento_vampirico <= 70):
            print("...")
            time.sleep(1)
            print("......")
            time.sleep(1)
            print("........")
            time.sleep(1)
            print(f"-> {self.nome} tentou hipnotizar você, percebeu sua consciência sumindo?")
        elif(self.conhecimento_vampirico <= 100):
            print("...")
            time.sleep(1)
            print("......")
            time.sleep(1)
            print("........")
            print(f"-> {self.nome} hipnotizou você! Assista Crepusculo imediatamente")  
        else:
            print("-> Valor inválido")
    
        
