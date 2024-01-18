'''Escreva um programa que calcule o tempo de uma viagem. Faça um
comparativo do mesmo percurso de avião, carro e ônibus.
Levando em consideração:
● avião = 600 km/h
● carro = 100 km/h
● ônibus = 80 km/h'''


try:
    # Solicita a distância da viagem ao usuário
    distancia_viagem = float(input("Digite a distância da viagem em quilômetros: "))

    # Calcula o tempo de viagem para cada meio de transporte
    velocidade_aviao = 600
    velocidade_carro = 100
    velocidade_onibus = 80

    tempo_aviao = distancia_viagem / velocidade_aviao
    tempo_carro = distancia_viagem / velocidade_carro
    tempo_onibus = distancia_viagem / velocidade_onibus

    # Exibe o resultado
    print(f"Tempo de viagem de avião: {tempo_aviao:.2f} horas")
    print(f"Tempo de viagem de carro: {tempo_carro:.2f} horas")
    print(f"Tempo de viagem de ônibus: {tempo_onibus:.2f} horas")

except ValueError as ve:
    print(f"Erro: {ve}. Certifique-se de inserir um valor válido para a distância.")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")
