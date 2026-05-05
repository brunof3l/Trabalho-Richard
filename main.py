class Funcionario:
    def __init__(self, nome, cpf, salario_base):
        # Inicializando com os setters para já aplicar as validações
        self.__nome = nome
        self.set_cpf(cpf)
        self.set_salario_base(salario_base)

    # Getters
    def get_nome(self):
        return self.__nome

    def get_cpf(self):
        return self.__cpf

    def get_salario_base(self):
        return self.__salario_base

    # Setters com validações
    def set_nome(self, nome):
        self.__nome = nome

    def set_cpf(self, cpf):
        if not cpf or cpf.strip() == "":
            raise ValueError("O CPF não pode ser vazio.")
        self.__cpf = cpf

    def set_salario_base(self, salario_base):
        if salario_base < 0:
            raise ValueError("O salário não pode ser negativo.")
        self.__salario_base = salario_base

    def exibir_dados(self):
        print(f"Nome: {self.__nome} | CPF: {self.__cpf} | Salário Base: R${self.__salario_base:.2f}")

    def calcular_salario(self):
        return self.__salario_base


class FuncionarioCLT(Funcionario):
    def __init__(self, nome, cpf, salario_base, bonus):
        super().__init__(nome, cpf, salario_base)
        self.__bonus = bonus

    def calcular_salario(self):
        # Salário = salário base + bônus
        return self.get_salario_base() + self.__bonus

    def exibir_dados(self):
        super().exibir_dados()
        print(f"Tipo: CLT | Bônus: R${self.__bonus:.2f} | Salário Final: R${self.calcular_salario():.2f}")
        print("-" * 30)


class Freelancer(Funcionario):
    def __init__(self, nome, cpf, valor_por_projeto, quantidade_projetos):
        # Freelancer não tem salário base fixo, enviamos 0 para a classe mãe
        super().__init__(nome, cpf, 0) 
        self.__valor_por_projeto = valor_por_projeto
        self.__quantidade_projetos = quantidade_projetos

    def calcular_salario(self):
        # Salário = valor_por_projeto * quantidade_projetos
        return self.__valor_por_projeto * self.__quantidade_projetos

    def exibir_dados(self):
        super().exibir_dados()
        print(f"Tipo: Freelancer | Projetos: {self.__quantidade_projetos} | Salário Final: R${self.calcular_salario():.2f}")
        print("-" * 30)


class Estagiario(Funcionario):
    def __init__(self, nome, cpf, bolsa, desconto):
        super().__init__(nome, cpf, bolsa)
        self.__desconto = desconto

    def calcular_salario(self):
        # Salário = bolsa - desconto
        return self.get_salario_base() - self.__desconto

    def exibir_dados(self):
        super().exibir_dados()
        print(f"Tipo: Estagiário | Desconto: R${self.__desconto:.2f} | Salário Final: R${self.calcular_salario():.2f}")
        print("-" * 30)


# --- INÍCIO DO SISTEMA E MENU INTERATIVO ---

def inicializar_funcionarios():
    """Gera 5 funcionários de cada tipo conforme exigido"""
    lista = []
    
    # 5 CLTs
    for i in range(1, 6):
        lista.append(FuncionarioCLT(f"CLT {i}", f"111.111.111-0{i}", 3000, 500))
        
    # 5 Freelancers
    for i in range(1, 6):
        lista.append(Freelancer(f"Freela {i}", f"222.222.222-0{i}", 1500, 2))
        
    # 5 Estagiários
    for i in range(1, 6):
        lista.append(Estagiario(f"Estagiário {i}", f"333.333.333-0{i}", 1200, 150))
        
    return lista

def main():
    empresa = inicializar_funcionarios()
    
    while True:
        print("\n=== SISTEMA DE GERENCIAMENTO DE FUNCIONÁRIOS ===")
        print("1. Listar todos os funcionários (e seus salários)")
        print("2. Cadastrar novo funcionário")
        print("3. Remover funcionário (por CPF)")
        print("4. Calcular folha total da empresa")
        print("5. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            print("\n--- LISTA DE FUNCIONÁRIOS ---")
            if not empresa:
                print("Nenhum funcionário cadastrado.")
            for func in empresa:
                func.exibir_dados()
                
        elif opcao == '2':
            print("\nQual tipo de funcionário deseja cadastrar?")
            print("1 - CLT | 2 - Freelancer | 3 - Estagiário")
            tipo = input("Opção: ")
            
            nome = input("Nome: ")
            cpf = input("CPF: ")
            
            try:
                if tipo == '1':
                    base = float(input("Salário Base: R$ "))
                    bonus = float(input("Bônus: R$ "))
                    empresa.append(FuncionarioCLT(nome, cpf, base, bonus))
                elif tipo == '2':
                    valor_proj = float(input("Valor por Projeto: R$ "))
                    qtd_proj = int(input("Quantidade de Projetos: "))
                    empresa.append(Freelancer(nome, cpf, valor_proj, qtd_proj))
                elif tipo == '3':
                    bolsa = float(input("Bolsa Auxílio: R$ "))
                    desc = float(input("Desconto (ex: VT): R$ "))
                    empresa.append(Estagiario(nome, cpf, bolsa, desc))
                else:
                    print("Tipo inválido!")
                print("Funcionário cadastrado com sucesso!")
            except ValueError as e:
                print(f"Erro ao cadastrar: {e} (Verifique os dados digitados)")
                
        elif opcao == '3':
            cpf_remover = input("Digite o CPF do funcionário a remover: ")
            tamanho_original = len(empresa)
            empresa = [f for f in empresa if f.get_cpf() != cpf_remover]
            if len(empresa) < tamanho_original:
                print("Funcionário removido com sucesso!")
            else:
                print("CPF não encontrado.")
                
        elif opcao == '4':
            total = sum(f.calcular_salario() for f in empresa)
            print(f"\n--- FOLHA DE PAGAMENTO TOTAL: R${total:.2f} ---")
            
        elif opcao == '5':
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()