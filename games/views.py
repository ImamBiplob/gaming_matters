from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Game

# Create your views here.


def index(request):
    games = Game.objects.all()
    return render(request, 'games/index.html', {'games': games})


def detail(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    return render(request, 'games/detail.html', {'game': game})
