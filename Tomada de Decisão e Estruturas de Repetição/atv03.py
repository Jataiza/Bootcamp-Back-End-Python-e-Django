# Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.


while True:
    nota = -1
    nota_str = input("Digite uma nota (0 a 10): ")

    if nota_str.find(".") >= 0 or nota_str.find(",") >= 0:
        print("Digite um número inteiro")
        continue
    else:
        nota = int(nota_str)

    if (nota > 0) and (nota < 10):
        print("Valor válido!")
        break
    else:
        print("Valor inválido!")
        continue
