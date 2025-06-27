import os

opcao = ''
while opcao != '0':
    os.system('clear')

    print("___________________________________________________")
    print("|                                                 |")
    print("|                Sistema SIG-Cup                  |")
    print("|_________________________________________________|")
    print("|                                                 |")
    print("|           1 Clientes                            |")
    print("|           2 Canecas                             |")
    print("|           3 Pedidos                             |")
    print("|           4 Informações                         |")
    print("|           0 Sair                                |")
    print("|_________________________________________________|")
    print("\n")
    opcao = str(input("Digite a opção desejada: "))

    match opcao:

        case '1':
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
                    
                    #cpf
                    nome = str(input("Nome: "))
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

                    print("Nome: ")
                    print("\nEndereço: ")
                    print("\nTelefone: \n")

                    input("Tecle <ENTER> para continuar...")

                case '3':
                    os.system('clear')
                    print("____________________________________________")
                    print("|                                          |")
                    print("|         Atualizar Dados dos Clientes     |")
                    print("|__________________________________________|\n")
                    
                    nome = str(input("Nome: "))
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

                    valor_id = input("Digite o id do cliente para excluir: \n")

                    print("Cliente excluido com sucesso!")
                    input("Tecle <ENTER> para continuar...")

                case '0':
                    print("Saindo do Módulo Cliente")
                    
        case '2':
            os.system('clear')
            print("____________________________________________")
            print("|                                          |")
            print("|                Canecas                   |")
            print("|__________________________________________|")
            print("|                                          |")
            print("|           1 Cadastrar                    |")
            print("|           2 Listar                       |")
            print("|           3 Atualizar                    |")
            print("|           4 Deletar                      |")
            print("|           0 Sair                         |")
            print("|__________________________________________|")
            op_canecas = str(input("Escolha sua opção: "))

            match op_canecas != '0':

                case '1':
                    os.system('clear')
                    print("____________________________________________")
                    print("|                                          |")
                    print("|           Cadastro de Canecas            |")
                    print("|__________________________________________|\n")

                    cor  = str(input("Cor: "))
                    valor = float(input("\nvalor: "))
                    id = id + 1 #Ideia de uma fila de IDs

                    print("\n\nCaneca cadastrada com sucesso!\n")
                    input("Tecle <ENTER> para continuar...")

                case '2':
                    print("Listar")
                
                case '3':
                    print("Atualizar")
                
                case '4':
                    print("Deletar")
                
                case '0':
                    print("Saindo do módulo canecas")

        case '3':
            os.system('clear')
            print("____________________________________________")
            print("|                                          |")
            print("|                Pedidos                   |")
            print("|__________________________________________|")
            print("|                                          |")
            print("|           1 Cadastrar                    |")
            print("|           2 Listar                       |")
            print("|           3 Atualizar                    |")
            print("|           4 Deletar                      |")
            print("|           0 Sair                         |")
            print("|__________________________________________|")
            op_pedidos = str(input("Escolha sua opção: "))

            match op_pedidos != 0:

                case '1':
                    print("Cadastrar")

                case '2':
                    print("Listar")
                
                case '3':
                    print("Atualizar")
                
                case '4':
                    print("Deletar")
                
                case '0':
                    print("Saindo do módulo pedidos")

        case '4':
            os.system('clear')
            print("____________________________________________")
            print("|                                          |")
            print("|                Informações               |")
            print("|__________________________________________|")
            print("|                                          |")
            print("|    Nome: Eduardo Nogueira                |")
            print("|    GitHub: @edunogueiraa                 |")
            print("|    Email: eduardonogueira105@gmail.com   |")
            print("|__________________________________________|")
            op_informacoes = str(input("Escolha sua opção: "))


            match op_informacoes != 0:

                case '1':
                    print("Cadastrar")
                    
                case '2':
                    print("Listar")
                
                case '3':
                    print("Atualizar")
                
                case '4':
                    print("Deletar")
                
                case '0':
                    print("Saindo do módulo informações")

        case '0':
            print("Encerrando o programa")
            input("Tecle <ENTER> para continuar...")

        case _: #else
            print("Opção inválida!\n")
            input("Tecle <ENTER> para continuar...")    