class Veiculo:
    def __init__(self, modelo, marca, ano, cor, nivel_tanque):
        self.modelo = modelo
        self.marca = marca
        self.ano = ano
        self.cor = cor
        self.nivel_tanque = nivel_tanque
    
    def andar(self):
        print(f"{self.modelo} está andando")

    def parar(self):
        print(f"{self.modelo} parou de andar")

    def imprimir(self):
        print(
            "O veículo tem características:\n" \
            f"Marca: {self.marca}\n" \
            f"Modelo: {self.modelo}\n" \
            f"Ano: {self.ano}\n" \
            f"Cor: {self.cor}\n"
            f"Nível de Gasolina: {self.nivel_tanque}"
        )

class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, cor, nivel_tanque, qtd_portas, bagageiro):
        super().__init__(marca, modelo, ano, cor, nivel_tanque)
        self.qtd_portas = qtd_portas
        self.bagageiro = bagageiro
    
    def portas(self):
        if self.qtd_portas <= 2:
            escolha = int(input("Seu carro é: 1 - Conversível | 2 - Normal"))
            if(escolha == 1):
                print(f"{self.modelo} é um conversível de {self.qtd_portas} portas!")
            elif(escolha == 2):
                print(f"{self.modelo} é um carro normal de {self.qtd_portas} portas!")
            else:
                print("VALORES ERRADOS")
        else:
            print(f"Seu {self.modelo} tem {self.qtd_portas}")   

class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, cor, nivel_tanque, cilindradas):
        super().__init__(marca, modelo, ano, cor, nivel_tanque)
        self.cilindradas = cilindradas
    
    def cilindradas(self):
        print(f"A {self.modelo} tem {self.cilindradas}") 
    
    def empinada(self):
        if self.cilindradas > 20:
            print(f"A {self.modelo} está empinando! RANDANDADADAN")
        else:
            print(f"A {self.modelo} não pode empinar >:(")
    
    def imprimir(self):
        print(
            "A moto tem características:\n" \
            f"Marca: {self.marca}\n" \
            f"Modelo: {self.modelo}\n" \
            f"Ano: {self.ano}\n" \
            f"Cor: {self.cor}\n"
            f"Nível de Gasolina: {self.nivel_tanque}\n"
            f"Cilindradas: {self.cilindradas}"
        )

def main():
    carro1 = Veiculo("Civic", "Honda", 2023, "Preto", 4)
    carro2 = Carro("Chevrolet", "Prisma", 2011, "Cinza", 12, 2,2)
    carro2.portas()


main()
