from django.test import TestCase
from django.db import IntegrityError
from django.core.exceptions import ValidationError
from articulos.models import Categoria

class TestCategoriaModel(TestCase):
    # def test_smoke(self):
    #     self.assertEqual(2, 1+1)

    def test_insercion_categoria(self):
        Categoria.objects.create(nombre='Categoria 1')
        categoria = Categoria.objects.get(id=1)
        self.assertEqual(categoria.nombre, 'Categoria 1')

    # def test_name_should_not_be_empty(self):
    #     Categoria.objects.create(nombre='')
    #     categoria = Categoria.objects.get(id=1)
    #     self.assertEqual(categoria.nombre, 'Categoria 1')

    def test_name_should_not_be_empty(self):
        with self.assertRaises(IntegrityError):
            Categoria.objects.create(nombre=None)

    def test_name_should_be_less_than_fifty_length(self):
        categoria = Categoria.objects.create(nombre='hdhdhdhdhdhdhdhdhdhdhdhdhdhdhdhdhdhdhhdhdhdhdhdhdhdhdhdhdhdhdhdhdhdh')
        
        with self.assertRaises(ValidationError):
            categoria.full_clean()

