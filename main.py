import os

opcao = ''
while opcao != '0':
    
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
    opcao = int(input("Digite a opção desejada: "))

    match opcao:

        case 1:
         op_clientes = ''
         while op_clientes != '0':

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
            op_clientes = input("Escolha sua opção: ")

            match op_clientes != 0:

                case 1:

                    print("____________________________________________")
                    print("|                                          |")
                    print("|           Cadastro de Clientes           |")
                    print("|__________________________________________|\n")

                    nome = str(input("Nome: "))
                    endereco = str(input("\nEndereço: "))
                    telefone = str(input("\nTelefone: "))

                    print("\n\nCliente cadastrado com sucesso!\n")
                    input("Tecle <ENTER> para continuar...")


                case 2:

                    print("____________________________________________")
                    print("|                                          |")
                    print("|           Exibir Dados de Clientes       |")
                    print("|__________________________________________|\n")

                    print("Nome: ")
                    print("\nEndereço: ")
                    print("\nTelefone: \n")

                    input("Tecle <ENTER> para continuar...")

                case 3:
                 print()
                case 4:
                 print()
                case 0:
                 print()

        case 2:
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
            Resposta = input("Escolha sua opção: ")

        case 3:
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
            Resposta = input("Escolha sua opção: ")

        case 4:

            print("____________________________________________")
            print("|                                          |")
            print("|                Informações               |")
            print("|__________________________________________|")
            print("|                                          |")
            print("|    Nome: Eduardo Nogueira                |")
            print("|    GitHub: @edunogueiraa                 |")
            print("|    Email: eduardonogueira105@gmail.com   |")
            print("|__________________________________________|")
            Resposta = input("Escolha sua opção: ")

        case 0:
            print("Encerrando o programa")
            input("Tecle <ENTER> para continuar...")

        case _: #else
            print("Opção inválida!\n")
            input("Tecle <ENTER> para continuar...")    