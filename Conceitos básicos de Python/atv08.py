# Faça um Programa que pergunte quanto você ganha por hora e o
# número de horas trabalhadas no mês.Calcule e mostre o total do seu salário no referido mês.

horas_trabalhadas = int(input('Quantas horas trabalhou no mês: '))
ganho_hora = float(input('Qual o valor do salário em horas: '))

total_salario = horas_trabalhadas * ganho_hora

print(f'O salário total no mês será de: {total_salario:.2f}')

