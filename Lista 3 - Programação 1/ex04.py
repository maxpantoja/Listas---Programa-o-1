gabarito = [input(f"Informe o Gabarito da {i+1}ª questão: ") for i in range(int(input("Nº de questões: ")))]
ct, notas = 1, []
while ct == 1:
    nota = 0
    print("\nInforme as respostas: ")
    for i in range(len(gabarito)):
        nota += 1 if gabarito[i].upper() == input(f"Resposta {i+1}ª questão: ").upper() else 0
    notas.append(nota)
    ct = int(input("Questões finalizadas. Outro aluno deseja usar o sistema? (1-Sim; 2-Não). R: "))
print(f"Alunos: {len(notas)}.\nMaior nº de acerto: {max(notas)}.\nMenor nº de acerto: {min(notas)}.\nMédia de "
      f"acertos da tuma: {sum(notas)/len(notas):.2f}")
