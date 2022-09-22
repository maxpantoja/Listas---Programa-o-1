with open('usuarios.txt', 'r', encoding='utf-8') as f:
    matriz = [[], []]
    for linha in f:
        matriz[0].append((linha.replace('\n', '').split(' '))[0])
        matriz[1].append(int((linha.replace('\n', '').split(' '))[1]))
with open('relatório.txt', 'w', encoding='utf-8') as f:
    f.write('''ACME Inc.   Uso do espaço em disco pelos usuários
--------------------------------------------------
Nr. Usuário          Espaço utilizado    % do uso\n''')
    for i in range(len(matriz[0])):
        f.write(f'{i+1}   {matriz[0][i]}' + " " * (20 - len(matriz[0][i])) + f'{matriz[1][i]/1048576:.2f} MB' + " " *
                (15-len(str(round(matriz[1][i]/1048576, 2)))) + f'{(matriz[1][i]/sum(matriz[1]))*100:.2f}%\n')
    f.write(f'''\nEspaço total ocupado: {sum(matriz[1])/1048576:.2f} MB
Espaço médio ocupado: {(sum(matriz[1])/len(matriz[0]))/1048576:.2f} MB''')
