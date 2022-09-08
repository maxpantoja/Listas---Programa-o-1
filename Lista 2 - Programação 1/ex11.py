valor = int(input("MÍNIMO 10 REAIS E MÁXIMO 600\nInsira um valor para saque: "))
if (valor - int(valor) == 0) and (valor >= 10) and (valor <= 600):
    print(f"Notas de 100: {valor // 100}")
    print(f"Notas de 50: {valor % 100 // 50}")
    print(f"Notas de 10: {valor % 100 % 50 // 10}")
    print(f"Notas de 05: {valor % 100 % 50 % 10 // 5}")
    print(f"Notas de 01: {valor % 100 % 50 % 10 % 5 // 1}")
else:
    print("O valor informado não condiz com as restrições.")
