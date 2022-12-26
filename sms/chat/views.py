from django.shortcuts import render
from random import randint

# Create your views here.

def lobby(request):
    return render(request, 'chat/lobby.html')
