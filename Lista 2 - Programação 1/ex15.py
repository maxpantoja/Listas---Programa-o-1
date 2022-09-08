print("Digite 1 para SIM e 0 para NÃO.")
x1 = int(input("Telefonou para a vítima? R: "))
x2 = int(input("Esteve no local do crime? R: "))
x3 = int(input("Mora perto da vítima? R: "))
x4 = int(input("Devia para a vítima? R: "))
x5 = int(input("Já trabalhou com a vítima? R: "))
tese = x1 + x2 + x3 + x4 + x5
if tese == 5:
    print("A pessoa deve ser considerada como Assasina.")
elif tese >= 3:
    print("A pessoa deve ser considerada como Cúmplice.")
elif tese == 2:
    print("A pessoa deve ser considerada como Suspeita.")
else:
    print("A pessoa deve ser considerada como Inocente.")