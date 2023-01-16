from django.db import models

# Create your models here.


class GameType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Platform(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Game(models.Model):
    name = models.CharField(max_length=255)
    type = models.ForeignKey(GameType, on_delete=models.CASCADE)
    release_year = models.CharField(max_length=255)
    developer = models.CharField(max_length=255)
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE)
    price = models.IntegerField()
