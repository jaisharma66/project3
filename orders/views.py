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
    # Method to signup users using their name and saving it to a form in the DB
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

# Checks to see if the users login credentials are correct. Retrieves from the form
def login_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, 'orders/login.html', {"message": "Invalid credentials."})

# Logs the user out and renders the login template
def logout_view(request):
    logout(request)
    return render(request, 'orders/login.html', {"message": "Logged out."})

# Redirects the user to the login page as seen in HTML
def login_r(request):
    return render(request, 'orders/login.html')

# Adds the users item to the database to be displayed in their cart
@login_required
def carted(request, type_p, price, topping):
    username = request.user.username
    orders = Orders(user=username, order_items=type_p, price=price, topping=topping, toppings=None)
    orders.save()
    return redirect('index')

# Gets the users cart from the database and displays it. Also displays the total price passed as a var
@login_required
def view_cart(request):
    username = request.user.username
    ordered_item = Orders.objects.filter(user = username)
    added_price = 0
    topping_arr = []
    for prices in range(len(ordered_item)):
        added_price = added_price + ordered_item[prices].price
    for x in range(len(ordered_item)):
        topping_arr.append(ordered_item[x].topping)
    # Context dictionary passes an array that describes the number of toppings on a specific item
    # Correlates with HTML
    context = {
        "ordered_item": ordered_item,
        "added_price": added_price,
        "topping":  topping_arr
    }
    return render(request, 'orders/cart.html', context)

# Confirms the users order and adds it to the admin site
@login_required
def confirm_order(request):
    selectbox = request.POST.getlist("selectbox")
    username = request.user.username
    confirmed_orders = Orders.objects.filter(user = username)
    # Var y that is incremented to go through selectbox list
    y=0
    # These checks check to see how many toppings an item has, and depending on that, adds those toppings from the selectbox list.
    # After it adds it to the list, it increments forward by the amount of toppings present in that specific item
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

# Checks if the user is a superuser and sends them to the appropriate all orders page.
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

# An admin tool that removes an order. This is the personal touch
@login_required
def remove_admin(request, identification):
    delete_row = Orders.objects.filter(id = identification)
    delete_row.delete()
    return redirect('order_admin')

# A user tool that removes an order. This is the personal touch
@login_required
def remove_user(request, identification):
    delete_row = Orders.objects.filter(id = identification)
    delete_row.delete()
    return redirect('view_cart')