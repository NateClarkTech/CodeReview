from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect, get_object_or_404
from . models import Thread


def login_register(request):    
    return render(request, "login_register.html")

def threads(request):
    if request.user.is_authenticated:
        threads = Thread.objects.all()
        return render(request, "threads.html", {"threads": threads})
    
    else:
        return render(request, "login_register.html")


def thread(request, id):
    if request.user.is_authenticated:
        thread = get_object_or_404(Thread, pk=id)

        return render(request, "thread.html", {"thread": thread})
    
    else:   
        return render(request, "login_register.html")
    
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("threads")
    else:
        form = UserCreationForm()
    return render(request, "register.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("threads")
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})