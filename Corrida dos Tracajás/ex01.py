n = 0
lista = []
while n not in range(1, 51):
    n = int(input("Infome o número de tracajás (Mínimo 1 e máximo 50): "))
for i in range(n):
    x = 0
    while x not in range(1, 26):
        x = float(input(f"Informe a velocidade do Tracajá Nº{i+1} (Mínimo 1Km/h e máximo 25Km/h): "))
    lista.append(x)
maior = max(lista)
if maior < 10:
    print("Nível do Tracajá mais veloz é: Nível 1")
elif maior < 15:
    print("Nível do Tracajá mais veloz é: Nível 2")
elif maior >= 15:
    print("Nível do Tracajá mais veloz é: Nível 3")
