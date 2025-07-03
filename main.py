import os
import modulos.caneca
import modulos.cliente
import modulos.pedido
import modulos.relatorio
import modulos.informes
import modulos.menu
import modulos.valida

# CPFcliente -> nome, rua, telefone
clientes = {
    '000.000.000-00': ["Maggie Simpson", "Rua maria das dores", "55555-5555"],
    '111.111.111-11': ["Bart Simpson", "Rua do travesseiro", "55555-5556"],
    '222.222.222-22': ["Lisa Simpson", "Avenida das árvores", "55555-5557"],
    '333.333.333-33': ["Homer Simpson", "Rua da felicidade", "55555-5558"],
    '444.444.444-44': ["Marge Simpson", "Rua do amor", "55555-5559"],
    '555.555.555-55': ["Ned Flanders", "Rua da paz", "55555-5560"]
}

# IDcaneca -> modelo, cor, quantidadeEstoque, valor
canecas = {
    '0': ["Caneca do batman", "preta", 10, 50.00],
    '1': ["Caneca do superman", "azul", 20, 45.00],
    '2': ["Caneca do flash", "vermelha", 15, 40.00],
    '3': ["Caneca do lanterna verde", "verde", 25, 55.00],
    '4': ["Caneca do homem de ferro", "dourada", 30, 60.00],
    '5': ["Caneca da Mulher Maravilha", "roxa", 12, 48.00]
}

# IDpedido -> CPFcliente, IDcaneca, quantidade, valorTotal
pedidos = {
    '0': ["000.000.000-00", 0, 2, 100.00],
    '1': ["111.111.111-11", 1, 1, 45.00],
    '2': ["222.222.222-22", 2, 3, 120.00],
    '3': ["333.333.333-33", 3, 1, 55.00],
    '4': ["444.444.444-44", 4, 4, 240.00],
    '5': ["555.555.555-55", 5, 2, 96.00]
}

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
                        modulos.cliente.cadastro_cliente(clientes)
                    case '2':
                        modulos.cliente.listar_cliente(clientes)
                    case '3':
                        modulos.cliente.atualizar_cliente(clientes)
                    case '4':
                        modulos.cliente.excluir_cliente(clientes)
             
        case '2':

            opcao_caneca = ''
            while opcao_caneca != '0':
                opcao_caneca = modulos.caneca.menu_caneca()

                match opcao_caneca:

                    case '1':
                        modulos.caneca.cadastro_caneca(canecas)
                    case '2':
                        modulos.caneca.listar_caneca(canecas)
                    case '3':
                        modulos.caneca.atualizar_caneca(canecas)
                    case '4':
                        modulos.caneca.excluir_caneca(canecas)

        case '3':

            opcao_pedido = ''
            while opcao_pedido != '0':
                opcao_pedido = modulos.pedido.menu_pedido()

                match opcao_pedido:

                    case '1':
                        modulos.pedido.cadastro_pedido(pedidos)
                    case '2':
                        modulos.pedido.listar_pedido(pedidos)
                    case '3':
                        modulos.pedido.atualizar_pedido(pedidos)
                    case '4':
                        modulos.pedido.excluir_pedido(pedidos)

        case '4':

            modulos.informes.informes()

        case '5':

            opcao_relatorios = ''
            while opcao_relatorios != '0':
                opcao_relatorios = modulos.relatorio.menu_relatorio()

                match opcao_relatorios:

                    case '1':
                        modulos.relatorio.pedidos_periodo()
                    case '2':
                        modulos.relatorio.pedidos_cliente()
                    case '3':
                        modulos.relatorio.pedidos_caneca()

        case '0':
            print("Encerrando o programa")
            input("Tecle <ENTER> para continuar...")

        case _: #else
            print("Opção inválida!\n")
            input("Tecle <ENTER> para continuar...")    