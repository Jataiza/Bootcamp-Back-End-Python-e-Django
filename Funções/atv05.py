''' Crie uma função chamada contar_vogais que recebe uma string como parâmetro.Implemente a lógica para contar o número de vogais na string e retorne o total de vogais. Solicite ao usuário para inserir uma frase e utilize a função para contar as vogais.'''

def contar_vogais(frase):
    vogais = []
    for letra in frase:
        if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
            vogais.append(letra)
    
    return len(vogais)

def main():
    frase_escolhida = input("Digite uma frase: ")

    quantidade_de_vogais = contar_vogais(frase_escolhida)
    print(f'A frase digitada contém {quantidade_de_vogais} vogais.')


main()
