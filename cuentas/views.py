from django.shortcuts import render, redirect
from django.contrib.auth import  login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import RegisterForm

# Create your views here.

def registerView(request):

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        
    form = RegisterForm()
    context = {'form': form}
    return render(request, 'cuentas/register.html', context)

def loginView(request):

    if request.method == 'POST':

        user = authenticate(request.POST, username = request.POST.get('username'), password = request.POST.get('password'))
        if user:

            login(request, user)
            return redirect('home')

        messages.info(request, 'Email o contraseña incorrecto')
        return render(request, 'store/store.html', {})

@login_required(login_url='home')
def logoutView(request):
    logout(request)
    return redirect('home')