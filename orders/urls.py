from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

from orders import views as orders_views

# All of the users' paths that are visitable
urlpatterns = [
    path("", views.signup, name="signup"),
    path("index", views.index, name="index"),
    path("login", views.login_view, name="login_view"),
    path("logout", views.logout_view, name="logout_view"),
    path("login_r", views.login_r, name="login_r"),
    path("carted/<type_p>/<price>/<topping>", views.carted, name="carted"),
    path("view_cart", views.view_cart, name="view_cart"),
    path("confirm_order", views.confirm_order, name="confirm_order"),
    path("order_admin", views.order_admin, name="order_admin"),
    path("remove_admin/<identification>", views.remove_admin, name="remove_admin"),
    path("remove_user/<identification>", views.remove_user, name="remove_user"),
]
