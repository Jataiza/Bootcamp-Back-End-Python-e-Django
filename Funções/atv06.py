import random 

lista = ['coelho', 'pato', 'tamandua', 'lagartixa', 'jabuti', 'morcego', 'lobo', 'grilo', 'baleia', 'gato', 'sapo', 'coruja']
letras = []
espacos = []
rodada = 1
palpite_certo = False

# busca a letra na lista de letras da palavra secreta 
def busca_palpite(letra):
    letra_encotrada = False
    for i in range(len(letras)):
        if(letras[i] == letra):
            espacos[i] = letra
            letra_encotrada = True
    return letra_encotrada

# verifica se ainda restam espaços para continuar o jogo
def tem_espacos():
    for espaco in espacos:
        if espaco == '_':
            return True        
    return False

# recebe uma palavra do usuaria e verifica se é igual a palavra secreta
def chutar_palavra():
    entrada = input('Está pronta?\nQual o seu chute?\n')
    chute = entrada.lower()
    if(chute == palavra_secreta):
        print('Parabéns! Você acertou! \ó/\õ/\ô/\n')
        return True
    else:
        print('Não foi dessa vez! :c\n')
        return False


# selecionando um item aleatório da lista como string 
palavra_aleatoria = str(random.sample(lista, 1))

# retirando os caracteres [, ', ' e ] da string
palavra_secreta = palavra_aleatoria[2:-2]

# colocando cada caractere da palavra como item da lista letras e um lista de tamanho correspondente com apenas espaços
for caractere in palavra_secreta:
    letras.append(caractere)
    espacos.append('_')

# intrucoes iniciais
print('### JOGO DA FORCA ###\nAdivinhe qual palavra preenche os espaços.\nInstruções: Você terá 6 chances de acertar. A cada rodada pode escolher uma letra. Caso a palavra possua a letra escolhida, ela será colocada no espaço correspondente e então você decide se chuta um resposta ou não.\nBoa sorte! c:\tDica: é um animal :D')

# inicia o jogo com um loop para cada rodada
while rodada <= 6 and palpite_certo == False:
    print(f'\n### RODADA {rodada} ###\nQual a palavra? {espacos}\n')
    palpite = input("Digite uma letra: ")

    if busca_palpite(palpite):
        print(f'Bom palpite!\t{espacos}\n')
    else:
        print('Sinto muito :( Tente outra letra!\n')

    
    if tem_espacos():
        if rodada < 6:
            resposta = input('Já consegue adivinhar qual a palavra?\nDigite 1 para chutar ou enter para continuar: ')
            if resposta == '1':
                palpite_certo = chutar_palavra()
            else:
                print('Vamos continuar jogando! c:')
        else:
            print('Com está é a última rodada! É sua última chance!\n')
            palpite_certo = chutar_palavra()

        rodada += 1
    else:
        print('Parabéns! Você venceu! \ó/\õ/\ô/\n')
        palpite_certo = True
