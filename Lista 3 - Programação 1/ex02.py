lista = [[100, 101, 102, 103, 104, 105], [1.2, 1.3, 1.5, 1.2, 1.3, 1], [0, 0, 0, 0, 0, 0], ["Cachorro Quente",
                                                                                            "Bauru Simples",
                                                                                            "Bauru com ovo",
                                                                                            "Hambúrguer",
                                                                                            "Cheeseburger",
                                                                                            "Refrigerante"]]
print("ATENÇÃO: Para encerrar a compra, basta digitar o código: 0")
print("=+" * 30 + "\n" + " " * 17 + "CARDÁPIO DA LANCHONETE" + "\n" + "=+" * 30)
print('''           Cod Especificação           Preço
           100 Cachorro Quente        R$ 1,20
           101 Bauru Simples          R$ 1,30
           102 Bauru com ovo          R$ 1,50
           103 Hambúrguer             R$ 1,20
           104 Cheeseburguer          R$ 1,30
           105 Refrigerante           R$ 1,00''')
print("=="*31)
x = int(input("Informe o código do produto que desejas comprar: "))
while x != 0:
    lista[2][lista[0].index(x)] += int(input("Qtd: "))
    x = int(input("Informe o código do produto que desejas comprar: "))
print("="*30 + "\n      RESULTADO DO PEDIDO\n" + "=" * 30)
total = 0
for i in range(6):
    if lista[2][i] != 0:
        print(f"{lista[3][i]}: R${lista[1][i] * lista[2][i]:.2f}")
        total += lista[1][i] * lista[2][i]
print(f"\nValor total do pedido: R${total:.2f}")
