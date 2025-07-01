import os
import modulos.caneca
import modulos.cliente
import modulos.pedido
import modulos.relatorio
import modulos.informes
import modulos.painel
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

opcao = ''
while opcao != '0':
    os.system('clear')

    modulos.painel.painel()

    opcao = str(input("Digite a opção desejada: "))

    match opcao:

        case '1':

            modulos.cliente.cliente()
             
        case '2':

            modulos.caneca.caneca()
 
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