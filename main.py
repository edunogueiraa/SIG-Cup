import os
import modulos.caneca
import modulos.cliente
import modulos.pedido


opcao = ''
while opcao != '0':
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
    opcao = str(input("Digite a opção desejada: "))

    match opcao:

        case '1':

            modulos.cliente.cliente()
             
        case '2':

            modulos.caneca.caneca()
 
        case '3':
            
            modulos.pedido.pedido()

        case '4':
            os.system('clear')
            print("____________________________________________")
            print("|                                          |")
            print("|                Informações               |")
            print("|__________________________________________|")
            print("|                                          |")
            print("|    Nome: Eduardo Nogueira                |")
            print("|    GitHub: @edunogueiraa                 |")
            print("|    Email: eduardonogueira105@gmail.com   |")
            print("|__________________________________________|\n")

            input("Tecle <ENTER> para continuar...") 

        case '5':
            os.system('clear')
            print("____________________________________________")
            print("|                                          |")
            print("|                Relatórios                |")
            print("|__________________________________________|")
            print("|                                          |")
            print("|           1 Pedidos por Periodo          |")
            print("|           2 Pedidos por Cliente          |")
            print("|           3 Pedidos por Produto          |")
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

        case '0':
            print("Encerrando o programa")
            input("Tecle <ENTER> para continuar...")

        case _: #else
            print("Opção inválida!\n")
            input("Tecle <ENTER> para continuar...")    