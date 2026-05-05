class funcionario:
    def __init__(self, nome, cpf, salario_base):
        self.nome = nome
        self.cpf = cpf
        self.salario_base = salario_base
        
    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"CPF: {self.cpf}")
        print(f"Salário Base: R${self.salario_base}")
        
    def calcular_salario(self):
        return self.salario_base