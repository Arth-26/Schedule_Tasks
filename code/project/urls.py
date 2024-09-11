from django.urls import path
from .views import *


app_name = 'project'


urlpatterns = [
    path('', CustomLoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
]