# Encapsulamento: é o termo que utiliza para esconder alguns atributos e métodos para que não sejam acessados
# Publico
# _Protegida
# __Privada

class Time():
    def __init__(self, nome, estado, ano):
        self.nome = nome
        self.estado = estado
        self.ano = ano
        self.__renda = 0 # private (atributo privado)
    
    # Estrutura privada
    @property
    def renda(self):
        return self.__renda
    
    @renda.setter
    def renda(self, nova_renda):
        # renda é privada, por isso a mensagem de erro
        raise ValueError("Impossível alterar renda diretamente!")
    
    def calcula_renda(self):
        self.__renda = self.__renda + self.renda

santos = Time('Santos', 'São Paulo', '1912')
santos.__renda = 10000000    