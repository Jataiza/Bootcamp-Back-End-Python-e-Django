'''Faça um Programa que peça as quatro notas de 5 alunos, calcule
e armazene numa lista a média de cada aluno, imprima o número
de alunos com média maior ou igual a 7.0'''

medias_alunos = [] 

for i in range(5):
    print(f"Informe as quatro notas do aluno {i + 1}:")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    nota3 = float(input("Nota 3: "))
    nota4 = float(input("Nota 4:"))

    
    media = (nota1 + nota2 + nota3 + nota4) / 4 
    medias_alunos.append(media)


alunos_aprovados = sum(media >= 7.0 for media in medias_alunos) 

print(f"\nNúmero de alunos com média maior ou igual a 7.0: {alunos_aprovados}")
