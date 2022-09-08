tipo = input("Tipo do combustível G-Gasolina e A-Alcool: ")
litros = float(input("Qtd de litros: "))
if tipo.upper() == "G":
    if litros <= 20:
        valor = (litros * 2.5) - (0.04*2.5*int(litros))
    else:
        valor = (litros * 2.5) - (0.06*2.5*int(litros))
    print(f"O valor a ser pago é: R${valor:.2f}")
elif tipo.upper() == "A":
    if litros <= 20:
        valor = (litros * 1.9) - (0.03*1.9*int(litros))
    else:
        valor = (litros * 1.9) - (0.05*1.9*int(litros))
    print(f"O valor a ser pago é: R${valor:.2f}")
