# Criando uma classe

class Veiculo():
    def __init__(self, tipo, chassi, marca, modelo, ano):
        self.tipo = tipo
        self.chassi = chassi
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

class Aviao():
    def __init__(self, tipo, motor,linha_aerea, modelo, ano):
        self.tipo = tipo
        self.motor = motor
        self.linha_aerea = linha_aerea
        self.modelo = modelo
        self.ano = ano

# Criação do objeto
carro = Veiculo('carro', '23K2N4K23K', 'Fiat', 'Palio', '2009')
print(vars(carro))

aviao = Aviao('Boing', '1000', 'Azul', 'AirBus 433', '2020')
print(vars(aviao))


# self: refere-se ao próprio objeto que utilizou o método
# __init__: método relacionado ao construtor
class Funcionario():
    def __init__(self, nome, cpf, salario):
        #atributos
        self.nome = nome
        self.cpf = cpf
        self.salario = salario
    #Métodos
    def get_salario(self):
        print(f"Meu salário é: {self.salario}")

    def get_bonificacao(self):
        return self.salario * 0.15
    
jose = Funcionario('Havyner', '01100000010', 2500)
jose.get_salario()
print(jose.get_bonificacao())