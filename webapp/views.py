from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, "home.html")

def cv(request):
    return render(request, "cv.html")

def projects(request):
    return render(request, "projects.html")

def contact(request):
    return render(request, "contact.html")

def game(request):
    return render(request, "game.html")

def digitaltwin(request):
    return render(request, "digitaltwin.html")

def thesis(request):
    return render(request, "thesis.html")

def aspnetproject(request):
    return render(request, "aspnetproject.html")   

def currentproject(request):
    return render(request, "currentproject.html")   