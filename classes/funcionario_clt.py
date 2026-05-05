from classes.funcionario import Funcionario


class FuncionarioCLT(Funcionario):
    def __init__(self, nome, cpf, salario_base, bonus):
        super().__init__(nome, cpf, salario_base, "CLT")
        self.__bonus = bonus

    def calcular_salario(self):
        return self.get_salario_base() + self.__bonus

    def exibir_dados(self):
        super().exibir_dados()
        print(f"Vale Alimentação: R$ {self.__bonus:.2f}")
