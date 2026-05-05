from classes.funcionario import Funcionario


class Freelancer(Funcionario):
    def __init__(self, nome, cpf, valor_projeto, qtd_projetos):
        super().__init__(nome, cpf, 0, "Freelancer")
        self.__valor_projeto = valor_projeto
        self.__qtd_projetos = qtd_projetos

    def calcular_salario(self):
        return self.__valor_projeto * self.__qtd_projetos

    def exibir_dados(self):
        super().exibir_dados()
        print(f"Valor do Projeto: R$ {self.__valor_projeto:.2f}")
        print(f"Quantidade de Projetos: {self.__qtd_projetos}")
