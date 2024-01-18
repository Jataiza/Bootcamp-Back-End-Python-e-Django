'''Solicite ao usuário o peso em kg e a altura em metros. Calcule e
imprima o Índice de Massa Corporal (IMC) usando a fórmula:
IMC = peso / (altura x altura).'''


while True:
    try:
        # Solicita o peso e a altura ao usuário
        peso = float(input("Digite o peso em kg: "))
        altura = float(input("Digite a altura em metros:"))

        # Verifica se o peso e a altura são valores positivos
        if peso <= 0 or altura <= 0:
            raise ValueError("O peso e a altura devem ser valores positivos.")

        # Calcula o Índice de Massa Corporal (IMC)
        imc = peso / (altura ** 2)

        # Exibe o resultado
        print(f"Seu Índice de Massa Corporal (IMC) é: {imc:.2f}")

    except ValueError as ve:
        print(f"Erro: {ve}. Certifique-se de inserir valores válidos para peso e altura.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

    # Pergunta se deseja calcular o IMC novamente
    resposta = input("Deseja calcular o IMC novamente? (s/n): ")
    if resposta.lower() != "s":
        break
