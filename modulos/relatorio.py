import os

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

def pedidos_periodo(pedidos):
    os.system('clear')
    print("____________________________________________")
    print("|                                          |")
    print("|             Pedidos por Periodo          |")
    print("|__________________________________________|\n\n")

    relatorio_periodo = {}
    for i in pedidos:
        data = pedidos[i][4]
        print(data)

        dia, mes, ano = data.split('/')
        print(dia)
        print(mes)
        print(ano)

    relatorio_periodo[ano][mes].append(pedidos)

    input("\nTecle <ENTER> para continuar...")


def pedidos_cliente(pedidos):
    os.system('clear')
    print("____________________________________________")
    print("|                                          |")
    print("|             Pedidos por Cliente          |")
    print("|__________________________________________|\n")

    

    input("\nTecle <ENTER> para continuar...")

def pedidos_caneca(pedidos):
    os.system('clear')
    print("____________________________________________")
    print("|                                          |")
    print("|             Pedidos por Caneca           |")
    print("|__________________________________________|\n")

    input("\nTecle <ENTER> para continuar...")
