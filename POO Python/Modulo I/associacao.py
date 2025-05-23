'''ASSOCIAÇÃO
Ex.: Utilizar uma classe como atributo de outra classe
REVISAR
'''

class Escritor():
    def __init__(self, nome):
        self.__nome = nome
        self.__ferramenta = None

    @property
    def nome(self):
        return self.__nome
    
    @property
    def ferramenta(self):
        return self.__ferramenta
    
    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self.__ferramenta = ferramenta

class Caneta():
    def __init__(self, marca):
        self.__marca = marca

    @property
    def marca(self):
        return self.__marca
    
    def escrever(self):
        print("Caneta está escrevendo...")

escritor = Escritor('José')
caneta = Caneta('BIC')

escritor.ferramenta = caneta
escritor.ferramenta.escrever()