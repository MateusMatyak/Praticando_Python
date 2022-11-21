print('Controle de cadastro de Funcionários')

menu_funcionário = {
    1: 'Cadastrar Funcionário',
    2: ['Consultar Funcionário', {
        1: 'Consultar Todos os Funcionários',
        2: 'Consultar Funcionário por id',
        3: 'Consultar Funcionário(s) por Setor',
        4: 'Retornar',
    }],
    3: 'Remover Funcionário',
    4: 'Sair'
}
# Função que imprime as opções dos menus
def FUN_menu(menu: dict) -> None:  
    for key, val in menu.items():
        print(f"{key} - {val if type(val) == str else val[0]}")
    print('-' * 30)
    
# Função que imprime e valida a opção do menu
def mostrar_menu(menu: dict) -> int:  
    print(f"\n{'Menu Principal':-^30s}")
    FUN_menu(menu)
    while True:
        try:
            opcao = int(input("Escolha a opção desejada: "))
            # Verifica se a opção está presente no dicionário do menu
            # Se sim, limpa a tela e retorna a opção selecionada
            if opcao in menu.keys():
                break
            else:
                print("\nOpção inválida!\n")
        except ValueError:
            print("\nOpção inválida.\n")
    return opcao

#Função que cadastra Funcionários
def cadastrarfuncionário(id: int) -> None:  
    print("\nOpção Cadastrar funcionário\n")
    print("id da funcionário {:>03}".format(id))
    nome = input("Digite o nome do funcionário: ").strip()
    setor = input("Digite o setor do funcionário: ").strip()
    while True:
        try:
            salário = float(input("Digite o salário (R$) do funcionário: "))
            # Verifica se o salário é maior que zero
            if salário <= 0:
                print("\nALERTA!!!! Digite um salário maior que zero.\n")
            else:
                break
        except ValueError:
            print("\nALERTA!!! Digite um número válido.\n")
    Funcionários[id] = []
    Funcionários[id].append(nome)
    Funcionários[id].append(setor)
    Funcionários[id].append(salário)
    
# Função que remove Funcionários
def remover_funcionário() -> None:  
    while True:
        try:
            id = int(input("\nEscreva o id do funcionário a ser removido: "))
            # Verifica se existe o funcionário com o id informado
            # Se sim, remove o funcionário do dicionário
            if id not in Funcionários.keys():
                print("\nNenhum funcionário possui esse id.\n")
            else:
                Funcionários.pop(id)
            break
        except ValueError:
            print("\nALERTA!!!! Digite um id válido.\n")
    print("")
    
# Função para consulta de Funcionários
def consultarfuncionário() -> None:  
    # Variável usada para controlar a exibição do menu de consulta
    exibir_menu = True
    cabecalho = f"| {'id':<10} | {'Nome':<25} | {'setor':<20} | {'salário (R$)':>10} |"
    len_cabecalho = len(cabecalho)
    while True:
        try:
            # Exibe o menu de consulta
            if exibir_menu:
                print("\nVocê selecionou a opção Consultar Funcionários\n")
                print(f"{'Consultar Funcionários':-^30s}")
                FUN_menu(menu_funcionário[2][1])
            opcao = int(input("Escolha a opção desejada: "))
            # Opção 1 - Consultar Todas os Funcionários
            if opcao == 1:
                # Lista todas os Funcionários cadastrados, se houver
                if len(Funcionários) > 0:
                    print("\nTodos os Funcionários cadastrados:\n")
                    print("-" * len_cabecalho)
                    print(cabecalho)
                    print("-" * len_cabecalho)
                    for key, val in Funcionários.items():
                        print(f"| {key:<10} | {val[0]:<25} | {val[1]:<20} | {val[2]:>10.2f} |")
                    print("-" * len_cabecalho)
                else:
                    print("\nNão existem Funcionários cadastradas.")
                print("")
            # Opção 2 - Consultar funcionário por id
            elif opcao == 2:
                while True:
                    try:
                        id = int(input("\nDigite o id do funcionário a ser consultado: "))
                        # Exibe o funcionário com o respectivo id, se houver
                        if id in Funcionários.keys():
                            print("-" * len_cabecalho)
                            print(cabecalho)
                            print("-" * len_cabecalho)
                            print(
                                f"| {id:<10} | {Funcionários[id][0]:<25} | {Funcionários[id][1]:<20} | {Funcionários[id][2]:>10.2f} |")
                            print("-" * len_cabecalho)
                        else:
                            print("\nNão existe funcionário com esse id.\n")
                        print("")
                        break
                    except ValueError:
                        print("\nDigite um id válido.\n")
            # Opção 3 - Consultar funcionário por setor
            elif opcao == 3:
                while True:
                    try:
                        setor = input("\nDigite o setor da funcionário a ser consultada: ")
                        # Variável usada para controlar a exibição do cabeçalho da lista
                        existe_funcionário = False
                        for key, val in Funcionários.items():
                            # Imprime os dados do funcionário do setor informado
                            if val[1].upper() == setor.upper():
                                if not existe_funcionário:
                                    print("-" * len_cabecalho)
                                    print(cabecalho)
                                    print("-" * len_cabecalho)
                                print(f"| {key:<10} | {val[0]:<25} | {val[1]:<20} | {val[2]:>10.2f} |")
                                existe_funcionário = True
                        if not existe_funcionário:
                            print("\nNão existe funcionário com esse setor.\n")
                        else:
                            print("-" * len_cabecalho)
                        break
                    except ValueError:
                        print("Digite um setor válido.")
            elif opcao == 4:
                break
            else:
                print("\nAtenção! Você digitou uma opção inválida.\n")
            exibir_menu = True
        except ValueError:
            print("\nAtenção! Você digitou uma opção inválida.\n")
            exibir_menu = False
Funcionários = {}
while True:
    opcao_selecionada = mostrar_menu(menu_funcionário)
    if opcao_selecionada == 1:
        id_Funcionários = len(Funcionários) + 1
        cadastrarfuncionário(id_Funcionários)
    elif opcao_selecionada == 2:
        consultarfuncionário()
    elif opcao_selecionada == 3:
        remover_funcionário()
    else:
        break