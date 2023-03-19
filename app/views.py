from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import Login, Registro

from .models import Usuario, Mensagem

# Create your views here.

def index(request):
    msgs = Mensagem.objects.all()
    return render(request, 'app/index.html', {'form':Login(), 'aut':request.user.is_authenticated, 'msgs':msgs})

@login_required
def send(request):
    if request.method == 'POST':
        msg = request.POST['mensagem']
        m = Mensagem.objects.create(mensagem=msg, name=request.user.username)
        m.save()
    return redirect('/')

def registro(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        Usuario.objects.create_user(username=username, password=password, email=email)
        return redirect('/')
    return render(request, 'app/registro.html', {'form':Registro()})

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')    
    return render(request, 'app/signin.html', {'form':Login()})

@login_required
def logout(request):
    #logout(request)
    return redirect('/signin/')
