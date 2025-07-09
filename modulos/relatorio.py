import os
import datetime

def menu_relatorio():
    os.system('clear')
    print("____________________________________________")
    print("|                                          |")
    print("|                Relatórios                |")
    print("|__________________________________________|")
    print("|                                          |")
    print("|           1 Pedidos por Periodo          |")
    print("|           2 Pedidos por Cliente          |")
    print("|           3 Pedidos por Caneca           |")
    print("|           0 Sair                         |")
    print("|__________________________________________|\n")
    opcao_relatorios = str(input("Escolha sua opção: "))
    return opcao_relatorios


def pedidos_periodo(pedidos,clientes):
    os.system('clear')
    print("________________________________________________________________________________________________________")
    print("|                                                                                                      |")                                           
    print("|                                    Relatório Geral Pedidos Por Periodo                               |")
    print("|______________________________________________________________________________________________________|")
    print("|                |                           |                       |                                 |")
    print("|      Data      |    Quantidade Clientes    | Quantidade de Pedidos |      Valor Recebido na Data     |")
    print("|________________|___________________________|_______________________|_________________________________|")
    print("|                |                           |                       |                                 |")

    #Pegando uma data de cada
    datas = []
    for i in pedidos:
        if pedidos[i][4] not in datas:
            datas.append(pedidos[i][4])

    #Pecorrendo cada data
    for data in datas:

        quantidade_pedidos = 0
        clientes = []
        valor = 0

        #Pecorendo os pedidos e analizando
        for i in pedidos:
            if pedidos[i][4] == data:
                cpf = pedidos[i][0]
                if cpf not in clientes:
                    clientes.append(cpf)

                quantidade_pedidos += 1 #Contando pedidos da data
                valor += pedidos[i][3] #Somando valores dos pedidos da data

                quantidade_clientes = len(clientes)

        valor_formatado = f"{valor:.2f}"

        print(f"|   {data:12s} | {quantidade_clientes:25d} | {quantidade_pedidos:21d} | R$ {valor_formatado:>28s} |")

    print("|______________________________________________________________________________________________________|")
    

    input("\nTecle <ENTER> para continuar...")



def pedidos_cliente(pedidos,clientes):
    os.system('clear')
    print("___________________________________________________________________________________________________")
    print("|                                                                                                 |")                                           
    print("|                               Relatório Geral Pedidos Por Cliente                               |")
    print("|_________________________________________________________________________________________________|")
    print("|                |                           |                       |                            |")
    print("|       CPF      |       Nome Completo       |  Quantidade Comprada  |    Valor Gasto na Loja     |")
    print("|________________|___________________________|_______________________|____________________________|")
    print("|                |                           |                       |                            |")

    cpfs = list(clientes.keys())
    for i in range(len(cpfs)):
        cpf = cpfs[i]

        quantidade = 0
        valor = 0
        for x in pedidos:
            if pedidos[x][0] == cpf: 
                quantidade += pedidos[x][2]
                valor += pedidos[x][3]  

        nome = clientes[cpf][0][0:22]
        valor_formatado = f"{valor:.2f}"

        print(f"| {cpf:14s} | {nome:25s} | {quantidade:21d} | R$ {valor_formatado:>23s} |")

    print("|_________________________________________________________________________________________________|")
    

    input("\nTecle <ENTER> para continuar...")

def pedidos_caneca(pedidos,canecas):
    os.system('clear')
    print("___________________________________________________________________________________________________")
    print("|                                                                                                 |")                                           
    print("|                               Relatório Geral Pedidos Por Canecas                               |")
    print("|_________________________________________________________________________________________________|")
    print("|                |                           |                       |                            |")
    print("|   IDs Caneca   |          Modelo           |   Quantidade Vendas   |      Valor das Vendas      |")
    print("|________________|___________________________|_______________________|____________________________|")
    print("|                |                           |                       |                            |")

    ids_canecas = list(canecas.keys())
    for i in range(len(ids_canecas)):
        id = ids_canecas[i]

        quantidade = 0
        valor_caneca = 0

        valor_caneca = canecas[id][3]  

        #Juntei a quantidade de canecas do pedido
        for j in pedidos:
            if pedidos[j][1] == id: 
                quantidade += pedidos[j][2] #Quantidade de vendas de cada caneca

        valor_vendas = quantidade * valor_caneca

        modelo = canecas[id][0][0:22]
        valor_formatado = f"{valor_vendas:.2f}"

        print(f"| {id:<14d} | {modelo:25s} | {quantidade:21d} | R$ {valor_formatado:>23s} |")

    print("|_________________________________________________________________________________________________|")

    input("\nTecle <ENTER> para continuar...")
