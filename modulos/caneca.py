import os

# IDcaneca -> modelo, cor, quantidadeEstoque, valor
canecas = {
    '0': ["Caneca do batman", "preta", 10, 50.00],
    '1': ["Caneca do superman", "azul", 20, 45.00],
    '2': ["Caneca do flash", "vermelha", 15, 40.00],
    '3': ["Caneca do lanterna verde", "verde", 25, 55.00],
    '4': ["Caneca do homem de ferro", "dourada", 30, 60.00],
    '5': ["Caneca da Mulher Maravilha", "roxa", 12, 48.00]
}

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

def cadastro_caneca():
    os.system('clear')
    print("____________________________________________")
    print("|                                          |")
    print("|           Cadastro de Caneca             |")
    print("|__________________________________________|\n")
    
    modelo = str(input("Modelo:"))
    cor  = str(input("Cor: "))
    quantidade = int(input("Quantidade: "))
    valor = float(input("valor: "))
    id = len(canecas) + 1

    canecas[id] = [modelo,cor,quantidade,valor]

    print("\n\nCaneca cadastrada com sucesso!\n")
    input("Tecle <ENTER> para continuar...")

def listar_caneca():
    os.system('clear')
    print("____________________________________________")
    print("|                                          |")
    print("|             Listar Caneca                |")
    print("|__________________________________________|\n")

    id = input("Qual o ID da caneca? : ")
    print("\nID: ", id)
    print("Modelos: ", canecas[id][0])
    print("Cores: ", canecas[id][1])
    print("Quantidade em Estoque: ", canecas[id][2])
    print("Valores: ",canecas[id][3])
    

    input("Tecle <ENTER> para continuar...")

def atualizar_caneca():
    os.system('clear')
    print("____________________________________________")
    print("|                                          |")
    print("|             Atualizar Caneca             |")
    print("|__________________________________________|\n")

    id = input("Qual o ID da caneca? : ")
    
    if id in canecas:

        modelo = str(input("\nModelo:"))
        cor  = str(input("Cor: "))
        quantidade = int(input("Quantidade: "))
        valor = float(input("valor: "))

    canecas[id] = [modelo,cor,quantidade,valor]

    print("\n\nCaneca atualizada com sucesso!\n")
    input("Tecle <ENTER> para continuar...")

def excluir_caneca():
    os.system('clear')
    print("____________________________________________")
    print("|                                          |")
    print("|             Deletar Caneca               |")
    print("|__________________________________________|\n")

    id = input("Qual o ID da caneca? : ")

    if id in canecas:

        print("\nModelo: ",canecas[id][0])
        print("Cor: ",canecas[id][1])
        print("Quantidade: ",canecas[id][2])
        print("Valor: ", canecas[id][3])
        print()
        resposta = input("Deseja exluir a caneca do estoque? (S/N)")
        if resposta == 'S' or resposta == 's':
            del canecas[id]
            print("Exclusão realizada!")
        else:
            print("Exclusão não realizada!")
    else:
        print("Essa caneca não existe!")
    
    input("Tecle <ENTER> para continuar...")