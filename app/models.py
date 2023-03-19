from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Usuario(AbstractUser):
    pass

class Mensagem(models.Model):
    name = models.CharField(max_length=128)
    mensagem = models.CharField(max_length=1024)

