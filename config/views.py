from django.shortcuts import render
from django.http import HttpResponse
from dataentry.tasks import celery_test_task
from .forms import RegistrationForm
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib import  auth



def home(request):
    return render(request, 'home.html')


def celery_test(request):
    celery_test_task.delay()
    return HttpResponse('<h3>Function Executed Successfully.</h3>')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful.')
            return redirect('register')
        else:
            context = {
                'form': form,
            }
            return render(request, 'register.html', context)
    else:
        form = RegistrationForm()
        context = {
            'form': form,
        }
    return render(request, 'register.html', context)


def login(request):
    
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            
            if user is not None:
                auth.login(request, user)
                return redirect('home')
            
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('login')
                
    else:
        form = AuthenticationForm() 
        context = {
            'form': form,
        }
        return render(request, 'login.html', context)

def logout(request):
    auth.logout(request)
    return redirect('home')