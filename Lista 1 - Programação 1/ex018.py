print("=-="*22)
print("Este programa calcula o tempo aproximado de download de um arquivo.")
print("=-="*22)
arquivo = float(input("Insira o tamanho do arquivo (em MB): "))
velocidade = float(input("Insira a velocidade de seu link de internet (em Mbps): "))
tempo = (arquivo * 8) / velocidade
print(f"O tempo necessário para realizar o download será de: {tempo/60:.2f} minutos")
