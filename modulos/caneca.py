import os

def caneca():
    os.system('clear')
    print("____________________________________________")
    print("|                                          |")
    print("|                Canecas                   |")
    print("|__________________________________________|")
    print("|                                          |")
    print("|           1 Cadastrar                    |")
    print("|           2 Listar                       |")
    print("|           3 Atualizar                    |")
    print("|           4 Deletar                      |")
    print("|           0 Sair                         |")
    print("|__________________________________________|")
    op_canecas = str(input("Escolha sua opção: "))

    match op_canecas != '0':

        case '1':
            os.system('clear')
            print("____________________________________________")
            print("|                                          |")
            print("|           Cadastro de Caneca             |")
            print("|__________________________________________|\n")
            
            cor  = str(input("Cor: "))
            valor = float(input("\nvalor: "))
            modelo = str(input("\nModelo:"))
            quantidade = int(input("\nQuantidade: "))
            #id = len(dicionário) + 1

            print("\n\nCaneca cadastrada com sucesso!\n")
            input("Tecle <ENTER> para continuar...")

        case '2':
            os.system('clear')
            print("____________________________________________")
            print("|                                          |")
            print("|             Listar Canecas               |")
            print("|__________________________________________|\n")

            print("Modelos: ", modelos)
            print("Cores: ", cores)
            print("Valores: ",valores)
            print("Quantidade em Estoque: ", quantidade_estoque)

            input("Tecle <ENTER> para continuar...")

        case '3':
            os.system('clear')
            print("____________________________________________")
            print("|                                          |")
            print("|             Atualizar Caneca             |")
            print("|__________________________________________|\n")

            id_atualizar_caneca = int(input("Digite o ID da caneca: "))
            cor  = str(input("\n\nCor: "))
            valor = float(input("\nvalor: "))
            modelo = str(input("\nModelo:"))
            quantidade = int(input("\nQuantidade: "))
            id = id_atualizar_caneca

            print("\n\nCaneca atualizada com sucesso!\n")
            input("Tecle <ENTER> para continuar...")

        case '4':
            os.system('clear')
            print("____________________________________________")
            print("|                                          |")
            print("|             Deletar Caneca               |")
            print("|__________________________________________|\n")

            id_deletar_caneca = int(input("Digite o ID da caneca: "))

            print("\n\nCaneca atualizada com sucesso!\n")
            input("Tecle <ENTER> para continuar...")

        case '0':
            print("Saindo do módulo canecas")