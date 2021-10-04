import math

class Figure:

    def square(self, side):
        if isinstance(side,str):
            return 'Solo numeros'
        else:
            if side < 0:
                return 'Solo numeros positivos'
            else:
                return side * side

    def circle(self, radius):
        if isinstance(radius, str):
            return 'Solo numeros'
        else:
            if radius < 0:
                return 'Solo numeros positivos'
            else:
                return math.pi * (pow(radius, 2))

    def rectangle(self, length = 0, width = 0):
        if isinstance(length, str) or isinstance(width, str):
            return 'Solo numeros'
        elif length == 0 and width == 0 :
            return 'Valores no validos'
        else:
            if length < 0 or width < 0:
                return 'Solo numeros positivos'
            else:
                return length * width

    def triangle(self, height = 0, width = 0):
        if isinstance(height, str) or isinstance(width, str):
            return 'Solo numeros'
        elif height == 0 and width == 0 :
            return 'Valores no validos'
        else:
            if height < 0 or width < 0:
                return 'Solo numeros positivos'
            else:
                result = (height * width) / 2
                if result - int(result) == 0:
                    return int(result)
                else:
                    return result

    def trapezoid(self, base1 = 0, base2 = 0, height = 0,):
        if isinstance(height, str) or isinstance(base1, str) or isinstance(base2, str):
            return 'Solo numeros'
        elif height <= 0 or base1 <= 0 or base2 <= 0:
            return 'Valores no validos'
        else:
            result = ((base1 + base2) / 2) * height
            if result - int(result) == 0:
                return int(result)
            else:
                return result