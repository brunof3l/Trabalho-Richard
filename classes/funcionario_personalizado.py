from classes.funcionario import Funcionario


class FuncionarioPersonalizado(Funcionario):
    def __init__(self, nome, cpf, tipo, salario_base, bonus):
        super().__init__(nome, cpf, salario_base, tipo)
        self.__bonus = bonus

    def calcular_salario(self):
        salario = self.get_salario_base() + self.__bonus
        if salario < 0:
            salario = 0
        return salario

    def exibir_dados(self):
        super().exibir_dados()
        print(f"Vale Alimentação: R$ {self.__bonus:.2f}")
