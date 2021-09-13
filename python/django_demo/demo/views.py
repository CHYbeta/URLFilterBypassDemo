from django.shortcuts import render, HttpResponse

# Create your views here.
def admin(request):
    return HttpResponse("logged in")

def login(request):
    return HttpResponse("login")