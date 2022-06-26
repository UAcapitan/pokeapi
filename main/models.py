from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class Pokemon(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pokemon_id = models.IntegerField()
    pokemon_name = models.CharField(max_length=50)
    pokemon_image = models.CharField(max_length=250)

    def __str__(self):
        return self.user.username