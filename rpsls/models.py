from django.db import models

# Create your models here.

class Player(models.Model):
    nick_name = models.CharField('Ápodo', max_length=30, unique=True) 

    def __str__(self):
        return self.nick_name

class Game(models.Model):
    game_id = models.CharField('Sala', max_length=100, unique=True)
    creator = models.ForeignKey(Player, on_delete=models.CASCADE,  related_name='creator', null=True, blank=True)
    opponent = models.ForeignKey(Player, on_delete=models.CASCADE,  related_name='opponent', null=True, blank=True)
    winner = models.ForeignKey(Player, on_delete=models.CASCADE,  related_name='winner', null=True, blank=True)
    closed = models.BooleanField('Cerrado', default=False)
    def __str__(self):
        return self.game_id


""" 
class ResultGame(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    player_one = models.ForeignKey(Player, on_delete=models.CASCADE,  related_name='player_one_id')
    player_two = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='player_two_id')
    winner = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='winner', default=None, null=True)

    def show_results(self):
        if self.winner == 1:
            return self.player_one
        elif self.winner == 2:
            return self.player_two
        elif self.winner == 0:
            return 'Tie!' """

