from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

from orders import views as orders_views

urlpatterns = [
    path("", views.signup, name="signup"),
    path("index", views.index, name="index"),
    path("login", views.login_view, name="login_view"),
    path("logout", views.logout_view, name="logout_view"),
    path("login_r", views.login_r, name="login_r"),
    # path('login/', auth_views.login, {'template_name': 'login.html'}, name='login'),
    # path('logout/', auth_views.logout, {'next_page': 'login'}, name='logout'),
]
