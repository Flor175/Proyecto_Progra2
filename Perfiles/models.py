from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Perfil(models.Model):
    MATEMATICA = "Matemática"
    FISICA = "Física"
    Carreras = {
        (MATEMATICA, "Matemática"),
        (FISICA, "Física")
    }
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    email_confirmed = models.BooleanField(default=False)
    numero_carnet = models.CharField(max_length=9, blank=True, null=True, unique=True)
    cui = models.CharField(max_length=13,blank=True, null=True, unique=True)
    profesion = models.CharField(max_length=100, choices=Carreras, default=MATEMATICA)

    def __str__(self): 
        return self.usuario.username

@receiver(post_save, sender=User)
def crear_usuario(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(usuario=instance)

@receiver(post_save, sender=User)
def guardar_usuario(sender, instance, **kwargs):
    instance.perfil.save()