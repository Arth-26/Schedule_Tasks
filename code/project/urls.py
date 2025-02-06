from django.urls import path
from .views import *


urlpatterns = [
    path('', CustomLoginView.as_view(), name='login'),
    path('singup/', SingUpView.as_view(), name='register'),
    path('logout/', logout_view, name='logout'),
    
    path('home/', HomeView.as_view(), name='home')
]