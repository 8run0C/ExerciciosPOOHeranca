class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, portas):
        super().__init__(self, marca, modelo, ano)
        self.portas = portas

class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, rodas):
        super().__init__(self, marca, modelo, ano)
        self.rodas = rodas
