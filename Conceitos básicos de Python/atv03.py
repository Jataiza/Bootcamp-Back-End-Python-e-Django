# Faça um Programa que peça a quantidade de quilômetros, transforme em metros, centímetros e milímetros.

km = float(input('Digite a quantidade de quilômetros: '))


metros = km*1000
centimetros = metros*100
milimetros = centimetros*10


print(km, ' KM é correspondente a: ', metros, ' metros, ',
      centimetros, ' centimetros, ', milimetros, 'milimetros')
