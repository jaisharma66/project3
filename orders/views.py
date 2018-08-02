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
def carted(request, type_p, price):
    username = request.user.username
    orders = Orders(user=username, order_items=type_p, price=price)
    orders.save()
    return redirect('index')

@login_required
def view_cart(request):
    username = request.user.username
    ordered_item = Orders.objects.filter(user = username)
    print(ordered_item)
    context = {
        "ordered_item": ordered_item,
    }
    return render(request, 'orders/cart.html', context)