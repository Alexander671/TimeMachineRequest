
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from .views import redirect_view
from MakeTimeRequest.views import makeRequest

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')), # new
    path('accounts/', include('django.contrib.auth.urls')),
    path('', redirect_view),
    path('request/',  makeRequest.as_view(), name = 'makeRequest')
 
]
