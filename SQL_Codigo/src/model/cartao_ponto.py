class CartaoPonto:
    def __init__ (self,dia_trabalho: str = None, data_entrada: str = None, data_saida: str = None):
        self.set_dia_trabalho(dia_trabalho)
        self.set_data_entrada(data_entrada)
        self.set_data_saida(data_saida)

    def set_dia_trabalho(self, dia_trabalho:str):
        self.dia_trabalho = dia_trabalho

    def set_data_entrada(self,data_entrada:str):
        self.data_entrada = data_entrada

    def set_data_saida(self, data_saida: str):
        self.data_saida = data_saida

    def get_dia_trabalho(self) -> str:
        return self.dia_trabalho

    def get_data_entrada(self) -> str:
        return self.data_entrada

    def get_data_saida(self) -> str:
        return self.data_saida

    def to_String(self) -> str:
        return f"Dia de Trabalho: {self.get_dia_trabalho()} // Data de Entrada: {self.get_data_entrada()} // Data de Saida: {self.get_data_saida()} "         