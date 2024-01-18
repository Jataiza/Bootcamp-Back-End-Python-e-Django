'''Escreva um programa que calcule o salário líquido. Lembrando de
declarar o salário bruto e o percentual de desconto do Imposto de
Renda.
● Renda até R$ 1.903,98: isento de imposto de renda;
● Renda entre R$ 1.903,99 e R$ 2.826,65: alíquota de 7,5%;
● Renda entre R$ 2.826,66 e R$ 3.751,05: alíquota de 15%;
● Renda entre R$ 3.751,06 e R$ 4.664,68: alíquota de 22,5%;
● Renda acima de R$ 4.664,68: alíquota máxima de 27,5%.'''

try:
    # Solicita o salário bruto
    salario_bruto = float(input("Digite o salário bruto: "))

    # Calcula o desconto do Imposto de Renda com base na faixa salarial
    if salario_bruto <= 1903.98:
        percentual_desconto_ir = 0
    elif salario_bruto <= 2826.65:
        percentual_desconto_ir = 7.5
    elif salario_bruto <= 3751.05:
        percentual_desconto_ir = 15
    elif salario_bruto <= 4664.68:
        percentual_desconto_ir = 22.5
    else:
        percentual_desconto_ir = 27.5

    # Calcula o desconto do Imposto de Renda
    desconto_ir = salario_bruto * (percentual_desconto_ir / 100)

    # Calcula o salário líquido
    salario_liquido = salario_bruto - desconto_ir

    # Exibe o resultado
    print(f"Salário Líquido: R$ {salario_liquido:.2f}")
    print(f"Desconto do Imposto de Renda: R$ {desconto_ir:.2f}")

except ValueError as ve:
    print(f"Erro: {ve}. Certifique-se de inserir um valor válido para o salário bruto.")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")

