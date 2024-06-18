from django.shortcuts import HttpResponse, render, redirect
# from EjemploDjangoJJApp.models import Member
from EjemploDjangoJJApp.models import News
# from .forms import Memberform
from .forms import Newsform
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

    news = [
        { 
            'title': 'Something happend in views',
            'content':'Some news ... How to put together hard data and data from db, see the code for more details',
            'date': '2024-06-17'
        },
        { 
            'title': 'Something happend in the index template',
            'content':'Some more news ... How to set the right spaces (although with less than appropiate colours) you also need to see the code for that',
            'date': '2024-06-17'
        },
        { 
            'title': 'Marcos',
            'content':'what is this, More News?',
            'date': '2024-06-17'
        },
        { 
            'title': 'Job',
            'content':'And some more news, who would it though?',
            'date': '2024-06-17'
        },
    ]

    # employes = [
    #     { 
    #         'name': 'John',
    #         'designation':'Write'
    #     },
    #     { 
    #         'name': 'Vikas',
    #         'designation':'Accountant'
    #     },
    #     { 
    #         'name': 'Marcos',
    #         'designation':'Developer'
    #     },
    #     { 
    #         'name': 'Job',
    #         'designation':'Developer'
    #     },
    # ]

    # anon=type('', (object, ), {})
    # for m in Member.objects.all():
    #     employes.append(type('', (object,), { "name" : m.fname+" "+m.lname, "designation":'Dbase'}) )

    anon=type('', (object, ), {})
    for m in News.objects.all():
        # news.append(type('', (object,), { m }) ) # If you format properly from the class, you use it like this, else, you make it like the next line
        news.append(type('', (object,), { "title" : m.title, "content": m.content, "date": m.date }) )

    # data = {'name': "joseph",'version': "1.0.1",'employees':employes}
    data = {'name': "joseph",'version': "1.0.1",'news':news}
    return render(request, 'index.html', data)

def about(request):
    return render(request, 'about.html')

def contact(request):
    return HttpResponse('<h1>This is the Contact Page</h1><br><br><p>Yes, it is like this because its here to show the example of using HttpResponse instead of render or something else in the view</p>')



def join(request):
    if request.method == "POST":
        form = Memberform(request.POST or None)
        if form.is_valid():
            form.save()
        else:
            title = request.POST['title'] 
            content = request.POST['content']
            date = request.POST['date']
            messages.success(request, ('There was an error in your form, please check it and try again'))
            #return redirect('join')
            return render(request, 'join.html', {
                'title' : title,
                'content' : content,
                'date' : date
            })

    # if request.method == "POST":
    #     form = Memberform(request.POST or None)
    #     if form.is_valid():
    #         form.save()
    #     else:
    #         fname = request.POST['fname'] 
    #         lname = request.POST['lname']
    #         email = request.POST['email']
    #         passwd = request.POST['passwd']
    #         age = request.POST['age']
    #         messages.success(request, ('There was an error in your form, please check it and try again'))
    #         #return redirect('join')
    #         return render(request, 'join.html', {
    #             'fname' : fname,
    #             'lname' : lname,
    #             'email' : email,
    #             'passwd' : passwd,
    #             'age' : age,
    #         })

        messages.success(request, ('Your Form has been Submitted Successfully'))
        return redirect('home')
    
    else:
        return render(request, 'join.html', { 'name':'Join Today'})