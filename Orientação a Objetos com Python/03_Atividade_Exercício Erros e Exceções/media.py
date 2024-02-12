def calcular_media(valores):
    tamanho = len(valores)  # Obtém o número de elementos na lista valores
    soma = sum(valores)  # Calcula a soma de todos os valores na lista
    media = soma / tamanho if tamanho > 0 else 0  # Calcula a média, evitando a divisão por zero

    return media  # Retorna a média calculada

continuar = True  # Variável para controlar o loop de entrada de valores
valores = []  # Lista para armazenar os valores digitados pelo usuário

while continuar:  # Loop para continuar a solicitar valores até que o usuário decida calcular a média
    valor = input('Digite um número para entrar na sua média ou "OK" para calcular a média: ')  # Solicita ao usuário um valor ou a opção de calcular a média

    if valor.lower() == 'ok':  # Verifica se o usuário optou por calcular a média
        continuar = False  # Define continuar como False para sair do loop
    else:
        try:
            valores.append(float(valor))  # Converte o valor digitado para float e o adiciona à lista valores
        except ValueError:
            print("Por favor, digite um número válido.")  # Exibe uma mensagem de erro se o valor não puder ser convertido para float

media = calcular_media(valores)  # Chama a função calcular_media para calcular a média dos valores digitados
print('A média calculada para os valores {} foi de {:.2f}'.format(valores, media))  # Exibe a média calculada com dois dígitos após o ponto decimal
