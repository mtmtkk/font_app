from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls import static, url
from django.contrib import admin

app_name = 'app'
urlpatterns = [
    path('', views.index, name='index'),
    path('crop/', views.crop, name='crop'),
    path('result/', views.result, name='result'),
] + static.static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS) + static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
