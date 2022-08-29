print("=-="*23)
print("Este programa calcula o peso ideal de uma pessoa considerando o sexo.")
print("=-="*23)
sexo = input("Qual o seu sexo?\n(M) para Masculino   (F) para Feminino\nResposta: ")
if sexo.upper() == "M" or sexo.upper() == "F":
    h = float(input("Digite sua altura (em metros): "))
    if sexo.upper() == "M":
        print(f"O peso ideal para a altura de {h} m é de {72.7*h-58:.2f} Kg")
    else:
        print(f"O peso ideal para a altura de {h} m é de {62.1 * h - 44.7:.2f} Kg")
else:
    print("Você não digitou um sexo válido. Tente novamente.")
