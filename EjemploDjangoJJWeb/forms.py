from django import forms
# from EjemploDjangoJJApp.models import Member
from EjemploDjangoJJApp.models import News

# class Memberform(forms.ModelForm):
#     class Meta:
#         model = Member
#         fields = ['fname', 'lname', 'email', 'passwd', 'age']

class Newsform(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content', 'date']