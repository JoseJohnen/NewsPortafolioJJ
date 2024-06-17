from django.shortcuts import HttpResponse, render, redirect
from EjemploDjangoJJApp.models import Member
from .forms import Memberform
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

def authView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})

@login_required
def dashboard(request):
    return render(request, "dashboard.html")

def homepage(request):

    employes = [
        { 
            'name': 'John',
            'designation':'Write'
        },
        { 
            'name': 'Vikas',
            'designation':'Accountant'
        },
        { 
            'name': 'Marcos',
            'designation':'Developer'
        },
        { 
            'name': 'Job',
            'designation':'Developer'
        },
    ]

    anon=type('', (object, ), {})
    for m in Member.objects.all():
        employes.append(type('', (object,), { "name" : m.fname+" "+m.lname, "designation":'Dbase'}) )

    data = {'name': "joseph",'version': "1.0.1",'employees':employes}
    return render(request, 'index.html', data)

def about(request):
    return render(request, 'about.html')

def contact(request):
    return HttpResponse('<h1>This is Contact Page</h1>')



def join(request):
    if request.method == "POST":
        form = Memberform(request.POST or None)
        if form.is_valid():
            form.save()
        else:
            fname = request.POST['fname'] 
            lname = request.POST['lname']
            email = request.POST['email']
            passwd = request.POST['passwd']
            age = request.POST['age']
            messages.success(request, ('There was an error in your form, please check it and try again'))
            #return redirect('join')
            return render(request, 'join.html', {
                'fname' : fname,
                'lname' : lname,
                'email' : email,
                'passwd' : passwd,
                'age' : age,
            })

        messages.success(request, ('Your Form has been Submitted Successfully'))
        return redirect('home')
    
    else:
        return render(request, 'join.html', { 'name':'Join Today'})