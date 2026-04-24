from pyexpat import model

from django.db import models

class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
#Modelo de dados para o banco de dados, representando um carro
class Car(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=100)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name="car_brand")
    factory_year = models.IntegerField(blank=True, null=True)
    model_year = models.IntegerField(blank=True, null=True)
    plate = models.CharField(max_length=20, blank=True, null=True)
    value = models.FloatField(blank=True, null=True)
    photo = models.ImageField(upload_to="cars/", blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    #define a string que representa o objeto quando for chamado, por exemplo, no admin do django
    def __str__(self):
        return f"{self.brand} {self.model} ({self.model_year})"

class CarInventory(models.Model):
    cars_count = models.IntegerField()
    cars_value = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.cars_count} - {self.car_value} - {self.created_at}"
