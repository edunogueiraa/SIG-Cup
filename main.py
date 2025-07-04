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
    '111.111.111-11': ["Manoel Gomes", "Rua azul", "55555-5556"]
}

# IDcaneca -> modelo, cor, quantidadeEstoque, valor
canecas = {
    0: ["Caneca do batman", "preta", 10, 50.00],
    1: ["Caneca do caneta azul", "azul", 20, 45.00]
}

# IDpedido -> CPFcliente, IDcaneca, quantidade, valorTotal
pedidos = {
    0: ["000.000.000-00", 0, 2, 100.00],
    1: ["111.111.111-11", 1, 1, 45.00]
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
                        modulos.pedido.cadastro_pedido(pedidos,canecas)
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