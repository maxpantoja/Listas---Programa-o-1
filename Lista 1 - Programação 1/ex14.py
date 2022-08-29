print("=-="*23)
print('''Este programa verifica se a pesca ocorreu dentro do limite estabelecido
e, se tiver excedido, calcula a multa total a ser paga.''')
print("=-="*23)
peso = float(input("Informe quantos quilos você pescou (em Kg): "))
print("-" * 70)
if peso > 50:
    excesso = peso - 50
    multa = excesso * 4
    print('''Você ultrapassou o peso estabelecido pelo estado de São Paulo (50Kg).
Devido a isso, terás que pagar uma multa, como previsto no regulamento.
R$4,00 por cada quilo excedente.''')
    print("-" * 70)
    print(f"Peso de sua pesca: {peso}Kg")
    print(f"Peso excedente: {excesso:.2f}Kg")
    print(f"Multa: R${multa:.2f}")
else:
    print("Muito bem! Você está dentro do limite de pesca estabelecido (50Kg).")
