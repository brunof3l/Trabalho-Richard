class Funcionario:
    proximo_id = 1

    def __init__(self, nome, cpf, salario_base, tipo):
        self.__id = Funcionario.proximo_id
        Funcionario.proximo_id += 1
        self.__nome = nome
        self.__cpf = cpf
        self.__salario_base = salario_base
        self.__tipo = tipo
        self.__validar()

    def __validar(self):
        if self.__cpf == "":
            print("CPF não pode ser vazio.")
            self.__cpf = "Não informado"
        if self.__salario_base < 0:
            print("Salário não pode ser negativo.")
            self.__salario_base = 0

    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_cpf(self): return self.__cpf
    def get_salario_base(self): return self.__salario_base
    def get_tipo(self): return self.__tipo

    def set_nome(self, valor): self.__nome = valor
    def set_cpf(self, valor):
        if valor != "": self.__cpf = valor
    def set_salario_base(self, valor):
        if valor >= 0: self.__salario_base = valor
    def set_tipo(self, valor): self.__tipo = valor

    def exibir_dados(self):
        print(f"ID: {self.get_id()}")
        print(f"Tipo: {self.get_tipo()}")
        print(f"Nome: {self.get_nome()}")
        print(f"CPF: {self.get_cpf()}")
        print(f"Salário Base: R$ {self.get_salario_base():.2f}")

    def calcular_salario(self):
        return self.get_salario_base()
