from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def log(request):
    return render(request,'login.html')

def signup(request):
    return render(request,'signup.html')


