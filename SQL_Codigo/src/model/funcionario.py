class Funcionario:
    def __init__(self, nome: str = None, CPF: str = None, salario: str = None, codigo_cartao: str = None):
        
                    self.set_nome(nome)
                    self.set_CPF(CPF)
                    self.set_salario(salario)
                    self.set_codigo_cartao(codigo_cartao)

    def set_nome(self, nome:str):
            self.nome = nome                

    def set_CPF(self, CPF:str):
            self.CPF = CPF
    
    def set_salario(self, salario:str):
            self.salario = salario
    
    def set_codigo_cartao(self, codigo_cartao):
            self.codigo_cartao = codigo_cartao
    
    def get_nome(self) -> str:
        return self.nome
    
    
    def get_CPF(self) -> str:
        return self.CPF
    
    
    def get_salario(self) -> str:
        return self.salario
    
    
    def get_codigo_cartao(self) -> str:
        return self.codigo_cartao
    
    def to_string(self) -> str:
           return f"nome: {self.get_nome()} // CPF: {self.get_CPF()} // Salario: {self.get_salario()} // Codigo do Cartão: {self.get_codigo_cartao()}"