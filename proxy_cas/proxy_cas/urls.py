"""
URL configuration for proxy_cas project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
import django_cas_ng.views
from .views import home
from . import views

urlpatterns = [
    path('', home, name="home"),
    path('admin/', admin.site.urls),
    path('cas/pt', views.get_pt, name='get_pt'),
    path('cas/callback', django_cas_ng.views.CallbackView.as_view(), name='cas_ng_proxy_callback'),
]
