# Sistema de Ouvidoria
# Paulo César Dantas da Silva 20262500013

manifestacoes = []

contador_denuncia = 1
contador_reclamacao = 1
contador_solicitacao = 1
contador_sugestao = 1
contador_elogio = 1

opcao = 0

while opcao != 5:

    print("\n=========== SISTEMA DE OUVIDORIA =========")
    print("1 - CADASTRAR MANIFESTAÇÃO")
    print("2 - LISTAR MANIFESTAÇÕES")
    print("3 - PESQUISAR MANIFESTAÇÕES")
    print("4 - REMOVER MANIFESTAÇÃO")
    print("5 - SAIR")

    opcao = int(input("Digite uma opção: "))

    # CADASTRAR A MANIFESTAÇÃO

    if opcao == 1:

        print("\n--- TIPOS DE MANIFESTAÇÃO ---")
        print("1 - Denúncia")
        print("2 - Reclamação")
        print("3 - Solicitação")
        print("4 - Sugestão")
        print("5 - Elogio")

        tipo = int(input("Escolha o tipo de manifestação: "))

        if tipo == 1:
            tipo_manifestacao = "Denúncia"
            sigla = "DEN"
            sequencial = contador_denuncia

        elif tipo == 2:
            tipo_manifestacao = "Reclamação"
            sigla = "REC"
            sequencial = contador_reclamacao

        elif tipo == 3:
            tipo_manifestacao = "Solicitação"
            sigla = "SOL"
            sequencial = contador_solicitacao

        elif tipo == 4:
            tipo_manifestacao = "Sugestão"
            sigla = "SGT"
            sequencial = contador_sugestao

        elif tipo == 5:
            tipo_manifestacao = "Elogio"
            sigla = "ELG"
            sequencial = contador_elogio

        else:
            tipo_manifestacao = ""

        if tipo_manifestacao == "":
            print("Tipo de manifestação inválida!")

        else:
            nome = input("Digite seu nome: ")
            texto = input("Digite sua manifestação: ")

            if texto == "":
                print("A manifestação não pode estar vazia.")

            else:
                numero = str(sequencial)

                if sequencial < 10:
                    numero = "00" + numero

                elif sequencial < 100:
                    numero = "0" + numero

                codigo = sigla + "-2026-" + numero

                manifestacao = [codigo, nome, tipo_manifestacao, texto]

                manifestacoes.append(manifestacao)

                print("\nManifestação cadastrada com sucesso!")
                print("Protocolo:", codigo)

                if tipo == 1:
                    contador_denuncia = contador_denuncia + 1

                elif tipo == 2:
                    contador_reclamacao = contador_reclamacao + 1

                elif tipo == 3:
                    contador_solicitacao = contador_solicitacao + 1

                elif tipo == 4:
                    contador_sugestao = contador_sugestao + 1

                elif tipo == 5:
                    contador_elogio = contador_elogio + 1

    # LISTAR MANIFESTAÇÕES

    elif opcao == 2:

        if len(manifestacoes) == 0:
            print("Nenhuma manifestação cadastrada!")

        else:
            print("\n========== MANIFESTAÇÕES CADASTRADAS ==========")

            for i in range(len(manifestacoes)):
                print("\nProtocolo:", manifestacoes[i][0])
                print("Nome:", manifestacoes[i][1])
                print("Tipo:", manifestacoes[i][2])
                print("Descrição:", manifestacoes[i][3])

    # PESQUISAR MANIFESTAÇÕES

    elif opcao == 3:

        print("\n========= PESQUISAR MANIFESTAÇÕES =========")
        print("1 - PESQUISAR POR TIPO")
        print("2 - PESQUISAR POR NOME")

        opcao_pesquisa = int(input("Escolha uma opção de pesquisa: "))

        # PESQUISAR POR TIPO

        if opcao_pesquisa == 1:

            print("\n========= PESQUISAR POR TIPO =========")
            print("1 - Denúncia")
            print("2 - Reclamação")
            print("3 - Solicitação")
            print("4 - Sugestão")
            print("5 - Elogio")

            tipo_pesquisa = int(input("Escolha o tipo de pesquisa: "))

            if tipo_pesquisa == 1:
                pesquisa = "Denúncia"

            elif tipo_pesquisa == 2:
                pesquisa = "Reclamação"

            elif tipo_pesquisa == 3:
                pesquisa = "Solicitação"

            elif tipo_pesquisa == 4:
                pesquisa = "Sugestão"

            elif tipo_pesquisa == 5:
                pesquisa = "Elogio"

            else:
                pesquisa = ""

            if pesquisa == "":
                print("Tipo inválido.")

            else:
                encontrou = False

                print("\n--- RESULTADO DA PESQUISA ---")

                for manifestacao in manifestacoes:

                    if manifestacao[2] == pesquisa:
                        print("\nProtocolo:", manifestacao[0])
                        print("Nome:", manifestacao[1])
                        print("Tipo:", manifestacao[2])
                        print("Descrição:", manifestacao[3])

                        encontrou = True

                if encontrou == False:
                    print("Nenhuma manifestação desse tipo foi encontrada.")

        # PESQUISAR POR NOME

        elif opcao_pesquisa == 2:

            nome_pesquisa = input("Digite o nome que deseja pesquisar: ")

            encontrou = False

            print("\n--- RESULTADO DA PESQUISA ---")

            for manifestacao in manifestacoes:

                if manifestacao[1] == nome_pesquisa:
                    print("\nProtocolo:", manifestacao[0])
                    print("Nome:", manifestacao[1])
                    print("Tipo:", manifestacao[2])
                    print("Descrição:", manifestacao[3])

                    encontrou = True

            if encontrou == False:
                print("Nenhuma manifestação encontrada para esse nome.")

        else:
            print("Opção de pesquisa inválida.")

    # REMOVER MANIFESTAÇÃO

    elif opcao == 4:

        if len(manifestacoes) == 0:
            print("Nenhuma manifestação cadastrada.")

        else:
            print("\n========== MANIFESTAÇÕES CADASTRADAS ==========")

            for manifestacao in manifestacoes:
                print(
                    manifestacao[0],
                    "-",
                    manifestacao[1],
                    "-",
                    manifestacao[2],
                    "-",
                    manifestacao[3]
                )

            codigo_remover = input(
                "\nDigite o protocolo da manifestação que deseja remover: "
            )

            encontrou = False

            for manifestacao in manifestacoes:

                if manifestacao[0] == codigo_remover:
                    manifestacoes.remove(manifestacao)
                    encontrou = True

                    print("Manifestação removida com sucesso!")
                    break

            if encontrou == False:
                print("Protocolo não localizado.")

    # SAIR

    elif opcao == 5:
        print("\nSistema encerrado.")

    # OPÇÃO INVÁLIDA

    else:
        print("Opção inválida.")
