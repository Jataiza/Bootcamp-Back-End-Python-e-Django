'''Crie um dicionário representando contatos (nome, telefone).
Permita ao usuário procurar por um contato pelo nome.'''

contact = {'Nicolle': 19971279578, 'Noah': 19999999999, 'Jessica': '15988888888'}

search = input('Quem você deseja procurar? ')
if search in contact :
    print(f'A pessoa que procura é {search} e seu número de contato é {contact[search]}')
else :
    print(f'Não encontramos o contato de nome {search}')