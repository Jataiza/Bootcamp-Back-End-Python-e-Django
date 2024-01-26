'''Crie um programa que leia quanto dinheiro uma pessoa tem na
carteira, e calcule quanto poderia comprar de cada moeda estrangeira.
Considere a tabela de conversão abaixo:
Dólar Americano: R$ 4,91
Peso Argentino: R$ 0,02
Dólar Australiano: R$ 3,18
Dólar Canadense: R$ 3,64
Franco Suiço: R$ 0,42
Euro: R$ 5,36
Libra esterlina: R$ 6,21'''

bankAcount = float(2350.23)

def usd (bankAcount):
    convertCoin = round(bankAcount*0.20,2)
    print(convertCoin)
    return convertCoin

def arp (bankAcount):
    convertCoin = round(bankAcount*167.62,2)
    print(convertCoin)
    return convertCoin

def aus (bankAcount):
    convertCoin = round(bankAcount*0.31,2)
    print(convertCoin)
    return convertCoin

def cad (bankAcount):
    convertCoin = round(bankAcount*0.27,2)
    print(convertCoin)
    return convertCoin

def chf (bankAcount):
    convertCoin = round(bankAcount*0.18,2)
    print(convertCoin)
    return convertCoin

def eur (bankAcount):
    convertCoin = round(bankAcount*0.19,2)
    print(convertCoin)
    return convertCoin

def gbp (bankAcount):
    convertCoin = round(bankAcount*0.16,2)
    print(convertCoin)
    return convertCoin

doYouWant = input('Quer converter seu dinheiro? S para Sim e N para Não: ').upper()

if doYouWant == 'S' :
    coin = input('Insira: \nUSD para Dólar Americano \nARP para Peso Argentino \nAUS para Dólar Australiano \nCAD para Dólar Canadense \nCHF para Franco Suiço \nEUR para Euro \nGBP para Libra esterlina: ').upper()
    if coin == 'USD':
        conversor = usd(bankAcount)
        print(f'Você tem R${bankAcount} na sua carteira que convertendo para Dólar americano fica USD {conversor}')

    elif coin == 'ARP':
        conversor = arp(bankAcount)
        print(f'Você tem R${bankAcount} na sua carteira que convertendo para Dólar americano fica ARP {conversor}')
    
    elif coin == 'AUS':
        conversor = aus(bankAcount)
        print(f'Você tem R${bankAcount} na sua carteira que convertendo para Dólar americano fica AUS {conversor}')
    
    elif coin == 'CAD':
        conversor = cad(bankAcount)
        print(f'Você tem R${bankAcount} na sua carteira que convertendo para Dólar americano fica CAD {conversor}')
    
    elif coin == 'CHF':
        conversor = chf(bankAcount)
        print(f'Você tem R${bankAcount} na sua carteira que convertendo para Dólar americano fica CHF {conversor}')
    
    elif coin == 'EUR':
        conversor = eur(bankAcount)
        print(f'Você tem R${bankAcount} na sua carteira que convertendo para Dólar americano fica EUR {conversor}')
    
    elif coin == 'GBP':
        conversor = gbp(bankAcount)
        print(f'Você tem R${bankAcount} na sua carteira que convertendo para Dólar americano fica GBP {conversor}')
    
    else :
        print('Não reconhecemos essa moeda, tente novamente')

elif doYouWant == 'N' :
    StopIteration
else :
    print('Este não é um valor válido, tente novamente')