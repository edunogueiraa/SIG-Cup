import os

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
                

def cadastro_cliente(clientes):
    os.system('clear')
    print("____________________________________________")
    print("|                                          |")
    print("|           Cadastro de Cliente            |")
    print("|__________________________________________|\n")
    
    nome = str(input("Nome: "))
    cpf = str(input("CPF: "))
    endereco = str(input("Endereço: "))
    telefone = str(input("Telefone: "))
    print()
    clientes[cpf] = [nome,endereco,telefone]

    print("\n\nCliente cadastrado com sucesso!\n")
    input("Tecle <ENTER> para continuar...")


def listar_cliente(clientes):
    os.system('clear')
    print("____________________________________________")
    print("|                                          |")
    print("|          Listar Dados do Cliente         |")
    print("|__________________________________________|\n")

    cpf = str(input("Qual o CPF do cliente? : "))
    print("\nNome: ",clientes[cpf][0])
    print("CPF: ",cpf)
    print("Endereço: ",clientes[cpf][1])
    print("Telefone: ",clientes[cpf][2])
    print()

    input("Tecle <ENTER> para continuar...")

def atualizar_cliente(clientes):
    os.system('clear')
    print("____________________________________________")
    print("|                                          |")
    print("|         Atualizar Dados do Cliente       |")
    print("|__________________________________________|\n")
    
    cpf = str(input("Qual o CPF do cliente? : "))

    if cpf in clientes: 
        nome = str(input("\nNome: "))
        endereco = str(input("Endereço: "))
        telefone = str(input("Telefone: "))

    clientes[cpf] = [nome,endereco,telefone]

    print("\nCliente atualizado com sucesso!\n")
    input("Tecle <ENTER> para continuar...")

def excluir_cliente(clientes):
    os.system('clear')
    print("____________________________________________")
    print("|                                          |")
    print("|           Excluir Dados do Cliente       |")
    print("|__________________________________________|\n")

    cpf = str(input("Qual o CPF do cliente? : "))
    
    if cpf in clientes:
        print("\nNome: ",clientes[cpf][0])
        print("Endereço: ",clientes[cpf][1])
        print("Telefone: ",clientes[cpf][2])
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



