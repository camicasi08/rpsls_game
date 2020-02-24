from django.forms import ModelForm
from .models import Game, Player

class GameForm(ModelForm):
     class Meta:
        model = Game
        fields = ['game_id']

class PlayerForm(ModelForm):
    class Meta:
        model = Player
        fields = '__all__'