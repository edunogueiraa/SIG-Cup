import os

def relatorio():
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