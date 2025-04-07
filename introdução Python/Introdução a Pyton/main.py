'''Como sugestão de prática, indicamos você a criar um novo script python seguindo as orientações a seguir:

1- Crie três inputs que receba os três dados abaixo:
Nome do tipo string
Altura do tipo Float
CPF do tipo inteiro  

2. Exiba através de um único print as três informações para o usuário.

nome = input ("Infome seu nome: ")
altura = float(input("Informe sua altura:"))
cpf = int(input("Informe seu CPF: "))

print("Meu nome é", nome, ", tenho ", altura, "de altura, e meu CPF é:", cpf)

num = 100 == 100

print(num)'''


'''
1- Crie uma variável número e atribua o valor 15 a ela.
2- Crie um comando de condição para verificar se ela é == a 15, Menor que 15, maior que 15.
3- Informar através de print a informação para o usuário.
'''

'''numero = 16

if numero == 15:
    print("Número é igual a 15")
elif numero < 15:
    print("O número é menor que 15")
else:
    print("Número maior que 15")
'''

'''
1- Crie um laço com for in range que imprima os múltiplos de 3 no intervalo entre 0 e 15.
'''
'''for j in range(0, 18, 3):
    print(j)
'''
"""
verificação de tabeça asc
for i in range(122):
    print(str(i) + " - " + chr(i))
"""
''' Atividade de STRING
1- Crie uma string contendo o alfabeto com letras maiúsculas separado por espaços.
2- Percorra e imprima essa string com enumerate.
3- Substitua os espaços por traço. “-” e imprima para o usuário.

alfabeto = 'A B C D E F G H I J K L M N O P Q R S T U V X W Y Z'
print(alfabeto.replace(" ", "-"))

for k, v in enumerate(alfabeto):
    print(k, v)
'''
'''
Atividade de listas

1- Crie uma lista abaixo com a seguinte palavra:
“PYTHON”

a) A lista deve conter as letras separadas e em maiúsculas.
b) Crie uma nova lista somente com as três últimas letras da palavra “PYTHON”.

lista = ['P', 'Y', 'T', 'H', 'O', 'N']
nova_lista = lista [3: ]
print(nova_lista)
'''
'''
Atividade 2 de listas
1- Crie uma lista de móveis de uma casa;
2- Adicione um elemento no final da lista;
3- Remova um elemento pelo seu índice.

lista = ['cadeira', 'cama', 'TV', 'geladeira']
print(lista)
lista.append('mesa')
print(lista)
lista.pop(2)
print(lista)
'''

''' Atividade de Dicionarios

1- Crie um dicionário contendo dias da semana sendo dia1, dia2, dia3... as chaves e o dia seu valor. Ex: “dia1”: “domingo”.
a) Remova dois dos últimos dias da semana.
b) Remova segunda-feira pela sua chave.
c) Imprima chaves e valores do dicionário.
d) Imprima o dicionário final.

D_semana = {"dia1":"Domingo", "dia2":"Segunda-feira", "dia3":"Terça-feira", "dia4":"Quarta-feira", "dia5":"Quinta-feira", "dia6":"Sexta-feira", "dia7":"Sábado"}
# questão a
D_semana.popitem()
D_semana.popitem()
# questão b
del(D_semana["dia2"])
# questão c
print(D_semana.keys())
print(D_semana.values())
# questão d
print(D_semana)
'''

''' Atividade Funções
1- Crie uma função que receba dois parâmetros e realize sua soma, subtração, adição e multiplicação.
2- Informe esses resultados através de um print ao usuário dentro da função.
'''

def calculadora(a, b):
    soma = a + b
    subtração = a - b
    divisao = a / b
    multiplicacao = a * b

    print("Soma: ", soma)
    print("Subtração: ", subtração)
    print("Divisão: ", divisao)
    print("Multiplicação: ", multiplicacao)

calculadora(2, 4)