import unittest
from edades import Edad

class testEdades(unittest.TestCase):

    def setUp(self):
        self.edad = Edad()

    def test_calcular_edad_de_menos2(self):
        result =  self.edad.calcularEdad(-2)
        self.assertEqual("No existes", result)

    def test_calcular_edad_de_0(self):
        result =  self.edad.calcularEdad(0)
        self.assertEqual("Eres niño", result)

    def test_calcular_edad_de_13(self):
        result =  self.edad.calcularEdad(13)
        self.assertEqual("Eres niño", result)

    def test_calcular_edad_de_14(self):
        result =  self.edad.calcularEdad(14)
        self.assertEqual("Eres adolescente", result)

    def test_calcular_edad_de_17(self):
        result =  self.edad.calcularEdad(17)
        self.assertEqual("Eres adolescente", result)

    def test_calcular_edad_de_18(self):
        result =  self.edad.calcularEdad(18)
        self.assertEqual("Eres adulto", result)
    
    def test_calcular_edad_de_65(self):
        result =  self.edad.calcularEdad(65)
        self.assertEqual("Eres adulto", result)

    def test_calcular_edad_de_66(self):
        result =  self.edad.calcularEdad(66)
        self.assertEqual("Eres adulto mayor", result)

    def test_calcular_edad_de_90(self):
        result =  self.edad.calcularEdad(90)
        self.assertEqual("Eres adulto mayor", result)

    def test_calcular_edad_de_X(self):
        result =  self.edad.calcularEdad('X')
        self.assertEqual("Solo numeros", result)

    def test_calcular_edad_vacia(self):
        result =  self.edad.calcularEdad()
        self.assertEqual("No existes", result)

if __name__ == '__main__':
    unittest.main(verbosity=2)
    
