from django import forms
from .models import Task
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
class TaskForm(forms.ModelForm):
    class Meta:
        model=Task
        fields=['title','description','due_date','complited','task_day','task_week','task_month','task_year']

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password_confirm = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean_password_confirm(self):
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.get('password_confirm')
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Passwords don't match")
        return password_confirm
    
class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)