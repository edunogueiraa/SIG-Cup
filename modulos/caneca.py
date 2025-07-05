import os

def menu_caneca():
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
    print("|__________________________________________|\n")
    opcao_caneca = str(input("Escolha sua opção: "))
    
    return opcao_caneca

def cadastro_caneca(canecas):
    os.system('clear')
    print("____________________________________________")
    print("|                                          |")
    print("|           Cadastro de Caneca             |")
    print("|__________________________________________|\n")
    
    modelo = str(input("Modelo: "))
    cor  = str(input("Cor: "))
    quantidade = int(input("Quantidade: "))
    valor = float(input("valor: "))
    id = max(canecas.keys()) + 1

    canecas[id] = [modelo,cor,quantidade,valor]

    print("\n\nCaneca cadastrada com sucesso!")
    input("\nTecle <ENTER> para continuar...")

def listar_caneca(canecas):
    os.system('clear')
    print("____________________________________________")
    print("|                                          |")
    print("|             Listar Caneca                |")
    print("|__________________________________________|\n")

    id = int(input("Qual o ID da caneca? : "))

    if id in canecas.keys():
        print("\nID: ", id)
        print("Modelo: ", canecas[id][0])
        print("Cor: ", canecas[id][1])
        print("Quantidade em Estoque: ", canecas[id][2])
        print("Valor: R$ %.2f"%canecas[id][3])
    else:
        print("Caneca não existe! \nVeja outras:\n")
        #Mostrando outras canecas disponiveis
        for id, item in canecas.items():
            print("ID:",id, item[0])
    
    input("\nTecle <ENTER> para continuar...")

def atualizar_caneca(canecas):
    os.system('clear')
    print("____________________________________________")
    print("|                                          |")
    print("|             Atualizar Caneca             |")
    print("|__________________________________________|\n")

    id = int(input("Qual o ID da caneca? : "))
    
    if id in canecas:

        modelo = str(input("\nModelo:"))
        cor  = str(input("Cor: "))
        quantidade = int(input("Quantidade: "))
        valor = float(input("valor: "))

        canecas[id] = [modelo,cor,quantidade,valor]

        print("\n\nCaneca atualizada com sucesso!")
    else:
        print("\n\nEssa caneca não existe!")

    input("\nTecle <ENTER> para continuar...")

def excluir_caneca(canecas):
    os.system('clear')
    print("____________________________________________")
    print("|                                          |")
    print("|             Deletar Caneca               |")
    print("|__________________________________________|\n")

    id = int(input("Qual o ID da caneca? : "))

    if id in canecas:

        print("\nModelo: ",canecas[id][0])
        print("Cor: ",canecas[id][1])
        print("Quantidade: ",canecas[id][2])
        print("Valor: R$ %.2f"%canecas[id][3])
        print()
        resposta = input("Deseja exluir a caneca do estoque? (S/N)")
        if resposta == 'S' or resposta == 's':
            del canecas[id]
            print("\n\nExclusão realizada!")
        else:
            print("\n\nExclusão não realizada!")
    else:
        print("\n\nEssa caneca não existe!")
    
    input("\nTecle <ENTER> para continuar...")