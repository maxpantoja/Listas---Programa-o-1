print("Projeção de Gastos com Abonno\n" + "=" * 20)
lista = [[], []]
x = float(input("Salário: R$"))
while x != 0:
    lista[1].append(x * 0.2 if (x * 0.2) > 100 else 100)
    lista[0].append(x)
    x = float(input("Salário: R$"))
print("\nSalário          Abono")
for i in range(len(lista[0])):
    print(f"R${lista[0][i]:.2f}" + " " * (13 - len(str(lista[0][i]))) + f"R${lista[1][i]:.2f}")
print(f'''
Foram processados {len(lista[0])} colaboradores
Total gasto com abonos: R${sum(lista[1])}
Valor mínimo pago a {lista[1].count(100):.2f} colaboradores
Maior valor de abono pago: R${max(lista[1]):.2f}''')
