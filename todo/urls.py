from django.urls import path
from .views import( 
    home,
    loginUser,
    deleteTodo,
    registerUser,
    logoutUser,
    forbidden,
    updateTodo
)
urlpatterns = [
    path('',home,name='home'),

    path('login/',loginUser,name='loginUser'),
    path('register/',registerUser,name='registerUser'),
    path('logout-user/',logoutUser,name='logoutUser'),

    path('delete-todo/<int:pk>',deleteTodo,name='deleteTodo'),
    path('forbidden',forbidden,name='forbidden'),
     path('update-todo/<int:pk>',updateTodo,name='updateTodo'),

]
