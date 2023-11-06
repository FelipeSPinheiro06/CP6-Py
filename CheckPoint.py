import oracledb as orcl
import brazilcep

# @Autor: def_main - Gustavo Vinhola - RM98826
# @Descrição: Função Principal do Programa
def main():
    conexao, inst_SQL = conecta_BD()

    while (conexao):
        print("1-Inserção")
        print("2-Consulta")
        print("3-Atualização")
        print("4-Exclusão")
        print("5-Sair")

        opc = int(input("Digite a opcao (1-5): "))

        if opc == 1:
            insere_professor(inst_SQL)  # Opção de inserção

        elif opc == 2:
            alterar_registro(inst_SQL)  # Opção de consulta e atualização

        elif opc == 3:
            alterar_registro(inst_SQL)  # Opção de atualização

        elif opc == 4:
            deleteRecord(inst_SQL)  # Opção de exclusão

        elif opc == 5:
            conexao = False

# @Autor: def - Rafael Chaves - RM99643
# @Descrição: Limpa todos os caracteres deixando apenas os numéros
def toCleanCpf(cpf):
    # Remove qualquer caractere não numérico do CPF
    cpfClean = ''.join(filter(str.isdigit, cpf))
    return cpfClean

# @Autor: def_insere - Gabriel Girami - RM98017
# @Descrição: Def insere_professor
def insere_professor(cursor):
    resp = 1
    while(resp != 0):
        print("0 - Sair")
        print("1 - Inserir informações do Professor")
        print("2 - Inserir o endereço do professor")
        opcao = int(input("Digite a sua opção (0-2): "))

        if(opcao == 0):
            resp = 0
        
        if(opcao == 1):
            try:
                cod = int(input("Digite o código do professor: "))
                nome = input("Digite o nome do professor: ")
                cpf = int(input("Digite o cpf do professor: "))
                idade = int(input("Digite a idade do professor: "))
                cep = int(input("Digite o cpf do professor: "))
                formacao = input("Digite a titulação do professor: ")
                endereco = int(input("Digite o cpf do professor: "))
            except ValueError:
                print("Digite apenas valores numéricos")
            else:
                
                #Fazendo a query
                inserir = f"""INSERT INTO TB_PROFESSOR (PROFESSOR_ID, PROFESSOR_NOME, 
                              PROFESSOR_CPF, PROFESSOR_IDADE, PROFESSOR_TITULACAO_MAX, ENDERECO_ID)
                              VALUES ({cod}, '{nome}', {cpf}, {idade}, {cep}, '{formacao}', {endereco});"""


                #Executando o comando
                cursor.execute(inserir)
                
            finally:
                print("Operação finalizada")

        else:        
            
            if(opcao ==2):
              try:
                      #Pegando os novos valores
                      cod_endereco = int(input("Digite o código do endereço: "))
                      cod_professor = int(input("Digite o código do professor: "))
                      cep = input("CEP: ")
                      try:
                          address = brazilcep.get_address_from_cep(cep)
                      except:
                          print("Erro de consulta com o cep")
                      else:
                          logradouro = address['street']
                          bairro = address['district']
                          cidade = address['city']
                          estado = address['state']
  
              except ValueError:
                      print("Digite valores numéricos")
              except:
                      print("Erro de transação com o banco")
              else:
                      #Preparando o comando
                      
                      #Comando antigo
                      '''
                        f"""ADD TB_ENDERECOS 
                        SET ENDERECO_LOGRADOURO = '{logradouro}', ENDERECO_BAIRRO = '{bairro}', 
                        ENDERECO_CIDADE = '{cidade}', ENDERECO_ESTADO 
                        = '{estado}, ENDERECO_CEP = '{cep}'"""
                      '''
                    
                      #Comando novo
                      inserir = f"""INSERT INTO TB_ENDERECO (ENDERECO_ID, ENDERECO_LOGRADOURO, 
                                    ENDERECO_BAIRRO, ENDERECO_CIDADE, 
                                    ENDERECO_ESTADO, ENDERECO_CEP, PROFESSOR_ID)
                                    VALUES ({cod_endereco}, '{logradouro}', '{bairro}', 
                                    '{cidade}', '{estado}', {cep}, {cod_professor});"""
  
                
                      #Executando o comando
                      cursor.execute(inserir)
              finally:
                      print("Professor alterado com sucesso!")
  
              resp = int(input("Deseja continuar (1-SIM/0-NÃO): "))





