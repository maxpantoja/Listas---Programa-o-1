lista = [[], []]
for i in range(5):
    lista[0].append(input("Nome do carro: "))
    lista[1].append(float(input("Informe o consumo (km/l): ")))
print("\nComparativo de Consumo de Combustível")
for i in range(5):
    print(f"Veículo {i+1}\nNome: {lista[0][i]}\nKm/l: {lista[1][i]}")
print("\nRelatório")
for i in range(5):
    print(f"{i+1} - {lista[0][i]}  -  {lista[1][i]} - {1000/lista[1][i]:.2f} litros - R${(1000/lista[1][i])*2.25:.2f}")
print(f"O menor consumo é do {lista[0][lista[1].index(max(lista[1]))]}")
