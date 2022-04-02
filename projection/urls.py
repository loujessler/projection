from django.contrib import admin
from django.urls import path
from framesearch import views


urlpatterns = [
    path('secret_page/', admin.site.urls),
    path('', views.home_page),
]
