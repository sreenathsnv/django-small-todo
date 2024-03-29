
from django.forms import ModelForm
from .models import CustomUser,Todo


class UserRegisterForm(ModelForm):

    class Meta:
        model = CustomUser
        fields = ['username','email']

class UserLoginForm(ModelForm):

    class Meta:
        model = CustomUser
        fields = ['email']


class TodoForm(ModelForm):
    
    class Meta:
        model = Todo
        fields = ['heading']


 

