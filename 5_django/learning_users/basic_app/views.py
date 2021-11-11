from django.shortcuts import render

# Create your views here.
def index(req): return render(req, "basic_app/index.html")

def login(req): return render(req, "basic_app/login.html")

def registration(req): return render(req, "basic_app/registration.html")
