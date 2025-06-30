import os

def pedido():
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