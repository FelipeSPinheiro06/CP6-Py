import oracledb as orcl

def alterar_registro(cursor):
    resp = 1
    while(resp != 0):
        print("0 - Sair")
        print("1 - Alterar o Professor")
        print("2 - Alterar o endereço do professor")
        opcao = int(input("Digite a sua opção (0-2): "))

        if(opcao == 0):
            resp = 0
        
        if(opcao == 1):
            lista_dados = []

            #Pegando o ID do professor
            id_professor = int(input("Digite o id do professor que deseja alterar: "))

            #Preparando o código que pega os dados
            query = f"""SELECT * FROM PROFESSORES WHERE id = {id_professor}"""

            #Executando o código
            cursor.execute(query)
            
            #Pegando todos os resultados do código executado
            dados = cursor.fetchall()

            #Adicionando na lista
            for dado in dados:
                lista_dados.append(dado)

            if(len(lista_dados) == 0): #Se for vazio, não há nada o que fazer
                print("Não existe registros na tabela!")
            
            else:
                try:
                    #Pegando os novos valores
                    nome_professor = input("Nome: ")
                    cpf_professor = int(input("CPF: "))
                    idade_professor = int(input("Idade: "))
                    titualacao_max = input("Titulação: ")
                except ValueError:
                    print("Digite valores numéricos")
                except:
                    print("Erro de transação com o banco")
                else:
                    #Preparando o comando
                    alteracao = f"""UPDATE PROFESSORES SET PROFESSOR_NOME = '{nome_professor}', PROFESSOR_CPF = {cpf_professor}, 
                                PROFESSOR_IDADE = {idade_professor}, PROFESSOR_TITULACAOMAX = '{titualacao_max}'"""
                    #Executando o comando
                    cursor.execute(alteracao)
                finally:
                    print("Professor alterado com sucesso!")

            resp = int(input("Deseja continuar (1-SIM/0-NÃO): "))

        if(opcao == 2):
            lista_dados_endereco = []

            #Pegando o ID do endereço
            id_endereco = int(input("Digite o id do endereço que deseja alterar: "))

            #Preparando o código que pega os dados
            query = f"""SELECT * FROM ENDERECOS WHERE ENDERECO_ID = {id_endereco}"""

            #Executando o código
            cursor.execute(query)
            
            #Pegando os resultados
            enderecos = cursor.fetchall()

            #Adicionando-os na lista
            for endereco in enderecos:
                lista_dados_endereco.append(endereco)

            if(len(lista_dados_endereco) == 0): #Se for vazio, não há nada o que fazer
                print("Não há registros na tabela!")

            else:
                try:
                    #Pegando os novos valores
                    logradouro = input("Nome: ")
                    bairro = input("Bairro: ")
                    cidade = input("Cidade: ")
                    estado = input("Estado: ")
                    cep = input("CEP: ")
                except ValueError:
                    print("Digite valores numéricos")
                except:
                    print("Erro de transação com o banco")
                else:
                    #Preparando o comando
                    alteracao = f"""UPDATE ENDERECOS SET ENDERECO_LOGRADOURO = '{logradouro}', ENDERECO_BAIRRO = '{bairro}', 
                                ENDERECO_CIDADE = '{cidade}', ENDERECO_ESTADO = '{estado}, ENDERECO_CEP = '{cep}'"""
                    #Executando o comando
                    cursor.execute(alteracao)
                finally:
                    print("Professor alterado com sucesso!")

            resp = int(input("Deseja continuar (1-SIM/0-NÃO): "))

        

def conecta_BD():

    try:
        #conectar com o Servidor
        str_conect = orcl.makedsn("oracle.fiap.com.br", "1521", "ORCL")
        #efetuar a conexao com o usuario
        conect = orcl.connect(user="RM99173", password="240102", dsn=str_conect)

        #Criar as instrucoes para cada modulo
        inst_SQL = conect.cursor()

    except Exception as e:
        print("Erro: ", e)
        conexao = False
        inst_SQL = ""
        conn = ""
    else:
        conexao = True

    return(conexao,inst_SQL,conn)