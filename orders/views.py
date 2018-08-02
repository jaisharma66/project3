from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from .models import *

# Create your views here.
@login_required
def index(request):
    print("entering index function")
    context = {
        "topping": Topping.objects.all(),
        "regular_pizza": Regular_Pizza.objects.all(),
        "sicilian_pizza": Sicilian_Pizza.objects.all(),
        "subs": Subs.objects.all(),
        "pasta": Pasta.objects.all(),
        "salads": Salads.objects.all(),
        "dinner_platters": Dinner_Platters.objects.all()
    }
    return render(request, 'orders/index.html', context)

# Code learned and used from simpleisbetterthancomplex.com
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'orders/signup.html', {'form': form})

def login_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    print("login_view entered. The username is " + username + " the password is " + password)
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, 'orders/login.html', {"message": "Invalid credentials."})

def logout_view(request):
    logout(request)
    return render(request, 'orders/login.html', {"message": "Logged out."})

def login_r(request):
    return render(request, 'orders/login.html')

@login_required
def carted(request, type_p, price, topping):
    username = request.user.username
    orders = Orders(user=username, order_items=type_p, price=price, topping=topping, toppings=None)
    orders.save()
    return redirect('index')

@login_required
def view_cart(request):
    username = request.user.username
    ordered_item = Orders.objects.filter(user = username)
    print(ordered_item)
    added_price = 0
    topping_arr = []
    for prices in range(len(ordered_item)):
        added_price = added_price + ordered_item[prices].price
    for x in range(len(ordered_item)):
        topping_arr.append(ordered_item[x].topping)
    context = {
        "ordered_item": ordered_item,
        "added_price": added_price,
        "topping":  topping_arr
    }
    return render(request, 'orders/cart.html', context)

@login_required
def confirm_order(request):
    selectbox = request.POST.getlist("selectbox")
    print(selectbox, " Selectbox options.")
    username = request.user.username
    confirmed_orders = Orders.objects.filter(user = username)
    y=0
    for x in range(len(confirmed_orders)):
        if confirmed_orders[x].topping == 0:
            entered = Orders_Confirmed(user=username, order_items=confirmed_orders[x].order_items, price=confirmed_orders[x].price, topping=confirmed_orders[x].topping, toppings=None)
            entered.save()
        elif confirmed_orders[x].topping == 1:
            entered1 = Orders_Confirmed(user=username, order_items=confirmed_orders[x].order_items, price=confirmed_orders[x].price, topping=confirmed_orders[x].topping, toppings=selectbox[y])
            y = y + 1
            entered1.save()
        elif confirmed_orders[x].topping == 2:
            entered2 = Orders_Confirmed(user=username, order_items=confirmed_orders[x].order_items, price=confirmed_orders[x].price, topping=confirmed_orders[x].topping, toppings=selectbox[y] + ", " + selectbox[y + 1])
            y = y + 2
            entered.save()
        elif confirmed_orders[x].topping == 3:
            entered3 = Orders_Confirmed(user=username, order_items=confirmed_orders[x].order_items, price=confirmed_orders[x].price, topping=confirmed_orders[x].topping, toppings=selectbox[y] + ", " + selectbox[y + 1] + ", " + selectbox[y + 2])
            y = y + 3
            entered3.save()
        elif confirmed_orders[x].topping == 4:
            entered4 = entered2 = Orders_Confirmed(user=username, order_items=confirmed_orders[x].order_items, price=confirmed_orders[x].price, topping=confirmed_orders[x].topping, toppings=selectbox[y] + ", " + selectbox[y + 1] + ", " + selectbox[y + 2] + ", " + selectbox[y + 3])
            y = y + 4
            entered4.save()
    return render(request, 'orders/confirmed.html')

@login_required
def order_admin(request):
    total_orders = Orders_Confirmed.objects.all()
    context = {
        "total_orders": total_orders
    }
    if request.user.is_superuser:
        return render(request, 'orders/orders.html', context)
    else:
        return redirect('index')

@login_required
def remove_admin(request, identification):
    delete_row = Orders.objects.filter(id = identification)
    delete_row.delete()
    return redirect('order_admin')

@login_required
def remove_user(request, identification):
    delete_row = Orders.objects.filter(id = identification)
    delete_row.delete()
    return redirect('view_cart')