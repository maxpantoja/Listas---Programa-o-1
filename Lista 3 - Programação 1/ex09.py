lista = [['Necessita de esfera', 'Necessita de limpeza', 'Necessita troca de cabo ou conector',
          'Quebrado ou inutilizado'], [0, 0, 0, 0]]
print("Códigos de problemas: 1-Esfera; 2-Limpeza; 3-Cabo ou Conector; 4-Quebrado ou Inutilizado; 0-Finalizar")
x = int(input("Código da situação do mouse 1: "))
while x != 0:
    lista[1][x-1] += 1
    x = int(input("Código da situação do mouse 1: "))
print(f"\nQauntidade de mouses: {sum(lista[1])}\nSituação                                    Quantidade    Percentual")
for i in range(4):
    print(f"{i+1} - {lista[0][i]}" + " " * (45 - len(lista[0][i])) + f"{lista[1][i]}           "
                                                                     f"{(float(lista[1][i])/sum(lista[1])) * 100:.2f}%")
