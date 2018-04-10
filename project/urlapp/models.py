from django.db import models

# Create your models here.

class Urls(models.Model):
    name = models.URLField(unique=True)

    def __str__(self):
        return self.name

