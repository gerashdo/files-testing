import unittest
from figuras import Figure

class TestFigure(unittest.TestCase):

    def setUp(self):
        self.figure = Figure()

    def test_area_cuadrado_lado5(self):
        result = self.figure.square(5)
        self.assertEqual(25, result)

    def test_area_cuadrado_lado_menos1(self):
        result = self.figure.square(-1)
        self.assertEqual("Solo numeros positivos", result)
    
    def test_area_cuadrado_lado_x(self):
        result = self.figure.square("x")
        self.assertEqual("Solo numeros", result)

    def test_area_circulo_radio1(self):
        result = self.figure.circle(1)
        self.assertEqual(3.141592653589793, result)

    def test_area_circulo_radio_menos1(self):
        result = self.figure.circle(-1)
        self.assertEqual("Solo numeros positivos", result)
    
    def test_area_circulo_radio_x(self):
        result = self.figure.circle("x")
        self.assertEqual("Solo numeros", result)

    def test_area_rectangulo_1x10(self):
        result = self.figure.rectangle(1, 10)
        self.assertEqual(10, result)

    def test_area_rectangulo_menos1x5(self):
        result = self.figure.rectangle(-1, 5)
        self.assertEqual("Solo numeros positivos", result)

    def test_area_rectangulo_Xx2(self):
        result = self.figure.rectangle('x', 2)
        self.assertEqual("Solo numeros", result)

    def test_area_rectangulo_sin_parametros(self):
        result = self.figure.rectangle()
        self.assertEqual("Valores no validos", result)

    def test_area_triangulo_2x5(self):
        result = self.figure.triangle(2, 5)
        self.assertEqual(5, result)

    def test_area_triangulo_menos3xmenos10(self):
        result = self.figure.triangle(-3, -10)
        self.assertEqual("Solo numeros positivos", result)

    def test_area_triangulo_Xx5(self):
        result = self.figure.triangle("x", 5)
        self.assertEqual("Solo numeros", result)

    def test_area_triangulo_sin_parametros(self):
        result = self.figure.triangle()
        self.assertEqual("Valores no validos", result)

    def test_area_trapezoide_base5_base6_altura2(self):
        result = self.figure.trapezoid(5, 6, 2)
        self.assertEqual(11, result)

    def test_area_trapezoide_basemeso3_basemenos10_altura1(self):
        result = self.figure.trapezoid(-3, -10, 1)
        self.assertEqual("Valores no validos", result)

    def test_area_trapezoide_base0_base15_altura4(self):
        result = self.figure.trapezoid(0, 15, 4)
        self.assertEqual("Valores no validos", result)

    def test_area_trapezoide_basex_base5_alturax(self):
        result = self.figure.trapezoid('x', 5, 'x')
        self.assertEqual("Solo numeros", result)

    def test_area_trapezoide_sin_parametros(self):
        result = self.figure.trapezoid()
        self.assertEqual("Valores no validos", result)

if __name__ == '__main__':
    unittest.main(verbosity=2)