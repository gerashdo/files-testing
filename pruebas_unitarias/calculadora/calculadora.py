
class Calculadora:
    def suma(self, num1, num2):

        if isinstance(num1, str) or isinstance(num1, str):
            return 'Solo numeros'
        elif isinstance(num1, float) or isinstance(num2, float):
            return 'Solo numeros enteros'
        else:
            if num1 < 0 or num2 < 0:
                return 'Solo numeros positivos'
            else:
                return num1 + num2

    def resta(self, num1, num2):
        if isinstance(num1, str) or isinstance(num1, str):
            return 'Solo numeros'
        elif isinstance(num1, float) or isinstance(num2, float):
            return 'Solo numeros enteros'
        else:
            if num1 < 0 or num2 < 0:
                return 'Solo numeros positivos'
            else:
                return num1 - num2

    def multiplica(self, num1, num2):
        if isinstance(num1, str) or isinstance(num1, str):
            return 'Solo numeros'
        elif isinstance(num1, float) or isinstance(num2, float):
            return 'Solo numeros enteros'
        else:
            return num1 * num2

    def divide(self, num1, num2):
        if isinstance(num1, str) or isinstance(num1, str):
            return 'Solo numeros'
        elif isinstance(num1, float) or isinstance(num2, float):
            return 'Solo numeros enteros'
        elif num2 == 0:
            return 'Indefinido'
        else:
            res = num1 / num2
            if res - int(res) == 0:
                return int(res)
            else:
                return res

    def potencia(self, num1, num2):
        if isinstance(num1, str) or isinstance(num1, str):
            return 'Solo numeros'
        elif num1 == 0 and num2 == 0:
            return 'Indefinido'
        elif num1 == 0:
            return 0
        elif num2 == 0:
            return 1
        else:
            return pow(num1, num2)
