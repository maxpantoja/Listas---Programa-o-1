print("Escolha o tipo de carne informando o número correspondente.")
tipo = int(input("(1)Filé Duplo  (2)Alcatra  (3)Picanha\nR: "))
kg = float(input("Quantidade Kg: "))
forma = int(input("Forma de pagamento: (1)Cartão Tabajara (2)Outros\nR: "))
if tipo == 1:
    if kg <= 5:
        preco = 4.9
    else:
        preco = 5.8
    tipo = "Filé Duplo"
elif tipo == 2:
    if kg <= 5:
        preco = 5.9
    else:
        preco = 6.8
    tipo = "Alcatra"
elif tipo == 3:
    if kg <= 5:
        preco = 6.9
    else:
        preco = 7.8
    tipo = "Picanha"
else:
    preco = 0
    tipo = "Não encontrado"
if forma == 1:
    total = kg * preco * 0.95
    desc = kg * preco * 0.05
    pag = "Cartão Tabajara"
else:
    total = kg * preco
    desc = 0
    pag = "Outros"
print(f'''Carne comprada: {tipo}
Quantidade: {kg}Kg
Preço total: R${kg * preco:.2f}
Forma de pagamento: {pag}
Desconto: R${desc:.2f}
Valor a pagar: R${total:.2f}''')




