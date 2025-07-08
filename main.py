import pickle
import modulos.caneca
import modulos.cliente
import modulos.pedido
import modulos.relatorio
import modulos.informes
import modulos.menu

# CPFcliente -> nome, rua, telefone
clientes = {}

try:#Abre o arquivo e ler
  arq_clientes = open("clientes.dat", "rb")
  clientes = pickle.load(arq_clientes)

except: #cria um novo aquivo, caso não tenha e fecha
  arq_clientes = open("clientes.dat", "wb")
arq_clientes.close()


# IDcaneca -> modelo, cor, quantidadeEstoque, valor
canecas = {}

try:
  arq_canecas = open("canecas.dat", "rb")
  canecas = pickle.load(arq_canecas)

except:
  arq_canecas = open("canecas.dat", "wb")
arq_canecas.close()


# IDpedido -> CPFcliente, IDcaneca, quantidade, valorTotal,data
pedidos = {}

try:
  arq_pedidos = open("pedidos.dat", "rb")
  pedidos = pickle.load(arq_pedidos)

except:
  arq_pedidos = open("pedidos.dat", "wb")
arq_pedidos.close()


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
                        modulos.pedido.cadastro_pedido(pedidos, canecas, clientes)
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
                        modulos.relatorio.pedidos_periodo(pedidos)
                    case '2':
                        modulos.relatorio.pedidos_cliente(pedidos)
                    case '3':   
                        modulos.relatorio.pedidos_caneca(pedidos)

        case '0':
            print("Encerrando o programa e gravando dados...")
            input("Tecle <ENTER> para continuar...")

        case _: #else
            print("Opção inválida!\n")
            input("Tecle <ENTER> para continuar...")


# Abre, grava e fecha

arq_clientes = open("clientes.dat", "wb")
pickle.dump(clientes, arq_clientes)
arq_clientes.close()

arq_canecas = open("canecas.dat", "wb")
pickle.dump(canecas, arq_canecas)
arq_canecas.close()

arq_pedidos = open("pedidos.dat", "wb")
pickle.dump(pedidos, arq_pedidos)
arq_pedidos.close()