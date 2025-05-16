''' EXERCICIO 1
Crie uma classe animal com atributos e métodos, posteriormente, crie uma classe que
herde seus atributos, e possua os seus atributos próprios.
'''

class Animal():
    def __init__(self, nome, idade, especie):
        self.nome = nome
        self.idade = idade
        self.especie = especie

    def get_especie(self):
        print(f"Minha espécie é: {self.especie}")

class Aves(Animal):
    def __init__(self, nome, idade, especie, categoria):
        super().__init__(nome, idade, especie)
        self.categoria = categoria

a_arara = Aves('Arara Azul', '25', 'Arara', 'ave tropical')
print(vars(a_arara))
a_arara.get_especie()
print(a_arara.get_especie)

print('Teste')