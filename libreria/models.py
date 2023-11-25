from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, max_length=100)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'password']

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    biografia = models.CharField(max_length=100)
    nacimiento = models.DateField(unique=True)
    nacionalidad = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre    

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    fecha_publicacion = models.DateField()
    categoria = models.CharField(max_length=200)
    autor= models.ForeignKey(Autor, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

class Editorial(models.Model):
    nombre = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)

    def __str__(self):
        return self.nombre

class LibroEditorial(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE)

    def __str__(self):
        return self.libro.titulo + ' - ' + self.editorial.nombre

class Prestamo(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    fecha_prestamo = models.DateField()
    fecha_devolucion = models.DateField()
    devuelto = models.BooleanField(default=False)

    def __str__(self):
        return self.libro.titulo + ' - ' + self.usuario.username

class Devolucion(models.Model):
    prestamo = models.ForeignKey(Prestamo, on_delete=models.CASCADE)
    fecha_devolucion = models.DateField()

    def __str__(self):
        return self.prestamo.libro.titulo + ' - ' + self.prestamo.usuario.username

class Reserva(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    fecha_reserva = models.DateField()
    fecha_expiracion = models.DateField()
    expirado = models.BooleanField(default=False)

    def __str__(self):
        return self.libro.titulo + ' - ' + self.usuario.username




