from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import todoItem

def home(request):
    template = loader.get_template('index.html')

    context = {
        "name": "sarah",
        "age" : "31"
    }
    return HttpResponse(template.render(context, request))

# def todos(request):
#     items = loader.get_template('todos.html')
#     return HttpResponse(items.render(request))


# those few lines i added myself

# Create your views here.

