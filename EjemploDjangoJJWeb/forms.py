from django import forms
from EjemploDjangoJJApp.models import Member

class Memberform(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['fname', 'lname', 'email', 'passwd', 'age']