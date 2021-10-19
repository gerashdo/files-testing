from django.db import models

class Articulo(models.Model):

    nombre = models.CharField(max_length=50)
    descripcion = models.TextField('Descripción')
    categoria = models.ForeignKey('articulos.Categoria', verbose_name='Categoria', on_delete=models.CASCADE)
    foto = models.ImageField('Imagen', upload_to='fotos')

    def __str__(self):
        return self.nombre


class Categoria(models.Model):
    
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
