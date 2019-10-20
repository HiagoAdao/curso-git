class Calculadora:
    """Classe para representar uma calculadora"""

    def __init__(self):
        self.result = "O resultado da {operacao} entre os elemento(s) ({elemento1}, {elemento2}) foi: {resultado}"

    def somar(self, elemento1: int, elemento2: int):
        """Função responsável por somar dois elementos
        :param elemento1 (int)
        :param elemento2 (int)"""
        resultado = elemento1 + elemento2

        return self.result.format(
            operacao="soma", elemento1=elemento1,
            elemento2=elemento2, resultado=resultado)

    def subtrair(self, elemento1: int, elemento2: int):
        """Função responsável por subtrair dois elementos
        :param elemento1 (int)
        :param elemento2 (int)"""
        resultado = elemento1 - elemento2
        return self.result.format(
            operacao="subtração", elemento1=elemento1,
            elemento2=elemento2, resultado=resultado)

    def multiplicar(self, elemento1: int, elemento2: int):
        """Função responsável por multiplicar dois elementos
        :param elemento1 (int)
        :param elemento2 (int)"""
        resultado = elemento1 * elemento2
        return self.result.format(
            operacao="multiplicação", elemento1=elemento1,
            elemento2=elemento2, resultado=resultado)

    def elevar_ao_quadrado(self, elemento1: int):
        """Função responsável por elevar ao quadrado dois elementos
        :param elemento1 (int)
        :param elemento2 (int)"""
        resultado = elemento1 * elemento1
        return self.result.format(
            operacao="elevação ao quadrado", elemento1=elemento1,
            elemento2=elemento1, resultado=resultado)

    def dividir(self, elemento1: int, elemento2: int):
        """Função responsável por dividir dois elementos
        :param elemento1 (int)
        :param elemento2 (int)"""
        if elemento2 == 0 or elemento1 == 0:
            return self.result.format(
                operacao="divisão", elemento1=elemento1,
                elemento2=elemento2, resultado=0)

        resultado = elemento1 / elemento2
        return self.result.format(
            operacao="divisão", elemento1=elemento1,
            elemento2=elemento2, resultado=resultado)

    def porcentagem(self, elemento1: int, elemento2: int):
        """Função responsável por calcular elemento1
        porcentagem entre dois elementos
        :param elemento1 (int)
        :param elemento2 (int)"""
        calculo = (elemento2 * 100) / elemento1
        resultado = f"{calculo}%"
        return self.result.format(
            operacao="divisão", elemento1=elemento1,
            elemento2=None, resultado=resultado)
