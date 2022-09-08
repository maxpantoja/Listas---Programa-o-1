n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
print("\nOBS: As operações são feitas do primeiro com o segundo. Ex: primeiro - segundo")
x = int(input("Informe a operação que desejas realizar:\n(1) Soma  (2) Subtração  (3) Multiplicação  (4) Divisão\nR: "))
if x == 1:
    resultado = n1 + n2
elif x == 2:
    resultado = n1 - n2
elif x == 3:
    resultado = n1 * n2
elif x == 4:
    resultado = n1 / n2
else:
    resultado = "erro"
    print("O valor informado não corresponde a uma das opções.")
if resultado != "erro":
    print("Seu resultado é: ", resultado)
    if resultado - int(resultado) == 0:
        if resultado % 2 == 0:
            print("O resultado é par.")
        else:
            print("O resultado é ímpar.")
    else:
        print("Por o número ser decimal, ele não pode ser considerado Par ou Ímpar.")
    if resultado >= 0:
        print("O resultado é positivo.")
    else:
        print("O resultado é negativo.")
    if resultado - int(resultado) == 0:
        print("O resultado é inteiro.")
    else:
        print("O resultado é decimal.")
