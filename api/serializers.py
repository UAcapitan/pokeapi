from rest_framework import serializers
from main import models

class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Pokemon
        exclude = ['id',]