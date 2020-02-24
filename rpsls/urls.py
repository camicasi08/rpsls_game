
from . import views
from django.urls import  path

app_name ='rpsls'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:game_id>/', views.detail, name='detail'),
    path('new_game/', views.new_game, name='new_game'),
    path('join_game/', views.JoinGame, name='join_game'),
    path('game/<int:game_id>/<int:player_id>', views.GameView, name='game')
]