from django.db import models

# Create your models here.
class Car(models.Model):
    type = models.CharField(max_length=100)
    regno = models.CharField(max_length=10)
    color = models.CharField(max_length=10)

    def __str__(self):
        return self.title