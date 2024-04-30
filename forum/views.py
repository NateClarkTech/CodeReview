from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from . models import *

#display all threads
def threads(request):
    if request.user.is_authenticated:
        #get all thread objects and pass them to the template
        threads = Thread.objects.all()
        return render(request, "threads.html", {"threads": threads})
    #if user is not logged in, redirect to landing page
    else:
        return render(request, "login_register.html")

#displays all the comments on a thread
def thread(request, id):
    if request.user.is_authenticated:
        #get all posts on a thread with the given id and pass them to the template
        thread = Thread.objects.get(id=id)
        comments = Post.objects.filter(thread=thread)
        return render(request, "thread.html", {"thread": thread, "comments": comments})
    
    #if user is not logged in, redirect to landing page
    else:   
        return render(request, "login_register.html")
    

# landing page where users can log in or register
def login_register(request):    
    return render(request, "login_register.html")

#page to register a user
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

#page for user to login
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