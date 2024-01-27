'''Crie um programa que leia quanto dinheiro uma pessoa tem na carteira, e calcule quanto poderia comprar de cada moeda estrangeira.
Considere a tabela de conversão abaixo:
Dólar Americano: R$ 4,91
Peso Argentino: R$ 0,02
Dólar Australiano: R$ 3,18
Dólar Canadense: R$ 3,64
Franco Suiço: R$ 0,42
Euro: R$ 5,36
Libra esterlina: R$ 6,21'''


def calcular_moedas(valor_em_reais):
    conversao = {
        "Dólar Americano": 4.91,
        "Peso Argentino": 0.02,
        "Dólar Australiano": 3.18,
        "Dólar Canadense": 3.64,
        "Franco Suiço": 0.42,
        "Euro": 5.36,
        "Libra esterlina": 6.21
    }

    for moeda, taxa in conversao.items():
        valor_em_moeda = valor_em_reais / taxa
        print(f"Com R$ {valor_em_reais:.2f}, você pode comprar aproximadamente {valor_em_moeda:.2f} {moeda}.")

def main():
    try:
        valor_em_reais = float(input("Digite o valor em reais que você tem na carteira: "))
        calcular_moedas(valor_em_reais)
    except ValueError:
        print("Por favor, insira um valor válido.")

if __name__ == "__main__":
    main()

