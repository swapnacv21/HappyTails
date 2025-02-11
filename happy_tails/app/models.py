from django.db import models

# Create your models here.

class Pets(models.Model):
    pet_id = models.TextField()
    pet_name = models.TextField()
    gender = models.TextField()
    age = models.IntegerField()
    adoption_fee = models.IntegerField()
    img = models.FileField()
    dis = models.TextField()

    