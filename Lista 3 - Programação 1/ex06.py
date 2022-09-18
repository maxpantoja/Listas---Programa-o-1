notas = []
for i in range(7):
    notas.append(float(input(f"{i+1}º nota: ")))
nome = input("Informe o nome do atleta: ")
print(f"\nAtleta: {nome}")
for i in range(7):
    print(f"Nota {i+1}: {notas[i]}")
print(f'''
RESULTADO FINAL:
Melhor nota:      {max(notas)}m
Pior nota:        {min(notas)}m
Média:            {(sum(notas)-max(notas)-min(notas))/5}''')
