from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    #Creamos un campo OneToOneField llamado user que establece una relación uno a uno con el modelo User de Django. 
    #Esto significa que cada instancia de User estará asociada a una instancia de Profile.
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    edad = models.IntegerField()

    def __str__(self):
        return self.user.username
