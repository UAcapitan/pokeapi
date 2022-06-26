from django.http import HttpResponse
from django.shortcuts import render, redirect
import requests
import requests_cache
from . import models

def get_pokemon(pokemon):
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon}').json()
    id_ = response['id']
    name = response['name']
    img = response['sprites']['front_default']
    pokemon = {
        'id': id_,
        'name': name, 
        'img': img
    }
    return pokemon

def main(request):
    return render(request, 'main/main.html')

def personal_account(request):
    if request.user.is_authenticated:
        context = {
            'user': request.user
        }

        pokemons = models.Pokemon.objects.filter(user=request.user)
        print(pokemons)
        
        if len(pokemons) != 0:
            context['pokemons'] = pokemons

        return render(request, 'main/personal_account.html', context=context)
    else:
        return redirect('auth/reg')

def change_pokemon(request, page=1):
    if request.user.is_authenticated:
        requests_cache.install_cache(cache_name='pokeapi_cache', backend='sqlite', expire_after=3600)

        list_ = []
        for i in range(1+(page-1)*9, page*9+1):
            try:
                list_.append(get_pokemon(i))
            except:
                break

        context = {
            'pokemons':list_
        }

        if page != 1:
            context['back'] = page - 1

        if len(list_) == 9:
            context['next'] = page + 1
        elif len(list_) == 0:
            context['back'] = 1
            context['text'] = 'This page is empty.'

        return render(request, 'main/change_pokemon.html', context)
    else:
        return redirect('auth/reg')

def choice_pokemon(request, id):
    if request.user.is_authenticated:
        response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{id}')
        if response.status_code == 200:
            pokemon = get_pokemon(id)
            if len(models.Pokemon.objects.filter(user=request.user, pokemon_id=id).all()) == 0:
                p = models.Pokemon(
                    user = request.user,
                    pokemon_id=pokemon['id'], 
                    pokemon_name=pokemon['name'],
                    pokemon_image=pokemon['img']
                )
                p.save()
        
        return redirect('main:account')

def delete_pokemon(request, id):
    if request.user.is_authenticated:
        models.Pokemon.objects.filter(user=request.user, pokemon_id=id).all().delete()
    return redirect('main:account')