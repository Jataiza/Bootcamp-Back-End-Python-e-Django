# Desenvolva um programa que solicite ao usuário os comprimentos dos três
# lados de um triângulo e classifique-o como equilátero, isósceles ou escaleno.
# equilátero: todos os lados com o mesmo valor
# isósceles: dois lados com o mesmo valor
# escaleno: todos os lados com medidas distintas.

lado1 = int(input("Digite o primeiro lado: "))
lado2 = int(input("Digite o segundo lado: "))
lado3 = int(input("Digite o terceiro lado: "))

if lado1 == lado2 and lado2 == lado3 and lado1 == lado3:
    print("Triângulo equilátero")
elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
    print("Triângulo isósceles")
else:
    print("Triângulo escaleno")
