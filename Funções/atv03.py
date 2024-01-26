'''Escreva um script que pergunta ao usuário se ele deseja converter
uma temperatura de grau Celsius para Fahrenheit ou vice-versa. Para
cada opção, crie uma função
Plus: Crie uma terceira, que é um menu para o usuário escolher a opção
desejada, onde esse menu chama a função de conversão correta.'''

def celFah (celsius):
    convertCToF = (celsius*1.8)+32
    return convertCToF

def fahCel (fahrenheit):
    convertFToC = (fahrenheit-32)/1.8
    return convertFToC

convertType = input('Digite C se deseja transformar Celsius em Fahrenheit, e F se deseja tranformar Fahrenheit em Celsius: ').upper()

if convertType == 'C' :
    celsius = float(input('Quantos graus celsius? '))
    conversor = celFah(celsius)
    print(f'A temperatura de {celsius} celsius para fahrenheit é {conversor}')

elif convertType == 'F' :
    fahrenheit = float(input('Quantos graus fahrenheit? '))
    conversor = fahCel(fahrenheit)
    print(f'A temperatura de {fahrenheit} fahrenheit para celsius é {conversor}')

else :
    print('Este não é um valor válido, tente novamente')