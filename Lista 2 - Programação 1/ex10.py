n1 = float(input("Informe a primeira nota: "))
n2 = float(input("Informe a segunda nota: "))
n3 = float(input("Informe a terceira nota: "))
media = (n1 + n2 + n3) / 3
if media == 10:
    print(f"Aprovado com Distinção, atingindo uma média de {media}")
elif media >= 7:
    print(f"Aprovado, atingindo uma média de {media}")
else:
    print(f"Reprovado, atingindo uma média de {media}")
