print("=-="*20)
print("Este programa imprimi a média de 4 notas informadas.")
print("=-="*20)
lista = []
for i in range(4):
    lista.append(float(input(f"Digite a {i+1}ª nota: ")))
print(f"A média das notas é: {sum(lista)/len(lista)}")
