from django.db import models

class Character(models.Model):
    name = models.CharField(max_length=60)
    location = models.CharField(max_length=60)
    vehicle = models.CharField(max_length=60)
    human = models.BooleanField()

    def __str__(self):
        return self.name
