from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import View
from .form import RequestForm

from requests import get
class makeRequest (View):
    def get(self, request):
        form = RequestForm()
        return render(request, 'request/request.html', {'formset': form})


    def post(self, request):
        form = RequestForm(request.POST)
        if form.is_valid():
            
            req = form.save(commit=False)
            req.user = request.user
            req.save()

            response = get(req.url)
            print(req.url)
            return HttpResponse(response)
        return render(request, 'request/request.html', {'formset': form})