from django import forms

from users.models import User

class UserForm(forms.Form):
    username = forms.CharField(max_length=200, label="Nombre de usuario")
    email = forms.EmailField(label="Email")
    password = forms.CharField(max_length=200, label="Contraseña")
    
    def save(self):
        User.objects.create(
            username=self.cleaned_data['username'], 
            email=self.cleaned_data['email'], 
            password=self.cleaned_data['password'], 
        )