# @Autor: def - Felipe Santos Pinheiro - RM550244
# @Descrição: Método que altera os dados das duas tabelas do banco de dados
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
            query = f"""SELECT * FROM TB_PROFESSORES WHERE id = {id_professor}"""

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
                    alteracao = f"""UPDATE TB_PROFESSORES SET PROFESSOR_NOME = '{nome_professor}', 
                                    PROFESSOR_CPF = {cpf_professor}, 
                                    PROFESSOR_IDADE = {idade_professor}, PROFESSOR_TITULACAOMAX =
                                    '{titualacao_max}'"""
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
            query = f"""SELECT * FROM TB_ENDERECOS WHERE ENDERECO_ID = {id_endereco}"""

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
                    cep = input("CEP: ")
                    try:
                        address = brazilcep.get_address_from_cep(cep)
                    except:
                        print("Erro de consulta com o cep")
                    else:
                        logradouro = address['street']
                        bairro = address['district']
                        cidade = address['city']
                        estado = address['state']

                except ValueError:
                    print("Digite valores numéricos")
                except:
                    print("Erro de transação com o banco")
                else:
                    #Preparando o comando
                    alteracao = f"""UPDATE TB_ENDERECOS SET ENDERECO_LOGRADOURO ='{logradouro}', 
                                    ENDERECO_BAIRRO = '{bairro}', 
                                    ENDERECO_CIDADE = '{cidade}', 
                                    ENDERECO_ESTADO = '{estado}, ENDERECO_CEP = '{cep}'"""
                    #Executando o comando
                    cursor.execute(alteracao)
                finally:
                    print("Professor alterado com sucesso!")

            resp = int(input("Deseja continuar (1-SIM/0-NÃO): "))




