opcao = ''
while opcao != 0:
    print("###################################################")
    print("###############  Sistema SIG-Cup   ################")
    print("###################################################")
    print("##           1 Clientes                          ##")
    print("##           2 Canecas                           ##")
    print("##           3 Pedidos                           ##")
    print("##           0 Sair                              ##")
    print("###################################################")
    print("\n")
    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:

        print("############################################")
        print("#####            Clientes               ####")
        print("############################################")
        print("##           1 Cadastrar                  ##")
        print("##           2 Listar                     ##")
        print("##           3 Atualizar                  ##")
        print("##           4 Deletar                    ##")
        print("##           0 Sair                       ##")
        print("############################################")

    elif opcao == 2:
        print("############################################")
        print("#####            Canecas                ####")
        print("############################################")
        print("##           1 Cadastrar                  ##")
        print("##           2 Listar                     ##")
        print("##           3 Atualizar                  ##")
        print("##           4 Deletar                    ##")
        print("##           0 Sair                       ##")
        print("############################################")

    elif opcao == 3:
        print("############################################")
        print("#####            Pedidos                ####")
        print("############################################")
        print("##           1 Cadastrar                  ##")
        print("##           2 Listar                     ##")
        print("##           3 Atualizar                  ##")
        print("##           4 Deletar                    ##")
        print("##           0 Sair                       ##")
        print("############################################")

    elif opcao == 0:
        print("Encerrando o programa")
    else:
        print("Opção inválida!")    