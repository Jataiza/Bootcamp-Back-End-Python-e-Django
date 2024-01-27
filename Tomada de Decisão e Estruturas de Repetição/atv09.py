'''programa deve calcular e apresentar a quantidade de números pares e
ímpares inseridos. O processo de leitura deve ser encerrado quando o usuário
informar o valor zero. Certifique-se de incluir validações para garantir que
apenas números positivos sejam considerados na contagem e cálculos.'''

def contar_pares_impares():
    numeros_pares = 0
    numeros_impares = 0

    while True:
        numero = int(input("Digite um número (ou 0 para encerrar): "))

        if numero == 0:
            break  # Encerra o loop quando o usuário digita 0
        elif numero < 0:
            print("Por favor, digite apenas números positivos.")
            continue  # Pula para a próxima iteração do loop

        if numero % 2 == 0:
            numeros_pares += 1
        else:
            numeros_impares += 1

    print(f"Quantidade de números pares: {numeros_pares}")
    print(f"Quantidade de números ímpares: {numeros_impares}")

contar_pares_impares()
