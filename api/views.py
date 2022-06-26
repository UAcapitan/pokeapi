from rest_framework import permissions, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from main import models
from . import serializers
from django.contrib.auth.models import User
from django.shortcuts import render
from . import paginators

class UserViewSet(generics.ListAPIView):
    queryset = models.Pokemon.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = serializers.PokemonSerializer
    pagination_class = paginators.StandardResultsSetPagination

class UserFullViewSet(APIView):
    def get(self, request, page):
        resp = models.User.objects.filter(id__gt=1+(page-1)*3-1).filter(id__lt=page*3+1).all().values()
        list_ = []
        for i in resp:
            id = i['id']
            pokemons = models.Pokemon.objects.filter(user_id=id).all()
            list_.append({
                'id': i['id'],
                'login': i['username'],
                'email': i['email'],
                'pokemons': pokemons.values(),
                })
        count = User.objects.count()
        return Response({
            'count': count,
            'next': f'http://127.0.0.1:8000/api/v1/users/full/{str(page+1)}/' if (page+1)*3 <= count+2 else None,
            'previous': f'http://127.0.0.1:8000/api/v1/users/full/{str(page-1)}/' if page != 1 else None,
            'results': list_
        })

def main(request):
    return render(request, 'api/main.html')