from django.shortcuts import render
from django.http import HttpResponseRedirect
from .functions import ROT

def index(request):
    context = {
        'result': False
    }

    return render(request, 'encoder/index.html', context)

def submit(request):
    string = request.POST.get('string', "")
    rotation = int(request.POST.get('rotation', ""))
    
    context = {
        'result': True,
        'original_string': string,
        'rotation': rotation,
        'encoded_string': ROT(rotation, string)
    }
    return render(request, 'encoder/index.html', context)
