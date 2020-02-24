from django.shortcuts import render, redirect
from django.http import HttpResponse,  HttpResponseRedirect
from .models import Game, Player
from .forms import GameForm, PlayerForm
from django.template.context_processors import csrf
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request, 'rpsls/index.html', {})

def detail(request, game_id):
    response = f'GAME ID: {game_id}'
    return HttpResponse(response)

def new_game(request):
    #print(request.body)
    if request.method == 'POST':
        #print(request.POST)
      
        game_form = GameForm(request.POST)
        player_form = PlayerForm(request.POST)
        try:
            verify =  Player.objects.get(nick_name = request.POST['nick_name'])
        except Player.DoesNotExist:
            verify = None
      

        if verify:
            if game_form.is_valid():
                game = game_form.save()
                game.creator = verify
                game.save()
                #print(game)
                return redirect('/rpsls/game/' + str(game.id) + '/' + str(verify.id))
        else:        
            if player_form.is_valid() and  game_form.is_valid():
                game = game_form.save()
                player = player_form.save()
                game.creator = player
                game.save()

                #print(game)
               
                return redirect('/rpsls/game/' + str(game.id) + '/' + str(player.id))
                
    else:
        game_form = GameForm()
        player_form = PlayerForm() 
    
    args ={}
    args.update(csrf(request))
    #args['test'] = ''
    args['game_form'] = game_form
    args['player_form'] = player_form
    return render(request, 'rpsls/new_game.html', args)

def JoinGame(request):
    games = Game.objects.all()
    if request.method == 'POST':
        player_form =  PlayerForm(request.POST)
        try:
            verify =  Player.objects.get(nick_name = request.POST['nick_name'])
        except Player.DoesNotExist:
            verify = None

        selected_game =  request.POST['game']
        game = Game.objects.get(id=selected_game)
       

        #print(selected_game)
        if verify:
            if game.creator == verify:
                return redirect('/rpsls/game/'+ str(game.id) + '/' + str(verify.id))
                #messages.warning(request, 'No puedes competir contra ti mismo')
            else:
                game.opponent = verify
                game.save()
                return redirect('/rpsls/game/'+ str(game.id) + '/' + str(verify.id))
        else:
            if player_form.is_valid():
                player=  player_form.save()
                if game.creator == None:
                    game.creator = player
                else:
                    game.opponent = player
                game.save()
                return redirect('/rpsls/game/'+ str(game.id) + '/' + str(player.id))
    else:
        player_form =  PlayerForm() 

    args ={}
    args.update(csrf(request))
    args['games'] = games
    #args['test'] = ''
    #args['game_form'] = game_form
    args['player_form'] = player_form    
       
    #print(games)
    return render(request, 'rpsls/join_game.html', args)

def GameView(request, game_id, player_id):
    #print(id)
    game = Game.objects.get(id=game_id)

    player = Player.objects.get(id=player_id)
    context = {}
    print(game.opponent)
    print(game.creator)
    if game.opponent == player:
        context['opponent'] = True
        context['creator'] = False
    elif game.creator == player:
        context['creator'] = True
        context['opponent'] = False
    
    context['player']  = player
    context['game'] = game

    print(context)
    #print(game)
    #print(player)
    
    return render(request, 'rpsls/game.html', context)
    