def classifica_pessoa(nivel_culpa):
    if nivel_culpa < 2:
        print('\nInocente')
    elif nivel_culpa == 2:
        print('\nSuspeita')
    elif nivel_culpa >= 3 and nivel_culpa < 5:
        print('\nCúmplice')
    else:
        print('\nAssassino')

perguntas = ['Telefonou para a vítima?', 'Esteve no local do crime?', 'Mora perto da vítima?', 'Devia para a vítima?', 'Já trabalhou com a vítima?']
respostas = []
nivel_culpa = 0

for pergunta in perguntas:
    resposta = input(f'{pergunta} ')
    respostas.append(resposta)

for resposta in respostas:
    if resposta == 'sim' or resposta == 'Sim':
        nivel_culpa += 1

classifica_pessoa(nivel_culpa)
