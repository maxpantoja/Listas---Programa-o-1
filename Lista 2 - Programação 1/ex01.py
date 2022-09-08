salario = float(input("Digite o salário atual do funcionário: "))
if salario <= 280:
    y = 0.2
elif salario <= 700:
    y = 0.15
elif salario <= 1500:
    y = 0.1
else:
    y = 0.05
print(f"Salário antes do reajuste: R${salario}")
print(f"Percentual de aumento aplicado: {y*100}%")
print(f"Valor do aumento: R${salario*y}")
print(f"Novo salário: R${salario + salario*y}")
