from datetime import date, time, timedelta
import datetime
from conexion.oracle_queries import OracleQueries
from controller.funcionario_control import Funcionario_Control
from model.funcionario import Funcionario
from model.cartao_ponto import CartaoPonto


class Cartao_Ponto_Control:
    def __init__(self):
        self.ctrl_funcionario = Funcionario_Control()

    #INSERÇÃO DE PONTO
    def inserir_cartao_ponto(self) -> CartaoPonto:
        
        
        oracle = OracleQueries()
        guia = oracle.connect()
        output_value = guia.var(int)

        self.listar_funcionarios(oracle, need_connect=True)
        
        codigo_cartao = str(input("Digite o codigo (6 digitos) do Funcionario: "))
        funcionario = self.valida_funcionario(oracle, codigo_cartao)
        if funcionario == None:
            return None
        
        hora_atual = datetime.datetime.now()
        hora_formatada = hora_atual.strftime("%H:%M")
        intervalo_tempo = timedelta(hours=8, minutes=00)
        tempo_saida = hora_formatada + intervalo_tempo

        data = dict (codigo_cartao = funcionario.get_codigo_cartao(), dia_trabalho = output_value, hora_entrada = hora_formatada, hora_saida = tempo_saida)

        dia_trabalhado = output_value.getvalue()
        oracle.conn.commit()

        df_dia_trabalhado = oracle.sqlToDataFrame(f"Selecione codigo_cartao, dia_trabalhado, hora_entrada, hora_saida onde dia_trabalho = {dia_trabalhado}")
        novo_dia = CartaoPonto(df_dia_trabalhado.dia_trabalho.values[0], df_dia_trabalhado.hora_entrada.values[0], df_dia_trabalhado.hora_saida.values[0], funcionario)
        
        print(novo_dia.to_string())
        return novo_dia
    
    # ATUALIZAÇÃO DE DIA
    def atualizar_cartao_ponto(self) -> CartaoPonto:
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        dia_trabalhado = (input("Insira o dia que deseja alterar o horario: "))
        if not self.verificar_funcionario_exist(oracle, need_connect=True):
            self.listar_funcionarios(oracle)
            codigo_cartao = int(input("Digite o codigo (6 digitos) do Funcionario: "))
            funcionario = self.valida.funcionario(oracle, codigo_cartao)
            if funcionario == None:
                return None
            
    
            hora_atual = datetime.datetime.now()
            hora_formatada = hora_atual.strftime("%H:%M")
            intervalo_tempo = timedelta(hours=8, minutes=00)
            tempo_saida = hora_formatada + intervalo_tempo

            oracle.write(f"O dia trabalhado do funcionario de codigo '{funcionario.get.codigo_cartao()} foi atualizado para dia '{dia_trabalhado}', horario de entrada: '{hora_formatada} e horario de saida: '{tempo_saida}")
            df_dia_trabalhado = oracle.sqlToDataFrame(f"Selecione codigo_cartao, dia_trabalhado, hora_entrada, hora_saida onde dia_trabalho = {dia_trabalhado}")
            dia_atualizado = CartaoPonto(df_dia_trabalhado.dia_trabalho.values[0], df_dia_trabalhado.hora_entrada.values[0], df_dia_trabalhado.hora_saida.values[0], funcionario)
            print(dia_atualizado.to_String())
            return dia_atualizado
        else:
            print(f"O funcionario de codigo {codigo_cartao} não trabalhou no dia {dia_trabalhado}")


        # EXCLUSAO DE DIA
        def excluir_cartao_ponto(self) -> CartaoPonto:
            oracle = OracleQueries(can_write=True)
            oracle.connect()

            if not self.verifica_dia_exist(oracle,dia_trabalhado, codigo_cartao):
                df_dia_trabalhado = oracle.sqlToDataFrame(f"Selecione codigo_cartao, dia_trabalhado, hora_entrada, hora_saida onde dia_trabalho = {dia_trabalhado}")
                funcionario = self.valida_funcionario(oracle,df_dia_trabalhado.codigo_cartao.values[0])

                excluir_opcao = input("Deseja excluir o dia '{dia_trabalhado}'(S ou N): ")
                if excluir_opcao.lower() == "s":
                    oracle.write(f"delete o dia_trabalhado onde codigo_cartao = {codigo_cartao}")
                    print("Dia removido com sucesso!")
                    dia_excluido = CartaoPonto(df_dia_trabalhado.dia_trabalho.values[0], df_dia_trabalhado.hora_entrada.values[0], df_dia_trabalhado.hora_saida.values[0], funcionario)
                    print(dia_excluido.to_string())

            else:
                print(f"O funcionario de codigo {codigo_cartao} não trabalhou no dia {dia_trabalhado}")       
     





        

