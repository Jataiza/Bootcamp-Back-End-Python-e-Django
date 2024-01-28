
horas_exercicio = int(input('Digite o número de horas que você se exercita na semana: '))


minutos_de_exercicio_por_semana = horas_exercicio*60
calorias_por_minuto = 5
semanas_no_mes = 4

calorias = (minutos_de_exercicio_por_semana*calorias_por_minuto)*semanas_no_mes

print('Você gasta ',calorias," calorias em 1 mês")
