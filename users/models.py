from django.db import models

class User(models.Model):
    username = models.CharField(max_length=200, verbose_name="nombre de usuario")
    email = models.EmailField(verbose_name="email")
    password = models.CharField(max_length=200, verbose_name="contraseña")
    