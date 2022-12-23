from django.shortcuts import render
from random import randint

# Create your views here.

def lobby(request):
    random_number = randint(1000, 9999)
    context = {
        'random': random_number
    }
    return render(request, 'chat/lobby.html', context)
