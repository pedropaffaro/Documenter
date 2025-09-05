class Calculadora:
    def somar(self, a, b):
        return a + b

    def subtrair(self, a, b):
        return a - b

def saudacao(nome):
    return f"Olá, {nome}!"

def fatorial(n):
    if n == 0:
        return 1
    return n * fatorial(n - 1)

if __name__ == "__main__":
    def saudacao_2(nome):
        return f"Olá, {nome}!"

    calc = Calculadora()
    print(calc.somar(2, 3))
    print(saudacao("Pedro"))
    print(fatorial(5))

