from conexion.oracle_queries import OracleQueries
from model.funcionario import Funcionario

class Funcionario_Control:
    def __init__(self):
        pass

    # INSERIR NOVO FUNCIONARIO
    def inserir_funcionario(self) -> Funcionario:
        
        # Conexão com o banco
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        codigo_cartao = input("Insira um novo codigo(6 digitos) de cartão: ")

        #VERIFICAÇÃO DE EXISTENCIA DE FUNCIONARIO // CRIAÇÃO DE NOVO FUNCIONARI
        if self.verifica_funcionario_exist(oracle, codigo_cartao):
            nome = input("Nome completo: ")
            cpf = input("CPF: ")
            salario = input("Salario estimado:")
            oracle.write(f"'{nome}', '{codigo_cartao}', '{cpf}' e '{salario}' inseridos!")
            df_funcionario = oracle.sqlToDataFrame(f"selecione nome, codigo_cartao, cpf, salario do codigo_cartao = '{codigo_cartao}' ")
            novo_funcionario = Funcionario(df_funcionario.nome.values[0],df_funcionario.codigo_cartao.values[0], df_funcionario.cpf.values[0], df_funcionario.salario.values[0])
            print (novo_funcionario.to_string())
            return novo_funcionario
        
        else:
            print(f"{codigo_cartao} já registrado!")
            return None


    #ATUALIZAÇÃO DE FUNCIONARIO
    def atualizar_funcionario(self) -> Funcionario:
            
        oracle = OracleQueries(can_write = True)
        oracle.connect()

        codigo_cartao = int(input("Insira o codigo (6 digitos) do funcionario que deseja alterar as informações: "))

        if not self.verifica_funcionario_exist(oracle, codigo_cartao):
            novo_nome = input("Insira o novo nome completo: ")
            novo_cpf = input("Insira o novo CPF: ")
            novo_salario = input("Insira o novo salario: ")
            oracle.write(f"'{novo_nome}', '{novo_cpf}' e '{novo_salario}' foram atualizados! ")
            df_funcionario = oracle.sqlToDataFrame(f"selecione nome, codigo_cartao, cpf e salario do codigo_cartao = '{codigo_cartao}'")
            funcionario_update = Funcionario(df_funcionario.nome.values[0],df_funcionario.codigo_cartao.values[0], df_funcionario.cpf.values[0], df_funcionario.salario.values[0])
            print(funcionario_update.to_string())
            return funcionario_update

        else:
            print(f"O codigo {codigo_cartao} não existe")
            return None 
            
    #EXCLUSÃO DE FUNCIONARIO  
    def excluir_funcionario(self):
         
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        codigo_cartao = int(input("Insira o codigo que deseja excluir: "))

        if not self.verifica_funcionario_exist(oracle, codigo_cartao):
            df_funcionario = oracle.sqlToDataFrame(f"selecione nome, codigo_cartao, cpf, salario do codigo_cartao = '{codigo_cartao}'")
            oracle.write(f"Funcionario com codigo '{codigo_cartao}' será deletado!")
            funcionario_exclusão = Funcionario(df_funcionario.nome.values[0],df_funcionario.codigo_cartao.values[0], df_funcionario.cpf.values[0], df_funcionario.salario.values[0])
            print(f"Funcionario de '{codigo_cartao}' foi removido do sistema ")
            print(funcionario_exclusão.to_string())

        else:
            print(f"O codigo {codigo_cartao} não existe!")  

    def verificar_funcionario_exist(self, oracle:OracleQueries, codigo_cartao: str = None) -> bool:
    
        df_funcionario = oracle.sqlToDataFrame(f"selecione nome, codigo_cartao, cpf e salario do codigo_cartao = {codigo_cartao}")
        return df_funcionario.empty                