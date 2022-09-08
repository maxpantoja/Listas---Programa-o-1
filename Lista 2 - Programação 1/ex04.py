n1 = float(input("Informe a primeira nota do aluno: "))
n2 = float(input("Informa a segunda nota do aluno: "))
media =(n1 + n2) / 2
if media >= 9:
    print("Conceito A - APROVADO")
elif media >= 7.5:
    print("Conceito B - APROVADO")
elif media >= 6:
    print("Conceito C - APROVADO")
elif media >= 4:
    print("Conceito D - REPROVADO")
else:
    print("Conceito E - REPROVADO")