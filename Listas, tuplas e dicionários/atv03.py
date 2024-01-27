'''Crie um dicionário representando um carrinho de compras.
Adicione produtos (chaves) e quantidades (valores) ao carrinho.
Calcule o total do carrinho de compra.'''

carrinho_de_compras = {
    "Maçã": 3,
    "Banana": 2,
    "Laranja": 1,
    "Abacaxi": 1
}

# Definindo os preços dos produtos
precos = {
    "Maçã": 2.50,
    "Banana": 1.50,
    "Laranja": 3.00,
    "Abacaxi": 4.00
}

def calcular_total(carrinho, precos):
    total = 0
    for produto, quantidade in carrinho.items():
        if produto in precos:
            total += quantidade * precos[produto]
        else:
            print(f"O preço para {produto} não está definido.")
    return total

total_do_carrinho = calcular_total(carrinho_de_compras, precos)
print(f"O total do carrinho de compras é: R$ {total_do_carrinho:.2f}")
