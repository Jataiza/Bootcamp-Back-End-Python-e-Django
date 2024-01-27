'''Faça um programa que lê três números inteiros e os mostra em ordem
crescente.'''

def ler_numeros():
    num1 = int(input("Digite o primeiro número inteiro: "))
    num2 = int(input("Digite o segundo número inteiro: "))
    num3 = int(input("Digite o terceiro número inteiro: "))
    return num1, num2, num3


def mostrar_ordem_crescente(num1, num2, num3):
    lista_numeros = [num1, num2, num3]
    lista_numeros.sort()
    print("Números em ordem crescente:", lista_numeros)


def main():
    numeros = ler_numeros()
    mostrar_ordem_crescente(*numeros)

main()
