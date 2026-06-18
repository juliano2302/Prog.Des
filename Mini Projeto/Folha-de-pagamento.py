# Classe mãe
class Funcionario:
    def __init__(self, nome, matricula, salario_fixo):
        self.nome = nome
        self.matricula = matricula
        self.__salario_fixo = 0
        self.set_salario_fixo(salario_fixo)

    # Getter
    def get_salario_fixo(self):
        return self.__salario_fixo

    # Setter
    def set_salario_fixo(self, salario):
        if salario >= 0:
            self.__salario_fixo = salario
        else:
            print("Erro: salário não pode ser negativo.")

    def calcular_salario(self):
        pass

    def exibir(self):
        print(
            f"Nome : {self.nome} | "
            f"Matricula : {self.matricula} | "
            f"Tipo : {self.__class__.__name__} | "
            f"Salario : R$ {self.calcular_salario():.2f}"
        )

# Classe filha CLT
class CLT(Funcionario):
    def __init__(self, nome, matricula, salario_fixo):
        super().__init__(nome, matricula, salario_fixo)

    def calcular_salario(self):
        return self.get_salario_fixo()

# Classe filha Vendedor
class Vendedor(Funcionario):
    def __init__(self, nome, matricula, salario_fixo, vendas):
        super().__init__(nome, matricula, salario_fixo)
        self.vendas = vendas

    def calcular_salario(self):
        return self.get_salario_fixo() + (self.vendas * 0.10)

# Classe filha Gerente
class Gerente(Funcionario):
    BONUS = 1500

    def __init__(self, nome, matricula, salario_fixo):
        super().__init__(nome, matricula, salario_fixo)

    def calcular_salario(self):
        return self.get_salario_fixo() + self.BONUS

# Programa principal
funcionarios = [
    CLT("Samara", "001", 3000),
    Vendedor("Pedro", "002", 2000, 12000),
    Gerente("Juliano", "003", 5000)
]

for funcionario in funcionarios:
    funcionario.exibir()