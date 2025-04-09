class Pessoa():

    def __init__(self, id, nome, cpf, dataNascimento):
        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.dataNascimento = dataNascimento

    def apresentar(self):
        print(f"Meu nome é : {self.nome}")