from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UserChangeForm
from django import forms
from .models import Bookstore,Book,Author
class SignupForm(UserCreationForm):
    password2=forms.CharField(label='conform password',widget=forms.PasswordInput)
    class Meta:
        model = User
        fields=['username', 'first_name', 'last_name', 'email']
        labels={'email':'Email'}

class EditUser(UserChangeForm):
    password=None
    class Meta:
        model = User
        fields=['username', 'first_name', 'last_name', 'email']
        labels={'email':'Email'}


class EditUserAdmin(UserChangeForm):
    password=None
    class Meta:
        model = User
        fields= "__all__"
        labels={'email':'Email'}
    
class BookRegistration(forms.ModelForm):
    class Meta:
        model = Bookstore
        fields = ['book_name', 'author_name' , 'description','price']

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['bookName']

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name']
        labels={'name':"AuthorName"}


