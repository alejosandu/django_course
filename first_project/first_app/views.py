from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    json = {
        'inserted_value': 'Nuevo valor actualizado views.py'
    }
    return render(request, 'first_app/index.html', context=json)