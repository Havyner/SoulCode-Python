'''
1) Deve se criar 5 funções diferentes, sendo elas somar, subtrair, dividir, multiplicar e listar.
2) Deve se criar um MENU com if else sendo que o usuário escolha qual função deve acessar. 
3) Ao ser escolhido a função, o usuário é direcionado a ela e insere os parâmetros que desejam realizar as operações.
4) As funções matemáticas devem receber os números para realizar a operação, realizar o cálculo e imprimir o resultado para o usuário.
5) Na função listar, deve-se criar uma lista de vantagens do python e imprimir para o usuário.

'''
# Função Somar
def somar():
    a = int (input ("Informe o Primeiro número: "))
    b = int (input ("Informe o Segundo número: "))

    soma = a + b

    print("O resultado da soma é: ", soma)
    menu()
    
# Função de Subtração
def subtrair():
    a = int (input ("Informe o Primeiro número: "))
    b = int (input ("Informe o Segundo número: "))

    sub = a - b

    print("O resultado da Subtração é: ", sub)
    menu()
    
# Função de divisão
def dividir():
    a = float (input ("Informe o Primeiro número: "))
    b = float (input ("Informe o Segundo número: "))

    div = a / b

    print("O resultado da Divisão é: ", div)
    menu()
    
    
# Dunção de Multiplicar
def multiplicar():
    a = int (input ("Informe o Primeiro número: "))
    b = int (input ("Informe o Segundo número: "))

    mult = a * b

    print("O resultado da Subtração é: ", mult)
    menu()
    
# Lista de vantagens de python
def listar():
    print("""*Fácil integração
*Sintaxe simples
*Grande comunidade ativa""")
    menu()

# Função de MENU para se criar um loop até ser interrompido pelo usuário
def menu():
    print("--------------MENU")
    print("-----1) Somar")
    print("-----2) Subtrair")
    print("-----3) Dividir")
    print("-----4) Multiplicar")
    print("-----5) Listar benefício de PYTHON")
    print("-----6) SAIR")

    op = int (input("Informe a opção desejada: "))

    if op == 1:
        somar()
    elif op == 2:
        subtrair()
    elif op == 3:
        dividir()
    elif op == 4:
        multiplicar()
    elif op == 5:
        listar()
    elif op == 6:
        print("Obrigado!!")
        exit
    else:
        print("Opção inválida!!")
        menu()

print("--------------MENU")
print("-----1) Somar")
print("-----2) Subtrair")
print("-----3) Dividir")
print("-----4) Multiplicar")
print("-----5) Listar benefício de PYTHON")
print("-----6) SAIR")

op = int (input("Informe a opção desejada: "))

# Realizando as condições
if op == 1:
    somar()
elif op == 2:
    subtrair()
elif op == 3:
    dividir()
elif op == 4:
    multiplicar()
elif op == 5:
    listar()
elif op == 6:
    print("Obrigado!!")
    exit
else:
    print("Opção inválida!!")
    menu()