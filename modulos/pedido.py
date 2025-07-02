import os

# IDpedido -> CPFcliente, IDcaneca, quantidade, valorTotal
pedidos = {
    '0': ["000.000.000-00", 0, 2, 100.00],
    '1': ["111.111.111-11", 1, 1, 45.00],
    '2': ["222.222.222-22", 2, 3, 120.00],
    '3': ["333.333.333-33", 3, 1, 55.00],
    '4': ["444.444.444-44", 4, 4, 240.00],
    '5': ["555.555.555-55", 5, 2, 96.00]
}

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

def cadastro_pedido():
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

def listar_pedido():
    os.system('clear')
    print("____________________________________________")
    print("|                                          |")
    print("|             Listar Pedidos               |")
    print("|__________________________________________|\n")
        
def atualizar_pedido():
    os.system('clear')
    print("____________________________________________")
    print("|                                          |")
    print("|             Atualizar Pedido             |")
    print("|__________________________________________|\n")

    id_pedido = int(input("Digite o ID do pedido: "))
        
def atualizar_pedido():
    os.system('clear')
    print("____________________________________________")
    print("|                                          |")
    print("|             Deletar Pedido               |")
    print("|__________________________________________|\n")

    id_pedido = int(input("Digite o ID do pedido: "))
        