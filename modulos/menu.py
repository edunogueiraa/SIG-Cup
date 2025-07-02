import os

def menu_principal():
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
        
    opcao_principal = str(input("Digite a opção desejada: "))
    return opcao_principal