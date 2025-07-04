import os

def menu_pedido():
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
    opcao_pedido = str(input("Escolha sua opção: "))
    return opcao_pedido

def cadastro_pedido(pedidos,canecas):
    os.system('clear')
    print("____________________________________________")
    print("|                                          |")
    print("|             Cadastrar Pedido             |")
    print("|__________________________________________|\n")


    cliente_pedido = str(input("Informe o CPF do cliente: "))
    pedidos_condicao = ''
    while pedidos_condicao != 'n':
        id_caneca = int(input("\nDigite o ID do modelo de caneca desejada: "))

        #Não deixar ele comprar uma quantidade maior que a existente em estoque

        quantidade = int(input("Digite a quantidade de canecas desse modelo: "))

        valor_caneca = canecas[id_caneca][3]
        
        valor_total = quantidade * valor_caneca

        pedidos_condicao = str(input("\nDeseja comprar outro modelo de caneca? (s/n)"))
        id_pedido = max(pedidos.keys()) + 1

        #Eliminando canecas que foram compradas
        canecas[id_caneca][2] -= quantidade

        pedidos[id_pedido] = [cliente_pedido, id_caneca, quantidade, valor_total]


def listar_pedido(pedidos):
    os.system('clear')
    print("____________________________________________")
    print("|                                          |")
    print("|             Listar Pedido                |")
    print("|__________________________________________|\n")

    id = int(input("Digite o ID do pedido: "))

    if id in pedidos:
        print("\nCPF Cliente: ", pedidos[id][0])
        print("ID caneca: ", pedidos[id][1])
        print("Quantidade de canecas: ", pedidos[id][2])
        print("Valor total: ", pedidos[id][3])
    else:
        print("\n\nPedido não existente!")
    input("Tecle <ENTER> para continuar...")
        
def atualizar_pedido(pedidos):
    os.system('clear')
    print("____________________________________________")
    print("|                                          |")
    print("|             Atualizar Pedido             |")
    print("|__________________________________________|\n")

    id = int(input("Digite o ID do pedido: "))

    if id in pedidos:
        print("\nInforme os novos dados do pedido: \n")

        cpf_cliente = input("\nCPF do cliente: ")
        id_caneca = input("ID caneca: ")
        quantidade = input("Quantidade: ")
        valor = input("Valor: ")
        pedidos[id] = [cpf_cliente, id_caneca, quantidade, valor]
        print("\n\nDados alterados com sucesso!")
    else:
        print("\n\nPedido inexistente!")
    input("Tecle <ENTER> para continuar...")
        
def excluir_pedido(pedidos):
    os.system('clear')
    print("____________________________________________")
    print("|                                          |")
    print("|             Deletar Pedido               |")
    print("|__________________________________________|\n")

    id = int(input("Digite o ID do pedido: "))
    if id in pedidos:
        print("\nCPF Cliente: ", pedidos[id][0])
        print("ID caneca: ", pedidos[id][1])
        print("Quantidade de canecas: ", pedidos[id][2])
        print("Valor total: ", pedidos[id][3])
        print()
        resposta = input("Deseja exluir o pedido? (S/N)")
        if resposta == 'S' or resposta == 's':
            del pedidos[id]
            print("\n\nPedido excluido com sucesso!")
        else:
            print("\n\nExclusão não realizada!")
    else:
        print("\n\nPedido inexistente!")
    input("Tecle <ENTER> para continuar...")        