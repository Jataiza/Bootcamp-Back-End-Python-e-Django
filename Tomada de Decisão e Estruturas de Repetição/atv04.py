while (True):
    nota = float(input('Digite a sua nota no exame, entre 0 e 10: '))
    if nota >= 0 and nota <= 10:
        break

if nota >= 7:
    print('Você foi aprovado! :)')
else:
    print('Você foi reprovado :(')
