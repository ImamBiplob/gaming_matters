from django.db import models
from tastypie.resources import ModelResource
from games.models import Game

# Create your models here.


class GameResource(ModelResource):
    class Meta:
        queryset = Game.objects.all()
        resource_name = 'games'
