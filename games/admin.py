from django.contrib import admin
from .models import GameType, Game, Platform
# Register your models here.


# class GameTypeAdmin(admin.ModelAdmin):


class GameAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'release_year',
                    'developer', 'platform', 'price')


admin.site.register(Game, GameAdmin)
admin.site.register(GameType,)
admin.site.register(Platform)
