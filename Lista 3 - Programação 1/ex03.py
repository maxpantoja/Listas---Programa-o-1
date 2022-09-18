lista = [[1, 2, 3, 4, 5, 6], ["Lula", "Bolsonaro", "Simone", "Ciro", "Nulo", "Branco"], [0, 0, 0, 0, 0, 0]]
voto = -1
while voto != 0:
    if voto in lista[0]:
        lista[2][lista[0].index(voto)] += 1
    voto = int(input("Opções: 1-Lula / 2-Bolsonaro / 3-Simone / 4-Ciro / 5-Nulo / 6-Branco\nVoto: "))
print("\nTABELA DE VOTOS")
for i in range(6):
    print(f"{lista[1][i]}: {lista[2][i]}")
print(f"\nPorcentagem de votos NULOS sobre o total: {(lista[2][4] / sum(lista[2])) * 100:.2f}%")
print(f"Porcentagem de votos BRANCOS sobre o total: {(lista[2][5] / sum(lista[2])) * 100:.2f}%")
