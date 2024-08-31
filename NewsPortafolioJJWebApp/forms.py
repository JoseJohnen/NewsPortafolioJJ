from django import forms
from django.contrib.auth.models import User
from NewsPortafolioJJWebApp.models import News

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content']

        labels = {
            'title':'Título',
            'content':'Contenido',
        }

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'un título'}),
            'content': forms.TextInput(attrs={'class':'form-control', 'placeholder':'algún contenido'}),
        }


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    class Meta:
        model = User
        fields = ['username', 'password', 'password_confirm']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        # CHeck if the passwords match
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Passwords do not match!")
        return cleaned_data