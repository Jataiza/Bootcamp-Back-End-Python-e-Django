'''Crie duas tuplas. Concatene-as para formar uma nova tupla'''

tuplaNumbers1 = (1,2,3,7,8,9)
tuplaNumbers2 = (4,5,6,10,11,12)

print(f'Tupla 1: {tuplaNumbers1}, \nTupla 2: {tuplaNumbers2}.' )

sumTupla = sum((tuplaNumbers1,tuplaNumbers2),())

print(f'A junção das tuplas é: {sumTupla}')