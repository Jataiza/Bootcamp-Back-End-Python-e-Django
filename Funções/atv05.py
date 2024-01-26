'''Crie uma função chamada contar_vogais que recebe uma string
como parâmetro. Implemente a lógica para contar o número de vogais
na string e retorne o total de vogais. Solicite ao usuário para inserir uma
frase e utilize a função para contar as vogais.
'''

def countVowels(text):
    vowels = 'aeiou'
    '''total = 0
    for i in vowels.upper() :
        total = total+text.count(i)'''
   # variavel = {i: text.count(i) for i in vowels.upper()}
    variavel = sum((text.count(i) for i in vowels.upper()))
    return variavel

text = input('Digite aqui sua frase favorita: ').upper()
totalVowels = countVowels(text)
print('o número de vogais nessa frase é: ', totalVowels)

