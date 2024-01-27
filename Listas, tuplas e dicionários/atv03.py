'''Crie um dicionário representando um carrinho de compras.
Adicione produtos (chaves) e quantidades (valores) ao carrinho.
Calcule o total do carrinho de compra.'''

shopping = {'cropped': 50, 'calça': 120.99, 'moletom': 100.89,
             'maiô': 89.9, 'vela aromatica': 30.5, 'blayblade': 79.9}

carrinho = []


while True:
    buy = input('Nós temos: cropped, calça, moletom, maiô, vela aromatica e blayblade \nO que da lista você deseja comprar? Ou digite x para sair: ')
    if buy == "x":
        break
    elif buy in shopping :
        carrinho.append(shopping[buy])
        total = sum(carrinho)
        print(f'Esse é o total do seu carrinho {total} BRL')
        
    else:
        print('Não temos esse produto, confira a lista e digite novamente')