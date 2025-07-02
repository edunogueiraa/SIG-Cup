import os
import modulos.caneca
import modulos.cliente
import modulos.pedido
import modulos.relatorio
import modulos.informes
import modulos.menu
import modulos.valida

opcao_principal = ''
while opcao_principal != '0':

    opcao_principal = modulos.menu.menu_principal()

    match opcao_principal:

        case '1':
            opcao_cliente = ''
            while opcao_cliente != '0':
                opcao_cliente = modulos.cliente.menu_cliente()

                match opcao_cliente:

                    case '1':
                        modulos.cliente.cadastro_cliente()
                    case '2':
                        modulos.cliente.listar_cliente()
                    case '3':
                        modulos.cliente.atualizar_cliente()
                    case '4':
                        modulos.cliente.excluir_cliente()
             
        case '2':

            modulos.caneca.menu_caneca()

            opcao_caneca = ''
            while opcao_caneca != '0':
                opcao_caneca = modulos.caneca.menu_caneca()

                match opcao_caneca:

                    case '1':
                        modulos.caneca.cadastro_caneca()
                    case '2':
                        modulos.caneca.listar_caneca()
                    case '3':
                        modulos.caneca.atualizar_caneca()
                    case '4':
                        modulos.caneca.excluir_caneca()

        case '3':
            
            modulos.pedido.pedido()

        case '4':

            modulos.informes.informes()

        case '5':

            modulos.relatorio.relatorio()

        case '0':
            print("Encerrando o programa")
            input("Tecle <ENTER> para continuar...")

        case _: #else
            print("Opção inválida!\n")
            input("Tecle <ENTER> para continuar...")    