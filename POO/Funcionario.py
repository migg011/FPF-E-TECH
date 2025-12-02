class Funcionario:

    def __init__(self, nome_dado, cargo_dado):
        self.nome = nome_dado
        self.cargo = cargo_dado

funcionario_1 = Funcionario("Miguel", "Atendente de caixa")
print("nome: ", funcionario_1.nome)
print("cargo: ", funcionario_1.cargo)