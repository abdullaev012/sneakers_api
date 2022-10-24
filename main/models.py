from django.db import models

# Create your models here.

class Sneakers(models.Model):
    sneakers_name = models.CharField(max_length = 150, verbose_name = 'Название')
    description = models.CharField(max_length = 170, verbose_name = 'Описание')
    image = models.ImageField(upload_to='main', verbose_name='Фото')
    price = models.IntegerField(verbose_name='Цена')