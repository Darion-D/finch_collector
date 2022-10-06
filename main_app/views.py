from ast import Del
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import Game
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView


# Create your views here.

class Home(TemplateView):
    template_name = 'home.html'

class About(TemplateView):

    template_name = 'about.html'

class GameList(TemplateView):
    template_name = 'game_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get('name')
        if name != None:
            context['games'] = Game.objects.filter(name__icontains=name)
            context['header'] = f'Searching for {name}'
        else:
            context['games'] = Game.objects.all()
            context['header'] = 'Trending Games'
        return context

class GameCreate(CreateView):
    model = Game
    fields = ['name', 'img',  'description']
    template_name = 'game_create.html'
    success_url = '/games/'

class GameDetail(DetailView):
    model = Game
    template_name = 'game_detail.html'

class GameUpdate(UpdateView):
    model = Game
    fields = ['name', 'img',  'description']
    template_name = 'game_update.html'
    success_url = '/games/'

class GameDelete(DeleteView):
    model = Game
    template_name = 'game_delete_confirmation.html'
    success_url = '/games/'
