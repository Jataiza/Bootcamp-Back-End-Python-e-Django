# Desenvolver um programa que solicite a idade do usuário e identifique se ele é uma criança, um adolescente, adulto ou idoso.
while True:
    idade = -1
    entrada = input("Digite sua idade: ")

    if entrada.find(".") >= 0 or entrada.find(",") >= 0:
        print("Digite um número inteiro")
    else:
        idade = int(entrada)

    if idade >= 60:
        print("Você é um idoso!")
        break
    elif idade >= 18:
        print("Você é um adulto!")
        break
    elif idade >= 12:
        print("Você é um adolescente!")
        break
    elif idade > 0:
        print("Você é uma criança!")
        break
    else:
        print("Idade inválida!")
