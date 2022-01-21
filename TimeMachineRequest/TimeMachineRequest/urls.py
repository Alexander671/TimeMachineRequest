
from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from .views import redirect_view
from MakeTimeRequest.views import makeRequest
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')), # new
    path('accounts/', include('django.contrib.auth.urls')),
    path('', redirect_view),
    path('request/',  makeRequest.as_view(), name = 'makeRequest')
 
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)