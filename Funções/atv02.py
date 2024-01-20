# 2. Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.

def reverso(numero):
    reverso = ''
    for digito in numero:
        reverso = digito + reverso
    return reverso

numero = input('Digite um numero: ')
print(f'Reverso do numero: {reverso(numero)}')