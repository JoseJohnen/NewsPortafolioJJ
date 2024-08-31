from django.shortcuts import HttpResponse, render, redirect
from .models import News
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.contrib.auth.models import User
from .forms import RegisterForm, NewsForm

from django.http import HttpResponseRedirect
# Create your views here.


# Login, Register, Logout, Etc...
def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = User.objects.create_user(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form':form})

def login_view(request):
    error_message = None
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next_url = request.POST.get('next') or request.GET.get('next') or 'home'
            return redirect(next_url)
        else:
            error_message = "Invalid Credentials!"
    return render(request, 'accounts/login.html', {'error':error_message})

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('login')
    else:
        return redirect('home')

# Home View
# Using the decorator
# @login_required # With this, you can make any method -and view accesed from it- to require to login
def home_view(request):
    news = [
        { 
            'title': 'Begining',
            'content':'Some news ... How to put together hard data and data from db, see the code for more details',
            'date': '2024-06-17'
        },
        { 
            'title': 'Something happend in the index template',
            'content':'Some more news ... How to set the right spaces (although with less than appropiate colours) you also need to see the code for that',
            'date': '2024-06-17'
        },
        { 
            'title': 'End',
            'content':'And some more news, who would it though?',
            'date': '2024-06-17'
        },
    ]

    #To make anon types
    #anon=type('', (object, ), {})

    for m in News.objects.all():
        # news.append(type('', (object,), { m }) ) # If you format properly from the class, you use it like this, else, you make it like the next line
        news.append(type('', (object,), { "title" : m.title, "content": m.content, "date": m.date }) )

    data = {'name': "joseph",'version': "1.0.1",'news':news}
    
    # template = loader.get_template("auth1_app/home.html")
    # res = template.render ({}, request)
    # return HttpResponse(res)
    return render(request, 'auth1_app/home.html', data)

# Protected View
class ProtectedView(LoginRequiredMixin, View):
    login_url = '/login/'
    #  'next' - to redirect URL
    redirect_field_name = 'redirect_to'

    def get(self, request):
        return render(request, 'registration/protected.html')

    
# News to Create
@login_required
def News_Form(request):
    submitted = False
    if request.method == "POST":
        # Así puedes, si requieres, pasar data individual
        # nombre = request.POST.get("nombre")
        # data = {'nombre': nombre,'form':form}

        form = NewsForm(request.POST)
        if form.is_valid():
            saveObj = form.save(commit=False)
            saveObj.User_id = request.user.id
            saveObj.save()
            return HttpResponseRedirect('/news?submitted=True')
        else:
            form = NewsForm()
            if 'submitted' in request.GET:
                submitted = True #although i should extract the value, but it's faster this way and kinda forced from the circumstances

        data = {'form':form,'submitted':submitted}
        return render(request, 'news/news_form.html', data)
    form = NewsForm()
    return render(request, 'news/news_form.html', {'form':form})