print("=-="*26)
print("Este programa calcula a quantidade de latas necessárias para pintar uma parede.")
print("=-="*26)
area = float(input("Informe a área a ser pintada(m²): "))
latas = (area / 3)/18
if latas - int(latas) != 0:
    latas = int(latas) + 1
else:
    latas = int(latas)
print(f"Quantidade de latas para realizar a pintura: {latas} latas.")
print(f"Valor Total a ser pago (R$80,00 cada): R${latas*80:.2f}")
