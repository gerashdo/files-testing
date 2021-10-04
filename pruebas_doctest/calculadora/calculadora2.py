

class Calculadora:

    def suma(self, num1, num2):
        if isinstance(num1, float) or isinstance(num2, float):
            return 'Solo numeros enteros'
        else:
            if not positivo(num1) or not positivo(num2):
                return 'Solo numeros positivos'
            else:
                return num1 + num2

    def positivo(self, val):
        if val < 0:
            return False
        else:
            return True


    # def positivo(self, val):
    #     if val < 0:
    #         return False
    #     else:
    #         return True

# if __name__=="__main__":
#     import doctest
#     doctest.testfile()