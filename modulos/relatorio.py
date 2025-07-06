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

# Formato do dicionário:  IDpedido -> CPFcliente, IDcaneca, quantidade, valorTotal,data

def pedidos_periodo(pedidos):
    os.system('clear')
    print("________________________________________________________________________________________________________")
    print("|                                                                                                      |")                                           
    print("|                                    Relatório Geral Pedidos Por Periodo                               |")
    print("|______________________________________________________________________________________________________|")
    print("|             |                                                                                        |")
    print("|    Datas    |                                      Pedidos                                           |")
    print("|_____________|________________________________________________________________________________________|")
    print("                                                                                                        ")

    for id, item in pedidos.items():
        print(f"|  {item[4]:<10} |        ID: {id}   CPF: {item[0]}   Caneca: {item[1]}   Qtd: {item[2]}   Valor: R$ {item[3]:.2f}  ")

    print(" _______________________________________________________________________________________________________")
    print()

    input("\nTecle <ENTER> para continuar...")


def pedidos_cliente(pedidos):
    os.system('clear')
    print("__________________________________________________________________________________________________")
    print("|                                                                                                 |")                                           
    print("|                               Relatório Geral Pedidos Por Cliente                               |")
    print("|_________________________________________________________________________________________________|")
    print("|                |                                                                                |")
    print("|     Clientes   |                                   Pedidos                                      |")
    print("|________________|________________________________________________________________________________|")
    print("|                |                                                                                 ")

    print("|________________|_________________________________________________________________________________|")
    print()

    input("\nTecle <ENTER> para continuar...")

def pedidos_caneca(pedidos):
    os.system('clear')
    print("__________________________________________________________________________________________________")
    print("|                                                                                                 |")                                           
    print("|                               Relatório Geral Pedidos Por Canecas                               |")
    print("|_________________________________________________________________________________________________|")
    print("|             |                                                                                   |")
    print("|  IDs Caneca |                                    Pedidos                                        |")
    print("|_____________|___________________________________________________________________________________|")
    print("|             |                                                                                    ")

    print("|_____________|___________________________________________________________________________________|")
    print()

    input("\nTecle <ENTER> para continuar...")
