''' Receba do usuário a quantidade de litros de combustível consumidos e
a distância percorrida. Calcule e imprima o consumo médio em km/l.'''


# Solicita a quantidade de litros de combustível consumidos

litros_consumidos = float(input("Digite a quantidade de litros de combustível consumidos: "))
 
 # Solicita a distância percorrida
distancia_percorrida = float(input("Digite a distância percorrida em quilômetros: "))


# Calcula o valor médio
consumo_medio = distancia_percorrida / litros_consumidos 

# Exibe o resultado
print(f"O consumo médio é de {consumo_medio:.2f} km/l") 
 #