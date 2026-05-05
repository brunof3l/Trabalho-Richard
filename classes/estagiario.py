from classes.funcionario import Funcionario


class Estagiario(Funcionario):
    def __init__(self, nome, cpf, salario_base, desconto):
        super().__init__(nome, cpf, salario_base, "Estagiário")
        self.__desconto = desconto

    def calcular_salario(self):
        return self.get_salario_base() - self.__desconto

    def exibir_dados(self):
        super().exibir_dados()
        print(f"Desconto Vale Transporte: R$ {self.__desconto:.2f}")
