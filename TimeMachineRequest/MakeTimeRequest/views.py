from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import View
from .form import RequestForm
from .models import Request
from requests import get


class makeRequest (View):
    def get(self, request):
        form = RequestForm()
        req = Request.objects.filter(user = request.user.id)
        print(req)
        return render(request, 'template_example/bluepink/index.html', {'req' : req, 'formset': form})
 

    def post(self, request):
        form = RequestForm(request.POST)
        if form.is_valid():
            
            req = form.save(commit=False)
            req.user = request.user
            
            req.save()
            
            
        return render(request, 'template_example/bluepink/index.html', {'formset': form})