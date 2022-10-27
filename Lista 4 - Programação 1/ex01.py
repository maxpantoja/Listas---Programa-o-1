agenda = {}
def incluirNovoNome(nome, telefones):
    agenda[nome] = telefones
def incluirTelefone(nome, telefone):
    if nome not in agenda:
        x = int(input('Este nome não existe em sua agenda. Desejas acrescentar?\n (1)-Sim (2)-Não. R: '))
        if x == 1:
            incluirNovoNome(nome, telefone)
    else:
        agenda[nome].append(telefone[0])
def excluirTelefone(nome, telefone):
    if len(agenda[nome]) == 1:
        del agenda[nome]
    else:
        del agenda[nome][agenda[nome].index(telefone)]
def excluirNome(nome):
    del agenda[nome]
def consultarTelefone(nome):
    for i in range(len(agenda[nome])):
        print(f"Contato {i+1}: {agenda[nome][i]}")
x = '1'
while x != '0':
    x = input('''O que desejas fazer com sua agenda neste momento?
        (1) - Salvar novo contato.
        (2) - Adicionar número a um contato existente.
        (3) - Excluir telefone de uma pessoa.
        (4) - Excluir uma pessoa da agenda.
        (5) - Consultar números de uma pessoa.
        (0) - Sair da agenda.
        Escolha: ''')
    if x == '1':
        incluirNovoNome(input('Insira o Nome do novo contato: '), (input('Insira os números deste separados por espaço: ')).split())
    elif x == '2':
        incluirTelefone(input('Insira o Nome da pessoa que desejas inserir o número: '), [input('Insira o número: ')])
    elif x == '3':
        excluirTelefone(input('Insira o nome da pessoa: '), input('Insira o número que desejas excluir desta: '))
    elif x == '4':
        excluirNome(input('Insira o nome da pessoa que desejas excluir: '))
    elif x == '5':
        consultarTelefone(input('Insira o nome da pessoa que desejas consultar os contatos: '))
    elif x == '0':
        print('Operações finalizadas.')
    else:
        print('Escolha uma opção válida.')