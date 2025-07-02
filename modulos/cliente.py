import os

# CPFcliente -> nome, rua, telefone
clientes = {
    '000.000.000-00': ["Maggie Simpson", "Rua maria das dores", "55555-5555"],
    '111.111.111-11': ["Bart Simpson", "Rua do travesseiro", "55555-5556"],
    '222.222.222-22': ["Lisa Simpson", "Avenida das árvores", "55555-5557"],
    '333.333.333-33': ["Homer Simpson", "Rua da felicidade", "55555-5558"],
    '444.444.444-44': ["Marge Simpson", "Rua do amor", "55555-5559"],
    '555.555.555-55': ["Ned Flanders", "Rua da paz", "55555-5560"]
}

def menu_cliente ():
    os.system('clear')
    print("____________________________________________")
    print("|                                          |")
    print("|                Clientes                  |")
    print("|__________________________________________|")
    print("|                                          |")
    print("|           1 Cadastrar                    |")
    print("|           2 Exibir Dados                 |")
    print("|           3 Atualizar                    |")
    print("|           4 Deletar                      |")
    print("|           5 Listar                       |")
    print("|           0 Sair                         |")
    print("|__________________________________________|\n")
    opcao_cliente = str(input("Escolha sua opção: "))

    return opcao_cliente
                

def cadastro_cliente():
    os.system('clear')
    print("____________________________________________")
    print("|                                          |")
    print("|           Cadastro de Cliente            |")
    print("|__________________________________________|\n")
    
    nome = str(input("Nome: "))
    cpf = str(input("\nCPF: "))
    endereco = str(input("\nEndereço: "))
    telefone = str(input("\nTelefone: "))
    print()
    clientes[cpf] = [nome,endereco,telefone]

    print("\n\nCliente cadastrado com sucesso!\n")
    input("Tecle <ENTER> para continuar...")


def listar_cliente():
    os.system('clear')
    print("____________________________________________")
    print("|                                          |")
    print("|          Listar Dados do Cliente         |")
    print("|__________________________________________|\n")

    cpf = str(input("Qual o CPF do cliente? : "))
    print("\nNome: ",clientes[cpf][0])
    print("\nCPF: ",cpf)
    print("\nEndereço: ",clientes[cpf][1])
    print("\nTelefone: ",clientes[cpf][2])
    print()

    input("Tecle <ENTER> para continuar...")

def atualizar_cliente():
    os.system('clear')
    print("____________________________________________")
    print("|                                          |")
    print("|         Atualizar Dados do Cliente       |")
    print("|__________________________________________|\n")
    
    cpf = str(input("Qual o CPF do cliente? : "))

    if cpf in clientes: 
        nome = str(input("\nNome: "))
        endereco = str(input("\nEndereço: "))
        telefone = str(input("\nTelefone: "))

    clientes[cpf] = [nome,endereco,telefone]

    print("\nCliente atualizado com sucesso!\n")
    input("Tecle <ENTER> para continuar...")

def excluir_cliente():
    os.system('clear')
    print("____________________________________________")
    print("|                                          |")
    print("|           Excluir Dados do Cliente       |")
    print("|__________________________________________|\n")

    cpf = str(input("Qual o CPF do cliente? : "))
    
    if cpf in clientes:
        print("\nNome: ",clientes[cpf][0])
        print("\nEndereço: ",clientes[cpf][1])
        print("\nTelefone: ",clientes[cpf][2])
        print()

        resposta = input("Deseja exluir o cliente? (S/N)")
        if resposta == 'S' or resposta == 's':
            del clientes[cpf]
            print("Cliente excluido com sucesso!")
        else:
            print("Exclusão não realizada!")
    else:
        print("Esse cliente não existe!")
    
    input("Tecle <ENTER> para continuar...")



