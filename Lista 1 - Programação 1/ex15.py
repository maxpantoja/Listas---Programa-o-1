print("=-="*19)
print("Este programa calcula o salário líquido de uma pessoa.")
print("=-="*19)
vh = float(input("Valor da hora: R$"))
h = float(input("Horas trabalhadas: "))
print("-"*100)
print(f"+Salário Bruto:   R${vh*h}")
print(f"-IR(11%):         R${vh*h*0.11}")
print(f"-INSS(8%):        R${vh*h*0.08}")
print(f"-Sindicato(5%):   R${vh*h*0.05}")
print(f"=Salário Líquido: R${vh*h*0.76}")
