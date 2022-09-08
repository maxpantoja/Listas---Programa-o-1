maca = float(input("Maça Kg: "))
morango = float(input("Morando Kg: "))
if maca <= 5:
    pmaca = 1.8
else:
    pmaca = 1.5
if morango <= 5:
    pmorango = 2.5
else:
    pmorango = 2.2
total = (maca * pmaca) + (morango * pmorango)
if morango + maca > 8 or total > 25:
    total *= 0.9
print(f"O preço total a ser pago será: R${total:.2f}")
