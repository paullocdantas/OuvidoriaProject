
# Sistema de Ouvidoria
# Paulo César Dantas da Silva 20262500013

import mysql.connector
import config_local

# CONEXÃO COM O BANCO DE DADOS

conexao = mysql.connector.connect(
    host=config_local.DB_HOST,
    user=config_local.DB_USER,
    password=config_local.DB_PASSWORD,
    database=config_local.DB_NAME
)

print("Conexão com o banco de dados realizada com sucesso!")

contador_denuncia = 1
contador_reclamacao = 1
contador_solicitacao = 1
contador_sugestao = 1
contador_elogio = 1

# CONSULTAR OS PROTOCOLOS JÁ CADASTRADOS NO MYSQL

cursor = conexao.cursor()

cursor.execute("SELECT protocolo FROM manifestacoes")

protocolos = cursor.fetchall()

for protocolo in protocolos:

    codigo_existente = protocolo[0]

    if codigo_existente is not None:

        partes = codigo_existente.split("-")

        if len(partes) == 3 and partes[2].isdigit():

            numero_existente = int(partes[2]) + 1

            if partes[0] == "DEN" and numero_existente > contador_denuncia:
                contador_denuncia = numero_existente

            elif partes[0] == "REC" and numero_existente > contador_reclamacao:
                contador_reclamacao = numero_existente

            elif partes[0] == "SOL" and numero_existente > contador_solicitacao:
                contador_solicitacao = numero_existente

            elif partes[0] == "SGT" and numero_existente > contador_sugestao:
                contador_sugestao = numero_existente

            elif partes[0] == "ELG" and numero_existente > contador_elogio:
                contador_elogio = numero_existente

cursor.close()

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

                # GRAVAR A MANIFESTAÇÃO NO MYSQL

                cursor = conexao.cursor()

                sql = """
                INSERT INTO manifestacoes (protocolo, nome, tipo, descricao)
                VALUES (%s, %s, %s, %s)
                """

                valores = (codigo, nome, tipo_manifestacao, texto)

                cursor.execute(sql, valores)

                conexao.commit()

                cursor.close()

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

        cursor = conexao.cursor()

        cursor.execute(
            "SELECT protocolo, nome, tipo, descricao FROM manifestacoes"
        )

        manifestacoes_banco = cursor.fetchall()

        if len(manifestacoes_banco) == 0:
            print("Nenhuma manifestação cadastrada!")

        else:
            print("\n========== MANIFESTAÇÕES CADASTRADAS ==========")

            for manifestacao in manifestacoes_banco:
                print("\nProtocolo:", manifestacao[0])
                print("Nome:", manifestacao[1])
                print("Tipo:", manifestacao[2])
                print("Descrição:", manifestacao[3])

        cursor.close()

    # PESQUISAR MANIFESTAÇÕES

    elif opcao == 3:

        print("\n========= PESQUISAR MANIFESTAÇÕES =========")
        print("1 - PESQUISAR POR TIPO")
        print("2 - PESQUISAR POR NOME")
        print("3 - PESQUISAR POR PROTOCOLO")

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

                cursor = conexao.cursor()

                sql = """
                SELECT protocolo, nome, tipo, descricao
                FROM manifestacoes
                WHERE tipo = %s
                """

                cursor.execute(sql, (pesquisa,))

                resultados = cursor.fetchall()

                print("\n--- RESULTADO DA PESQUISA ---")

                if len(resultados) == 0:
                    print("Nenhuma manifestação desse tipo foi encontrada.")

                else:
                    for manifestacao in resultados:
                        print("\nProtocolo:", manifestacao[0])
                        print("Nome:", manifestacao[1])
                        print("Tipo:", manifestacao[2])
                        print("Descrição:", manifestacao[3])

                cursor.close()

        # PESQUISAR POR NOME

        elif opcao_pesquisa == 2:

            nome_pesquisa = input("Digite o nome que deseja pesquisar: ")

            cursor = conexao.cursor()

            sql = """
            SELECT protocolo, nome, tipo, descricao
            FROM manifestacoes
            WHERE nome = %s
            """

            cursor.execute(sql, (nome_pesquisa,))

            resultados = cursor.fetchall()

            print("\n--- RESULTADO DA PESQUISA ---")

            if len(resultados) == 0:
                print("Nenhuma manifestação encontrada para esse nome.")

            else:
                for manifestacao in resultados:
                    print("\nProtocolo:", manifestacao[0])
                    print("Nome:", manifestacao[1])
                    print("Tipo:", manifestacao[2])
                    print("Descrição:", manifestacao[3])

            cursor.close()

        # PESQUISAR POR PROTOCOLO

        elif opcao_pesquisa == 3:

            protocolo_pesquisa = input(
                "Digite o protocolo que deseja pesquisar: "
            )

            cursor = conexao.cursor()

            sql = """
            SELECT protocolo, nome, tipo, descricao
            FROM manifestacoes
            WHERE protocolo = %s
            """

            cursor.execute(sql, (protocolo_pesquisa,))

            resultados = cursor.fetchall()

            print("\n--- RESULTADO DA PESQUISA ---")

            if len(resultados) == 0:
                print("Nenhuma manifestação encontrada para esse protocolo.")

            else:
                for manifestacao in resultados:
                    print("\nProtocolo:", manifestacao[0])
                    print("Nome:", manifestacao[1])
                    print("Tipo:", manifestacao[2])
                    print("Descrição:", manifestacao[3])

            cursor.close()

        else:
            print("Opção de pesquisa inválida.")

    # REMOVER MANIFESTAÇÃO

    elif opcao == 4:

        cursor = conexao.cursor()

        cursor.execute(
            "SELECT protocolo, nome, tipo, descricao FROM manifestacoes"
        )

        manifestacoes_banco = cursor.fetchall()

        if len(manifestacoes_banco) == 0:
            print("Nenhuma manifestação cadastrada.")

        else:
            print("\n========== MANIFESTAÇÕES CADASTRADAS ==========")

            for manifestacao in manifestacoes_banco:
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

            sql = "DELETE FROM manifestacoes WHERE protocolo = %s"

            cursor.execute(sql, (codigo_remover,))

            if cursor.rowcount > 0:
                conexao.commit()
                print("Manifestação removida com sucesso!")

            else:
                print("Protocolo não localizado.")

        cursor.close()

    # SAIR

    elif opcao == 5:
        print("\nSistema encerrado.")

    # OPÇÃO INVÁLIDA

    else:
        print("Opção inválida.")

conexao.close()
