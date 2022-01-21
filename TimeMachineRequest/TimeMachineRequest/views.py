
# accounts/views.py
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
def redirect_view(request):
    return redirect('request/')