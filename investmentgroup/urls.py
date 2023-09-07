"""
URL configuration for investmentgroup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from finance.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',project,name="Project"),
    path('go/',project1,name="Project1"),
    path('invest/',Index.as_view(),name='index'),
    path('team/',project2,name='Project2'),
    path('calculator/', include('finance.urls')),
    path('calculator1/',project3,name="Project3"),
]
