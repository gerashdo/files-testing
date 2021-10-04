import unittest
from marcador import Marcador

class TestMarcador(unittest.TestCase):

    def setUp(self):
        self.marcador = Marcador()
        self.anotaciones = []

    def test_dos_unoyuno(self):
        anotaciones = [1,2,1,2]
        for anotacion in anotaciones:
            self.marcador.anotar(anotacion)
        self.assertEqual("P1 30-30 P2", self.marcador.score())
    
    def test_player1_4_seguidas_win(self):
        anotaciones = [1,1,1,1]
        for anotacion in anotaciones:
            self.marcador.anotar(anotacion)
        self.assertEqual("P1 win", self.marcador.score())

    def test_tres1_uno2_uno1(self):
        anotaciones = [1,1,1,2,1]
        for anotacion in anotaciones:
            self.marcador.anotar(anotacion)
        self.assertEqual("P1 win", self.marcador.score())

    def test_unoyuno_4veces_dos1(self):
        anotaciones = [1,2,1,2,1,2,1,2,1,1]
        for anotacion in anotaciones:
            self.marcador.anotar(anotacion)
        self.assertEqual("P1 win", self.marcador.score())

    def test_unoyuno_5veces(self):
        anotaciones = [1,2,1,2,1,2,1,2,1,2]
        for anotacion in anotaciones:
            self.marcador.anotar(anotacion)
        self.assertEqual("Tie", self.marcador.score())
    
    def test_unoyuno_5veces_uno2(self):
        anotaciones = [1,2,1,2,1,2,1,2,1,2,2]
        for anotacion in anotaciones:
            self.marcador.anotar(anotacion)
        self.assertEqual("P2 Advantage", self.marcador.score())

if __name__ == '__main__':
    unittest.main()




    
    
