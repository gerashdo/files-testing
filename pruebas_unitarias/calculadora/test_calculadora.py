import unittest
from calculadora import Calculadora


class TestCalculadora(unittest.TestCase):

    def setUp(self):
        self.calc = Calculadora()

    def test_sumar_dos_mas_dos(self):
        result = self.calc.suma(2, 2)
        self.assertEqual(
            4, result, "2 + 2 = 4 El resultado no fue lo esperado")

    def test_sumar_0_mas_1(self):
        result = self.calc.suma(0, 1)
        self.assertEqual(1, result)

    def test_sumar_cinco_mas_veinte(self):
        result = self.calc.suma(5, 20)
        self.assertEqual(
            25, result, "5 + 20 = 25 El resultado no fue lo esperado")

    def test_solo_positivos(self):
        result = self.calc.suma(4, -1)
        self.assertEqual("Solo numeros positivos", result,
                         "El resultado no fue lo esperado")

    def test_sumar_4punto5_mas_menos1(self):
        result = self.calc.suma(4.5, -1)
        self.assertEqual("Solo numeros enteros", result)

    def test_sumar_x_mas_5(self):
        result = self.calc.suma('x', 5)
        self.assertEqual("Solo numeros", result)

    def test_restar_cero_menos_0(self):
        result = self.calc.resta(0, 0)
        self.assertEqual(0, result)

    def test_restar_0_menos_1(self):
        result = self.calc.resta(0, 1)
        self.assertEqual(-1, result)

    def test_restar_15_menos_menos3(self):
        result = self.calc.resta(15, -1)
        self.assertEqual("Solo numeros positivos", result)

    def test_restar_4punto5_menos_menos1(self):
        result = self.calc.resta(4.5, -1)
        self.assertEqual("Solo numeros enteros", result)

    def test_restar_x_menos_menos1(self):
        result = self.calc.resta('x', -1)
        self.assertEqual("Solo numeros", result)

    def test_multiplicar_0_por_0(self):
        result = self.calc.multiplica(0, 0)
        self.assertEqual(0, result)

    def test_multiplicar_0_por_1(self):
        result = self.calc.multiplica(0, 1)
        self.assertEqual(0, result)

    def test_multiplicar_6_por_9(self):
        result = self.calc.multiplica(6, 9)
        self.assertEqual(54, result)

    def test_multiplicar_10_por_menos3(self):
        result = self.calc.multiplica(10, -3)
        self.assertEqual(-30, result)

    def test_multiplicar_menos10_por_menos3(self):
        result = self.calc.multiplica(-10, -3)
        self.assertEqual(30, result)

    def test_multiplicar_4punto5_por_menos1(self):
        result = self.calc.multiplica(4.5, -1)
        self.assertEqual("Solo numeros enteros", result)

    def test_multiplicar_x_por_menos1(self):
        result = self.calc.multiplica('x', -1)
        self.assertEqual("Solo numeros", result)

    def test_dividir_0_entre_0(self):
        result = self.calc.divide(0, 0)
        self.assertEqual("Indefinido", result)

    def test_dividir_0_entre_1(self):
        result = self.calc.divide(0, 1)
        self.assertEqual(0, result)

    def test_dividir_1_entre_0(self):
        result = self.calc.divide(1, 0)
        self.assertEqual("Indefinido", result)

    def test_dividir_4_entre_5(self):
        result = self.calc.divide(4, 5)
        self.assertEqual(0.8, result)

    def test_dividir_10_entre_5(self):
        result = self.calc.divide(10, 5)
        self.assertEqual(2, result)

    def test_dividir_menos30_entre_menos3(self):
        result = self.calc.divide(-30, -3)
        self.assertEqual(10, result)

    def test_dividir_menos30_entre_3(self):
        result = self.calc.divide(-30, 3)
        self.assertEqual(-10, result)

    def test_dividir_5punto5_entre_menos1(self):
        result = self.calc.divide(5.5, -1)
        self.assertEqual("Solo numeros enteros", result)

    def test_dividir_x_entre_menos1(self):
        result = self.calc.divide('x', -3)
        self.assertEqual("Solo numeros", result)

    def test_elevar_0_al_0(self):
        result = self.calc.potencia(0, 0)
        self.assertEqual("Indefinido", result)

    def test_elevar_0_al_5(self):
        result = self.calc.potencia(0, 5)
        self.assertEqual(0, result)

    def test_elevar_11_al_0(self):
        result = self.calc.potencia(11, 0)
        self.assertEqual(1, result)

    def test_elevar_10_al_2(self):
        result = self.calc.potencia(10, 2)
        self.assertEqual(100, result)

    def test_elevar_2_al_menos2(self):
        result = self.calc.potencia(2, -2)
        self.assertEqual(0.25, result)

    def test_elevar_menos2_al_menos2(self):
        result = self.calc.potencia(-2, -2)
        self.assertEqual(0.25, result)

    def test_elevar_menos2_al_2(self):
        result = self.calc.potencia(-2, 2)
        self.assertEqual(4, result)

    def test_elevar_2punto5_al_2(self):
        result = self.calc.potencia(2.5, 2)
        self.assertEqual(6.25, result)

    def test_elevar_x_al_menos3(self):
        result = self.calc.potencia('x', -3)
        self.assertEqual("Solo numeros", result)


if __name__ == '__main__':
    unittest.main()
