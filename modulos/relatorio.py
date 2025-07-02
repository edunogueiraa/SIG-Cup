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

def pedidos_periodo():
    os.system('clear')
    print("____________________________________________")
    print("|                                          |")
    print("|             Pedidos por Periodo          |")
    print("|__________________________________________|\n")

def pedidos_cliente():
    os.system('clear')
    print("____________________________________________")
    print("|                                          |")
    print("|             Pedidos por Cliente          |")
    print("|__________________________________________|\n")

def pedidos_produto():
    os.system('clear')
    print("____________________________________________")
    print("|                                          |")
    print("|             Pedidos por Produto          |")
    print("|__________________________________________|\n")
