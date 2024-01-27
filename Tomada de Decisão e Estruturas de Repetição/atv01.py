'''Faça um Programa que peça dois números e imprima o maior deles'''

number1 = int(input('Digite o primeiro número inteiro: '))
number2 = int(input('Digite o segundo número inteiro: '))

if number1 > number2 :
    print(f'O número {number1} é maior que {number2}')
elif number1 == number2 :
    print(f'O número {number1} e o {number2} são iguais')
else :
    print(f'O número {number2} é maior que {number1}')