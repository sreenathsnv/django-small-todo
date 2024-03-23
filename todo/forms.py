
from django.forms import ModelForm
from .models import CustomUser,Todo


class UserForm(ModelForm):

    class Meta:
        model = CustomUser
        fields = ['username','email','password']

class TodoForm(ModelForm):
    
    class Meta:
        model = Todo
        fields = ['heading']


 

