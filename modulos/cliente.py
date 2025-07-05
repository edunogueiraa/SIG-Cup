import os
import modulos.valida

def menu_cliente ():
    os.system('clear')
    print("____________________________________________")
    print("|                                          |")
    print("|                Clientes                  |")
    print("|__________________________________________|")
    print("|                                          |")
    print("|           1 Cadastrar                    |")
    print("|           2 Listar Dados                 |")
    print("|           3 Atualizar                    |")
    print("|           4 Deletar                      |")
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
    while not(modulos.valida.validar_nome(nome)):
        print("Esse nome é invalido! Digite novamente: ")
        nome = str(input("Nome: "))

    cpf = str(input("CPF: "))
    while not(modulos.valida.validar_cpf(cpf)):
        print("Esse CPF é invalido! Digite novamente: ")
        cpf = str(input("CPF: "))

    endereco = str(input("Endereço: "))

    telefone = str(input("Telefone: "))
    while not(modulos.valida.validar_telefone(telefone)):
        print("Esse telefone é invalido! Digite novamente: EX(DDD 99999-9999)")
        telefone = str(input("Telefone: "))

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
    if cpf in clientes:
        print("\nNome: ",clientes[cpf][0])
        print("CPF: ",cpf)
        print("Endereço: ",clientes[cpf][1])
        print("Telefone: ",clientes[cpf][2])
        print()
    else: 
        print("\n\nNão existe cliente com esse CPF!")

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

        print("\n\nCliente atualizado com sucesso!\n")
    else:
        print("\n\nNão existe cliente com esse CPF!")

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
            print("\n\nCliente excluido com sucesso!")
        else:
            print("\n\nExclusão não realizada!")
    else:
        print("\n\nNão existe cliente com esse CPF!")
    
    input("Tecle <ENTER> para continuar...")



