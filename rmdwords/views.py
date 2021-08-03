

# Create your views here.
from django.shortcuts import render, redirect
from time import localtime, strftime
from django.utils import timezone
from django.utils.crypto import get_random_string #generar string aleatorio
import random 




def index(request):
    
    return redirect ("/ramdom_word")

def rng(request):
    palabrarng = get_random_string(length=14)    
    print(palabrarng)
    
    
    
    if 'contador' in request.session:
        request.session['contador']+=1
        print(request.session['contador'])
    else:
        request.session['contador']= random.randrange(0, 10, 1)    
        print(request.session['contador'])
    
    context = {
        "word": palabrarng,
        "intento": request.session['contador']
        
    }
    return render(request,'rng.html', context)

def reset(request):
    request.session['contador']= 0
    for key, value in request.session.items():
        print('{} => {}'.format(key, value))
    return redirect ("/ramdom_word")
