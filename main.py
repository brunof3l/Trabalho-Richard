import random

nomes_base = ["Ana", "Bruno", "Carla", "Diego", "Elena", "Fabio", "Gisele", "Hugo", "Iara", "Junior"]
sobrenomes = ["Silva", "Santos", "Oliveira", "Souza", "Pereira", "Lima", "Ferreira", "Costa"]

class Funcionario:
    proximo_id = 1

    def __init__(self, nome, cpf, salario_base):
        self.__id = Funcionario.proximo_id
        Funcionario.proximo_id += 1
        self.__nome = nome
        self.__cpf = cpf
        self.__salario_base = salario_base
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

    def set_nome(self, valor): self.__nome = valor
    def set_cpf(self, valor):
        if valor != "": self.__cpf = valor
    def set_salario_base(self, valor):
        if valor >= 0: self.__salario_base = valor

    def exibir_dados(self):
        print(f"ID: {self.get_id()}\nNome: {self.get_nome()}\nCPF: {self.get_cpf()}\nBase: R$ {self.get_salario_base():.2f}")

    def calcular_salario(self):
        return self.get_salario_base()


class FuncionarioCLT(Funcionario):
    def __init__(self, nome, cpf, salario_base, bonus):
        super().__init__(nome, cpf, salario_base)
        self.__bonus = bonus

    def calcular_salario(self):
        return self.get_salario_base() + self.__bonus

    def exibir_dados(self):
        super().exibir_dados()
        print(f"Tipo: CLT\nBônus: R$ {self.__bonus:.2f}")

class Freelancer(Funcionario):
    def __init__(self, nome, cpf, valor_projeto, qtd_projetos):
        super().__init__(nome, cpf, 0)
        self.__valor_projeto = valor_projeto
        self.__qtd_projetos = qtd_projetos

    def calcular_salario(self):
        return self.__valor_projeto * self.__qtd_projetos

    def exibir_dados(self):
        super().exibir_dados()
        print(f"Tipo: Freelancer\nValor do Projeto: R$ {self.__valor_projeto:.2f}\nQtd de Projetos: {self.__qtd_projetos}")

class Estagiario(Funcionario):
    def __init__(self, nome, cpf, salario_base, desconto):
        super().__init__(nome, cpf, salario_base)
        self.__desconto = desconto

    def calcular_salario(self):
        return self.get_salario_base() - self.__desconto

    def exibir_dados(self):
        super().exibir_dados()
        print(f"Tipo: Estagiário\nDesconto: R$ {self.__desconto:.2f}")

def gerar_nome_aleatorio():
    return f"{random.choice(nomes_base)} {random.choice(sobrenomes)}"

funcionarios = []
def funcionarios_iniciais():
    for i in range(1, 6):
        nome_clt = gerar_nome_aleatorio()
        funcionarios.append(FuncionarioCLT(nome_clt, f"111.111.111-{i:02d}", 3000, 500))
    for i in range(6, 11):
        nome_freelancer = gerar_nome_aleatorio()
        funcionarios.append(Freelancer(nome_freelancer, f"222.222.222-{i:02d}", 200, random.randint(1, 5)))
    for i in range(11, 16):
        nome_estagiario = gerar_nome_aleatorio()
        funcionarios.append(Estagiario(nome_estagiario, f"333.333.333-{i:02d}", 1200, 50))

def cadastrar():
    print("=" * 30)
    print("\t--- Cadastrar ---")    
    print("=" * 30)
    tipo = input("1-CLT | 2-Freelancer | 3-Estagiário: ")
    nome = input("Digite o Nome: ").title()
    cpf = input("Digite o CPF: ")

    if tipo == "1":
        salario_base = float(input("Salário Base: "))
        bonus = float(input("Bônus: "))
        funcionarios.append(FuncionarioCLT(nome, cpf, salario_base, bonus))
    elif tipo == "2":
        valor_projeto = float(input("Valor por Projeto: "))
        qtd_projetos = int(input("Qtd de Projetos: "))
        funcionarios.append(Freelancer(nome, cpf, valor_projeto, qtd_projetos))
    elif tipo == "3":
        salario_base = float(input("Salário Base: "))
        desconto = float(input("Desconto: "))
        funcionarios.append(Estagiario(nome, cpf, salario_base, desconto))
    else:
        print("Opção inválida.")
        return
    print("Cadastrado com sucesso!")
    print("=" * 30)

def listar():
    print("=" * 30)
    print("--- Lista de Funcionários ---")
    print("=" * 30)
    if len(funcionarios) == 0:
        print("Nenhum funcionário cadastrado.")
        return
    for f in funcionarios:
        f.exibir_dados()
        print("=" * 30)

def calcular_salarios():
    print("=" * 30)
    print("\t--- Salários Finais ---")
    print("=" * 30)
    for f in funcionarios:
        print(f"{f.get_nome()}: R$ {f.calcular_salario():.2f}")
    print("=" * 30)

def calcular_folha():
    total = 0
    for f in funcionarios:
        total += f.calcular_salario()
    print(f"\nFOLHA TOTAL DA EMPRESA: R$ {total:.2f}")
    print("=" * 30)

def remover():
    listar()
    if len(funcionarios) == 0:
        return
    try:
        remover = int(input("\nDigite o ID do funcionário para remover: "))
    except ValueError:
        print("Digite um número válido para o ID.")
        return

    for f in funcionarios:
        if f.get_id() == remover:
            funcionarios.remove(f)
            print(f"{f.get_nome()} removido com sucesso!")
            print("=" * 30)
            return

    print("ID inválido.")

def main():
    funcionarios_iniciais()
    while True:
        print("=" * 30)
        print("\t--- Menu ---")
        print("=" * 30)
        print("\n1-Cadastrar\n2-Listar\n3-Calcular Salários\n4-Folha Total\n5-Remover\n0-Sair")
        op = input("\nEscolha uma opção: ")
        
        if op == "1":
            cadastrar()
        elif op == "2":
            listar()
        elif op == "3":
            calcular_salarios()
        elif op == "4":
            calcular_folha()
        elif op == "5":
            remover()
        elif op == "0":
            print("\nSaindo do Sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
