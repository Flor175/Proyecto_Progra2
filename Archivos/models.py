from django.db import models
from Archivos.validators import validate_file_extension, validar_expresion
from django.contrib.auth.models import User
from django.conf import settings
from Perfiles.models import Perfil
import os
# Create your models here.

user = Perfil.usuario

def user_directory_path(instance, filename):
    return 'Documentos/{0}/{1}'.format(instance.user.usuario.username, filename) 

class Documento(models.Model):
    user = models.ForeignKey(Perfil, on_delete=models.CASCADE, null=True)
    archivo = models.FileField(upload_to=user_directory_path, validators=[validate_file_extension])

    def filename(self):
        return os.path.basename(self.archivo.name)

class Expresion(models.Model):
    expresion = models.TextField(validators=[validar_expresion], default=False)