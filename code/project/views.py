from django.shortcuts import render
from django.http import HttpResponseRedirect

def redirect_to_localhost(request):
    return HttpResponseRedirect('http://localhost:8000')