a = float(input("Informe o A da equação: "))
if a != 0:
    b = float(input("Informe o B da equação: "))
    c = float(input("Informe o C da equação: "))
    delta = b ** 2 -4 * a * c
    if delta < 0:
        print("A equação não possui raizes reais.")
    elif delta == 0:
        print("A equação possui apenas uma raiz real. x: ", -b / (2*a))
    else:
        print("x1 = ", (-b + delta**0.5) / (2 * a))
        print("x2 = ", (-b - delta**0.5) / (2 * a))
else:
    print("Considerando que o A=0, sua equação não é de segundo grau.")
