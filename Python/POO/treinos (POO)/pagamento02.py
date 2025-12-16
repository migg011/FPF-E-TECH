class Pagamento:
    def __init__(self, valor):
        self.valor = valor

    def calcular_valor(self):
        return self.valor

class PagamentoPix(Pagamento):
    def __init__(self, valor):
        super().__init__(valor)
        self.desconto = 10

    def calcular_valor(self):
        return self.valor - (self.valor * (self.desconto / 100))

produto01 = PagamentoPix(200)
resultado = produto01.calcular_valor()
print(resultado)