# @Autor: def - Rafael Chaves - RM99643
# @Descrição: Método que deleta os dados no banco de dados Oracle 
def deleteRecord(script):
    while True:
        try:
            # Escolha(1-4) para decidir como que quer deletar os dados
            print("1 - Deseja deletar os dados referente ao Professor especifico?")
            print("2 - Deseja deletar os dados referente ao endereço do Professor?")
            print("3 - Deseja deletar todos os dados referente a uma conta de um professor?")
            print("4 - Deseja sair?")
            option = int(input("Digite a opção que deseja(1-4): "))

            # Solicitando CPF do Professor para que seja feita o delete com o filtro certo
            IcpfProfessor = input("Digite o CPF referente ao Professor que deseja deletar os dados: ")

            # Limpar o CPF removendo a pontuação e mantendo apenas os números
            cpf_professor = toCleanCpf(IcpfProfessor)

            # Verificar se o CPF possui 11 dígitos após a limpeza
            if len(cpf_professor) == 11:
                # Opção 1 - Deleta os dados do Professor escolhido
                if(option == 1):
                    # Verificar se o CPF possui 11 dígitos após a limpeza
                    if len(cpf_professor) == 11:
                        # Preparar o comando SQL de exclusão
                        scriptDelete = f"DELETE FROM TB_PROFESSORES WHERE PROFESSOR_CPF = {cpf_professor};"
                        
                        # Executar o comando de exclusão
                        script.execute(scriptDelete)

                        # Confirmar a transação
                        script.connection.commit()

                        # Print para confirmar a exclusão
                        print(f"Registro da tabela 'TB_PROFESSORES' excluído com sucesso.")
                    else:
                        # Se o cpf entrar errado
                        print(f"Cpf '{cpf_professor}' inválido!")

                # Opção 2 - Deleta os dados do Endereço escolhido
                elif (option == 2):
                    try:
                        # Preparar o comando SQL para consultar os endereços do professor com base no CPF
                        scriptSelect = f"""
                            SELECT P.PROFESSOR_CPF, E.ENDERECO_LOGRADOURO, E.ENDERECO_BAIRRO, 
                            E.ENDERECO_CIDADE, E.ENDERECO_ESTADO, E.ENDERECO_CEP FROM TB_PROFESSORES P
                            JOIN TB_ENDERECOS E 
                                ON P.PROFESSOR_ID = E.PROFESSOR_ID
                                WHERE P.PROFESSOR_CPF = '{cpf_professor}';
                        """
                        
                        # Executar o comando de seleção
                        script.execute(scriptSelect)
                        
                        # Pegar todos os endereços relacionados a esse CPF
                        enderecosProfessor = script.fetchall()
                        
                        if len(enderecosProfessor) != 0:
                            # Listar os endereços e permitir que o usuário escolha qual endereço excluir
                            print(f"Endereços relacionados a este CPF '{cpf_professor}': ")
                            for i, endereco in enumerate(enderecosProfessor):
                                print(f"{i + 1} - {endereco}")  # listar o(s) endereço(s) completo(s)

                            escolhaEndereco = int(input("Digite o número do endereço que deseja excluir: ")) - 1

                            if 0 <= escolhaEndereco < len(enderecosProfessor):
                                # Obter o ID do endereço selecionado
                                endereco_id = enderecosProfessor [escolhaEndereco] [0]

                                # Preparar o comando SQL de exclusão do endereço com base no ID
                                scriptDeleteEndereco = f"DELETE FROM ENDERECOS WHERE ENDERECO_ID = {endereco_id};"

                                # Executar o comando de exclusão
                                script.execute(scriptDeleteEndereco)

                                # Confirmar a transação
                                script.connection.commit()

                                print(f"Endereço excluído com sucesso.")
                            else:
                                print("Escolha de endereço inválida.")
                        else:
                            print(f"Nenhum endereço encontrado para o CPF: '{cpf_professor}'.")
                    except Exception as e:
                        print(f"Erro ao excluir registros: {e}")

                # Opção 3 - Deleta todos os dados do Professor e endereço escolhido
                elif (option == 3):
                    try:
                        # Preparar o comando SQL para consultar o Id do professor com base no CPF
                        scriptSearchId = f""" 
                            SELECT P.PROFESSOR_ID FROM TB_PROFESSORES P
                            JOIN TB_ENDERECOS E 
                                ON P.PROFESSOR_ID = E.PROFESSOR_ID
                                WHERE P.PROFESSOR_CPF = '{cpf_professor}';
                        """

                        # Executar o comando de exclusão
                        script.execute(scriptSearchId)
      
                        # Pegar o ID do professor
                        professor_id = script.fetchone()

                        if professor_id:
                            # Faz um Transactional para deletar todos os dados referente ao CPF selecionado
                            scriptDeleteAll = f"""
                                BEGIN
                                    EXECUTE IMMEDIATE 'ALTER TABLE TB_ENDERECOS DISABLE 
                                    CONSTRAINT FK_tbProfessor';
                                    
                                    DELETE FROM TB_PROFESSORES
                                        WHERE PROFESSOR_ID = {scriptSearchId[0]};
                                    DELETE FROM TB_ENDERECOS
                                        WHERE PROFESSOR_ID = {scriptSearchId[0]};
                                        
                                    EXECUTE IMMEDIATE 'ALTER TABLE TB_ENDERECOS ENABLE 
                                    CONSTRAINT FK_tbProfessor';
                                    COMMIT;
                                END;
                                /
                            """

                            script.execute(scriptDeleteAll)
                            print(f"Todos os dados referentes ao CPF {cpf_professor} foram excluídos com sucesso.")
                        else:
                            print(f"Não foi encontrado nenhum dado referente ao cpf: {cpf_professor}")
                    except Exception as e:
                        print(f"Erro ao excluir registros: {e}")
              
            else:
                # Se o cpf entrar errado
                print(f"Cpf '{cpf_professor}' inválido!")

            if (option == 4):
                print("Saindo...")
                break 
        
        except Exception as e:
            print(f"Erro ao excluir registros: {e}")


       

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
    else:
        conexao = True

    return(conexao,inst_SQL)

if (__name__ == "__main__"):
    main()



