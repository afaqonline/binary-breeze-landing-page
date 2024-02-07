from django.db import models

# Create your models here.

class ClientData(models.Model):
    name = models.CharField(max_length=100, null=False)
    email = models.EmailField(max_length=100, null=False, unique=True)

    def __str__(self):
        return self.name
        return self.email
