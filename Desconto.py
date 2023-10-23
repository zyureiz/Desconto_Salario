def calcular_desconto_salario(salario):
    if salario <= 1320:
        desconto = salario * 0.05  # 5% de imposto
    elif salario <= 2000:
        desconto = salario * 0.10  # 10% de imposto
    elif salario <= 3000:
        desconto = salario * 0.15  # 15% de imposto
    elif salario <= 6000:
        desconto = salario * 0.20  # 20% de imposto
    else:
        desconto = salario * 0.25  # 25% de imposto
    
    salario_liquido = salario - desconto
    return salario_liquido

# Solicitar ao usuário que insira o salário
salario = float(input("\nDigite o salário(em reais): "))

# Calcular o salário líquido após o desconto de imposto
salario_liquido = calcular_desconto_salario(salario)

# Exibir o valor líquido
print("\nO Valor líquido após desconto é de: R$",salario_liquido)
print("\n")