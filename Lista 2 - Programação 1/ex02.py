salario = float(input("Hora funcionário: R$")) * float(input("Horas trabalhadas: "))
if salario <= 900:
    ir = 0
elif salario <= 1500:
    ir = 0.05
elif salario <= 2500:
    ir = 0.1
else:
    ir = 0.2
print(f"Salário Bruto                             : R${salario:.2f}")
print(f"(-) IR ({ir*100}%)                              : R${salario*ir}")
print(f"(-) INSS (10%)                            : R${salario*0.1}")
print(f"FGTS (11%)                                : R${salario * 0.11}")
print(f"Salário Líquido                           : R${salario*(ir+0.1)}")
