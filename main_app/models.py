from operator import mod
from django.db import models

# Create your models here.
class Game(models.Model):

    name = models.CharField(max_length=100)
    img = models.CharField(max_length=250)
    description = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering= ['name']

class Developer(models.Model):

    name = models.CharField(max_length=150)
    number_of_games = models.IntegerField(default=0)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='developers')
