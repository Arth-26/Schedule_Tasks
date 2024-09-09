from django.urls import path
from .views import redirect_to_localhost


app_name = 'project'


urlpatterns = [
    path('redirect/', redirect_to_localhost, name='redirect_to_localhost'),
]