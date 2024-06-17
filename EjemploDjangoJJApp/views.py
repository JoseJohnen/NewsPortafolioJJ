from django.shortcuts import render, HttpResponse

# Create your views here.
def Appview(request):
    return HttpResponse('<h1> This is an APP View Page</h1>')