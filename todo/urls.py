from django.urls import path
from .views import( 
    home,
    loginUser,
    deleteTodo
)
urlpatterns = [
    path('',home,name='home'),
    path('login/',loginUser,name='loginUser'),
    path('delete-todo/<int:pk>',deleteTodo,name='deleteTodo'),

]
