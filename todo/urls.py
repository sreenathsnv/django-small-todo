from django.urls import path
from .views import( 
    home,
    loginUser
)
urlpatterns = [
    path('',home,name='home'),
    path('login/',loginUser,name='loginUser'),
    

]
