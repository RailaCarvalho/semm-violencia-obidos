from pessoa import Pessoa

class Funcionario(Pessoa):

    def __init__(self, id, nome, cpf, identidade,tipo, login, senha):
        super().__init__(id, tipo, nome, cpf, identidade, login,senha)
        self.tipo = tipo
        self.login = login
        self.senha = senha