saltos = []
for i in range(5):
    saltos.append(float(input(f"{i+1}º salto (m): ")))
nome = input("Informe o nome do atleta: ")
print(f'''
Atleta: {nome}

Primeiro salto:   {saltos[0]}m
Segundo salto:    {saltos[1]}m
Terceiro salto:   {saltos[2]}m
Quarto salto:     {saltos[3]}m
Quinto salto:     {saltos[4]}m

Melhor salto:     {max(saltos)}m
Pior salto:       {min(saltos)}m
Média dos demais: {(sum(saltos)-max(saltos)-min(saltos))/3}

Resultado final:
{nome}: {(sum(saltos)-max(saltos)-min(saltos))/3}m''')