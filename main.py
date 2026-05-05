import random
from classes.estagiario import Estagiario
from classes.freelancer import Freelancer
from classes.funcionario_clt import FuncionarioCLT
from classes.funcionario_personalizado import FuncionarioPersonalizado

nomes_base = ["Ana", "Bruno", "Carla", "Diego", "Elena", "Fabio", "Gisele", "Hugo", "Iara", "Junior"]
sobrenomes = ["Silva", "Santos", "Oliveira", "Souza", "Pereira", "Lima", "Ferreira", "Costa"]

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
    tipo = input("1-CLT\n2-Freelancer\n3-Estagiário\n4-Outro tipo:\nDigite a opção: ")
    nome = input("Digite o Nome do Funcionário: ").title()
    cpf = input("Digite o CPF do Funcionário: ")

    if tipo == "1":
        salario_base = float(input("Salário Base: "))
        bonus = float(input("Bônus: "))
        funcionarios.append(FuncionarioCLT(nome, cpf, salario_base, bonus))
    elif tipo == "2":
        valor_projeto = float(input("Valor por Projeto: "))
        qtd_projetos = int(input("Quantidade de Projetos: "))
        funcionarios.append(Freelancer(nome, cpf, valor_projeto, qtd_projetos))
    elif tipo == "3":
        salario_base = float(input("Salário Base: "))
        desconto = float(input("Desconto: "))
        funcionarios.append(Estagiario(nome, cpf, salario_base, desconto))
    elif tipo == "4":
        função = input("Digite a função do funcionário: ").title()
        salario_base = float(input("Salário Base: "))
        bonus = float(input("Bonus: "))
        funcionarios.append(
            FuncionarioPersonalizado(
                nome,
                cpf,
                função,
                salario_base,
                bonus
            )
        )
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
        print(f"{f.get_nome()} ({f.get_tipo()}): R$ {f.calcular_salario():.2f}")
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
