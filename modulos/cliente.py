import os

def cliente():
    os.system('clear')
    print("____________________________________________")
    print("|                                          |")
    print("|                Clientes                  |")
    print("|__________________________________________|")
    print("|                                          |")
    print("|           1 Cadastrar                    |")
    print("|           2 Exibir Dados                 |")
    print("|           3 Atualizar                    |")
    print("|           4 Deletar                      |")
    print("|           5 Listar                       |")
    print("|           0 Sair                         |")
    print("|__________________________________________|")
    op_clientes = str(input("Escolha sua opção: "))

    match op_clientes != '0':

        case '1':
            os.system('clear')
            print("____________________________________________")
            print("|                                          |")
            print("|           Cadastro de Clientes           |")
            print("|__________________________________________|\n")
            
            cpf = str(input("CPF:"))
            nome = str(input("\nNome: "))
            endereco = str(input("\nEndereço: "))
            telefone = str(input("\nTelefone: "))

            print("\n\nCliente cadastrado com sucesso!\n")
            input("Tecle <ENTER> para continuar...")


        case '2':
            os.system('clear')
            print("____________________________________________")
            print("|                                          |")
            print("|          Exibir Dados dos Clientes       |")
            print("|__________________________________________|\n")

            print("CPF: ")
            print("\nNome: ")
            print("\nEndereço: ")
            print("\nTelefone: \n")

            input("Tecle <ENTER> para continuar...")

        case '3':
            os.system('clear')
            print("____________________________________________")
            print("|                                          |")
            print("|         Atualizar Dados dos Clientes     |")
            print("|__________________________________________|\n")
            
            cpf = str(input("CPF: "))
            nome = str(input("\nNome: "))
            endereco = str(input("\nEndereço: "))
            telefone = str(input("\nTelefone: "))

            print("\n\nDados alterados com sucesso!\n")
            input("Tecle <ENTER> para continuar...")

        case '4':
            os.system('clear')
            print("____________________________________________")
            print("|                                          |")
            print("|           Excluir Dados dos Clientes     |")
            print("|__________________________________________|\n")

            valor_cpf = input("Digite o cpf do cliente para excluir: ")

            print("Cliente excluido com sucesso!")
            input("Tecle <ENTER> para continuar...")

        case '0':
            print("Saindo do Módulo Cliente")