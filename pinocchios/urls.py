"""pinocchios URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import include, path
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views

from orders import views as orders_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("orders.urls")),
    # path('signup/', orders_views.signup, name='signup'),
    # path('login/', orders_views.login, name='login'),
    # path('admin/', admin.site.urls),
    # path('login/', auth_views.login, {'template_name': 'login.html'}, name='login'),
    # path('logout/', auth_views.logout, {'next_page': 'login'}, name='logout'),
    # path('signup/', orders_views.signup, name='signup'),
]
