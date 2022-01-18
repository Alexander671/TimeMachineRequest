
# accounts/views.py
from django.shortcuts import render
from django.http import HttpResponse

def redirect_view(request):
    return render(request, 'base.html')