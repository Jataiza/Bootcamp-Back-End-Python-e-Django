'''Faça um programa que permita ao usuário digitar o seu nome e em seguida mostre o nome do usuário de trás para frente utilizando somente letras maiúsculas. Dica:lembre−se que ao informar o nome ous uário pode digitar letras maiúsculas ou minúsculas.'''

nome = (input("Digite seu nome: ")).upper()

nomeAoContrario = ""

for letra in nome:
    nomeAoContrario = letra + nomeAoContrario

print(nomeAoContrario)