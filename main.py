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
    print("|           5 Relatórios                          |")
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
                    print("|           Cadastro de Caneca             |")
                    print("|__________________________________________|\n")
                    
                    cor  = str(input("Cor: "))
                    valor = float(input("\nvalor: "))
                    modelo = str(input("\nModelo:"))
                    quantidade = int(input("\nQuantidade: "))
                    #id = len(dicionário) + 1

                    print("\n\nCaneca cadastrada com sucesso!\n")
                    input("Tecle <ENTER> para continuar...")

                case '2':
                    os.system('clear')
                    print("____________________________________________")
                    print("|                                          |")
                    print("|             Listar Canecas               |")
                    print("|__________________________________________|\n")

                    print("Modelos: ", modelos)
                    print("Cores: ", cores)
                    print("Valores: ",valores)
                    print("Quantidade em Estoque: ", quantidade_estoque)

                    input("Tecle <ENTER> para continuar...")

                case '3':
                    os.system('clear')
                    print("____________________________________________")
                    print("|                                          |")
                    print("|             Atualizar Caneca             |")
                    print("|__________________________________________|\n")

                    id_atualizar_caneca = int(input("Digite o ID da caneca: "))
                    cor  = str(input("\n\nCor: "))
                    valor = float(input("\nvalor: "))
                    modelo = str(input("\nModelo:"))
                    quantidade = int(input("\nQuantidade: "))
                    id = id_atualizar_caneca

                    print("\n\nCaneca atualizada com sucesso!\n")
                    input("Tecle <ENTER> para continuar...")

                case '4':
                    os.system('clear')
                    print("____________________________________________")
                    print("|                                          |")
                    print("|             Deletar Caneca               |")
                    print("|__________________________________________|\n")

                    id_deletar_caneca = int(input("Digite o ID da caneca: "))

                    print("\n\nCaneca atualizada com sucesso!\n")
                    input("Tecle <ENTER> para continuar...")

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
                    os.system('clear')
                    print("____________________________________________")
                    print("|                                          |")
                    print("|             Cadastrar Pedido             |")
                    print("|__________________________________________|\n")

                    cliente_pedido = str(input("Informe o CPF do cliente: "))
                    while pedidos != 'n':
                        caneca_pedido = int(input("\nDigite o ID do modelo de caneca desejada: "))
                        quantidade_pedido = int(input("\nDigite a quantidade de canecas desse modelo: \n"))
                        
                        valor_total = quantidade_pedido * valor_caneca

                        pedidos = str(input("Deseja comprar outro modelo de caneca? (s/n)"))

                case '2':
                    os.system('clear')
                    print("____________________________________________")
                    print("|                                          |")
                    print("|             Listar Pedidos               |")
                    print("|__________________________________________|\n")
                
                case '3':
                    os.system('clear')
                    print("____________________________________________")
                    print("|                                          |")
                    print("|             Atualizar Pedido             |")
                    print("|__________________________________________|\n")

                    id_pedido = int(input("Digite o ID do pedido: "))
                
                case '4':
                    os.system('clear')
                    print("____________________________________________")
                    print("|                                          |")
                    print("|             Deletar Pedido               |")
                    print("|__________________________________________|\n")

                    id_pedido = int(input("Digite o ID do pedido: "))
                
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
            print("|__________________________________________|\n")

            input("Tecle <ENTER> para continuar...") 

        case '5':
            os.system('clear')
            print("____________________________________________")
            print("|                                          |")
            print("|                Relatórios                |")
            print("|__________________________________________|")
            print("|                                          |")
            print("|           1 Pedidos por Periodo          |")
            print("|           2 Pedidos por Cliente          |")
            print("|           3 Pedidos por Produto          |")
            print("|           0 Sair                         |")
            print("|__________________________________________|")
            op_relatorios = str(input("Escolha sua opção: "))

            match op_relatorios != '0':

                case '1':
                    os.system('clear')
                    print("____________________________________________")
                    print("|                                          |")
                    print("|             Pedidos por Periodo          |")
                    print("|__________________________________________|\n")

                case '2':
                    os.system('clear')
                    print("____________________________________________")
                    print("|                                          |")
                    print("|             Pedidos por Cliente          |")
                    print("|__________________________________________|\n")

                case '3':
                    os.system('clear')
                    print("____________________________________________")
                    print("|                                          |")
                    print("|             Pedidos por Produto          |")
                    print("|__________________________________________|\n")

                case '0':
                    print("Saindo do Módulo Relatórios")

        case '0':
            print("Encerrando o programa")
            input("Tecle <ENTER> para continuar...")

        case _: #else
            print("Opção inválida!\n")
            input("Tecle <ENTER> para continuar...")    