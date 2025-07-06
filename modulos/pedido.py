import os
import datetime

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
    print("|__________________________________________|\n")
    opcao_pedido = str(input("Escolha sua opção: "))
    return opcao_pedido

def cadastro_pedido(pedidos,canecas,clientes):
    os.system('clear')
    print("____________________________________________")
    print("|                                          |")
    print("|             Cadastrar Pedido             |")
    print("|__________________________________________|\n")


    cliente_pedido = str(input("Informe o CPF do cliente: "))
    if cliente_pedido in clientes:

        #Pegando data dia/mes/ano
        data = datetime.datetime.now().strftime("%d/%m/%Y")

        # Gravando ID do pedido
        id_pedido = max(pedidos.keys()) + 1

        pedidos_condicao = ''
        while pedidos_condicao.lower() != 'n':
            
            #Mostrando as canecas para o cliente escolher
            print("\nCanecas disponiveis")
            for id, item in canecas.items():
                print("ID:",id, " Modelo:",item[0]," Cor:",item[1]," Quantidade:",item[2]," Valor: %.2f"%item[3])
            
            id_caneca = int(input("\nDigite o ID do modelo de caneca desejada: "))

            if id_caneca in canecas:

                while True:
                    quantidade = int(input("Digite a quantidade de canecas desejadas: "))
                    if quantidade > canecas[id_caneca][2]:
                        print("Não temos essa quantidade em estoque!")
                        print("\nO modelo escolhido", canecas[id_caneca][0], "só possui", canecas[id_caneca][2], "canecas\n")
                        resposta = input("Deseja outra quantidade para esse modelo? (s/n): ")
                        if resposta.lower() == 'n':
                            quantidade = 0
                            break
                    else:
                        break

                if quantidade > 0:
                    valor_caneca = canecas[id_caneca][3]
                    canecas[id_caneca][2] -= quantidade
                    valor_total = quantidade * valor_caneca
                    pedidos[id_pedido] = [cliente_pedido, id_caneca, quantidade, valor_total, data]

                    #Caso ele compre outro modelo, vai ser cadastrada uma nova compra com uma nova quantidade e modelo
                    id_pedido += 1 
                    print("\n\nPedido cadastrado com sucesso!")

                    print("\nValor da compra: %.2f"%valor_total)
                    pedidos_condicao = input("\nDeseja comprar outro modelo de caneca? (s/n): ")
                    os.system('clear')

            else:
                print("A caneca não existe no estoque!")
                print("\nEscolha novamente: ")

        input("Tecle <ENTER> para continuar...")

    else:
        print("Esse cliente não está cadastrado")
        input("Tecle <ENTER> para continuar...")

def listar_pedido(pedidos):
    os.system('clear')
    print("____________________________________________")
    print("|                                          |")
    print("|             Listar Pedido                |")
    print("|__________________________________________|\n")

    print("Lista de pedidos: ")
    for id, item in pedidos.items():
        print("ID:",id, "Cliente: ",item[0])

    id = int(input("\nDigite o ID do pedido: "))

    if id in pedidos:
        print("\nCPF Cliente: ", pedidos[id][0])
        print("ID caneca: ", pedidos[id][1])
        print("Quantidade de canecas: ", pedidos[id][2])
        print("Valor: R$ %.2f"%pedidos[id][3])
        print("Data: ", pedidos[id][4])
    else:
        print("\n\nPedido não existente!")
    input("\nTecle <ENTER> para continuar...")
        
def atualizar_pedido(pedidos):
    os.system('clear')
    print("____________________________________________")
    print("|                                          |")
    print("|             Atualizar Pedido             |")
    print("|__________________________________________|\n")

    print("Lista de pedidos: ")
    for id, item in pedidos.items():
        print("ID:",id, "Cliente: ",item[0])
    
    id = int(input("\nDigite o ID do pedido: "))

    if id in pedidos:
        print("\nInforme os novos dados do pedido: \n")

        cpf_cliente = input("\nCPF do cliente: ")
        id_caneca = input("ID caneca: ")
        quantidade = input("Quantidade: ")
        valor = float(input("Valor: "))
        data = datetime.datetime.now().strftime("%d/%m/%Y")
        pedidos[id] = [cpf_cliente, id_caneca, quantidade, valor, data]
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

    print("Lista de pedidos: ")
    for id, item in pedidos.items():
        print("ID:",id, "Cliente: ",item[0])

    id = int(input("\nDigite o ID do pedido: "))
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