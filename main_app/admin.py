from django.contrib import admin
from .models import Developer, Game

# Register your models here.
admin.site.register(Game)
admin.site.register(Developer)
