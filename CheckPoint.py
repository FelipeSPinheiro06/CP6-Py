def alterar_registro(cursor):
    lista_dados = []

    id_professor = int(input("Digite o id do professor que deseja alterar: "))

    query = f"""SELECT * FROM PROFESSORES WHERE id = {id_professor}"""

    cursor.execute(query)
    dados = cursor.fetchall()

    for dado in lista_dados:
        lista_dados.append(dado)

    if(len(lista_dados) == 0):
        print("Não existe registros na tabela!")
    
    else:
        try:
            nome_professor = input("Nome: ")
            cpf_professor = int(input("CPF: "))
            idade_professor = int(input("Idade: "))
            titualacao_max = input("Titulação: ")
        except ValueError:
            print("Digite valores numéricos")
        except:
            print("Erro de transação com o banco")
        else:
            alteracao = f"""UPDATE PROFESSORES SET PROFESSOR_NOME = '{nome_professor}', PROFESSOR_CPF = {cpf_professor}, PROFESSOR_IDADE = {idade_professor}, PROFESSOR_TITULACAOMAX = '{titualacao_max}'"""
            cursor.execute(alteracao)
        finally:
            print("Professor alterado com sucesso!")

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