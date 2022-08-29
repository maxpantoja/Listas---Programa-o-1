print("=-="*24)
print("Este programa verifica a melhor opção de compras para pintar uma parede.")
print("=-="*24)
modelo1 = 18
modelo2 = 3.8
area = float(input("Informe a área a ser pintada(m²): "))
latas1 = (area/6)/modelo1
if latas1 - int(latas1) != 0:
    latas1 = int(latas1) + 1
else:
    latas1 = int(latas1)
latas2 = (area/6)/modelo2
if latas2 - int(latas2) != 0:
    latas2 = int(latas2) + 1
else:
    latas2 = int(latas2)
tinta = area/6
print(f"Quantidade de Tinta Necessária: {tinta}")
listax = [0, 0, tinta * 10]
listap = [0, 0, tinta * 100]
for i in range(latas1 + 2):
    volume = 0
    if listap[2] - tinta >= listax[2] - tinta:
        listap = listax
    j = 0
    while j < (latas2 + 1):
        if tinta > volume:
            volume = (modelo1 * i) + (modelo2 * j)
            # print(f"Volume: {volume}")
        if volume*6/area >= 0.9:
            listax = [i, j, volume]
            j = latas2 * 2 + 2
        j += 1

print(f"Lista principal final: {listap}")

print("=+="*15)
print("TABELA COM COMBINAÇÕES POSSÍVEL E SEUS PREÇOS")
print("=+="*15)
print(f"# Comprando apenas Latas de 18l: {latas1} latas, Valor: R${latas1 * 80}")
print(f"# Comprando apenas Galões de 3.6l: {latas2} galões, Valor: R${latas2 * 25}")
print(f'''# Mistura de Latas e Galões, de forma que o desperdício de tinta seja menor:
{listap[0]} latas de 18l e {listap[1]} galões de 3.6l, Valor total: R${(listap[0] * 80) + (listap[1] * 25)}''')
