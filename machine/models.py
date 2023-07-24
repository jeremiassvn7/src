from django.db import models

# Create your models here.
class Trade(models.Model):#el logo es una imagen supongo que png
    icon = models.ImageField((""), upload_to=None, height_field=None, width_field=None, max_length=None)
    name = models.CharField(max_length=255)
    email = models.EmailField(blank=True,null=True)
    direction = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name



class Machine(models.Model):
    name = models.CharField(max_length=255)
    descrition = models.TextField(blank=True, null=True)
    capacity = models.IntegerField()
    bottle = models.IntegerField(blank=True, null=True)
    history_bottle = models.IntegerField(blank=True, null=True)
    uuid = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name