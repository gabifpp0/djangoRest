from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    PERFIL = (
        ('admin', 'Administrador'),
        ('professor', 'Professor'),
        ('aluno', 'Aluno'),
        ('coordenador', 'Coordenador'),
        ('diretor', 'Diretor')
    )

    perfil = models.CharField(max_length=15, choices=PERFIL)

class Aluno(models.Model):
    matricula = models.CharField(max_length=10, unique=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True, related_name='aluno')

class Professor(models.Model):    
    matricula = models.CharField(max_length=10, unique=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True, related_name='professor')