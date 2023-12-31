"""
URL configuration for jully20 project.

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
from django.urls import path
from app1.views import *
from app2.views import *
from app3.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('string1/', string1, name='string1'),
    path('string2/', string2, name='string2'),
    path('string3/', string3, name='string3'),
    path('string4/', string4, name='string4'),
    path('string5/', string5, name='string5'),
    path('string6/', string6, name='string6'),
]
