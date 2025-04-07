# Herança - conseguimos criar classes herdadas de outras classes

# classe pai
class Veiculo():
    def __init__(self, tipo, chassi, marca, modelo, ano):
        self.tipo = tipo
        self.chassi = chassi
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

# Classe filho
class Motocicleta(Veiculo):
    def __init__(self, tipo, chassi, marca, modelo, ano, cilindrada):
        super().__init__(tipo, chassi, marca, modelo, ano) # super = superclasse
        self.cilindrada = cilindrada

v = Veiculo('carro', '21h3242l2', 'Fiat', 'Palio', '2010')
print(vars(v))
m = Motocicleta('motocicleta', 'asn232nj4j', 'Yamaha', 'Fazer', '2020', '160')
print(vars(m))