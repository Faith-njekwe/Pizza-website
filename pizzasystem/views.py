from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import PizzaForm
from .forms import Checkout
from django.utils.timezone import now 
from .models import UserProfile, Pizza
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm



def index(request):
    return render(request, 'index.html')

@login_required
def pizza_order(request):
    if request.method == 'POST':
        form = PizzaForm(request.POST)
        if form.is_valid():
            pizza_order = form.save(commit=False)
            pizza_order.user = request.user
            pizza_order.save()
            request.session['order_id'] = pizza_order.id #each pizza object has a unique id
            
            return redirect('checkout') 
    else:
        form = PizzaForm()
    return render(request, 'order.html', {'form':form})

@login_required
def checkout(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        form = Checkout(request.POST, instance=user_profile) 
        if form.is_valid():
            form.save()
            return redirect('confirmation', order_id=request.session['order_id'])
        else:
            print(form.errors) 
    else:
        form = Checkout(instance=user_profile)
    return render(request, 'checkout.html', {'form': form})

@login_required
def confirmation(request, order_id):
    order_id = request.session.get('order_id')
    order = Pizza.objects.get(id=order_id, user=request.user)

    return render(request, 'confirmation.html', {'order': order})

def login_user(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, f'Hi, {user.username}!')
			return redirect('index')
		
		else:
			messages.success(request, ("There Was An Error Logging In, Try Again..."))	
			return redirect('login')	

	else:
		return render(request, 'registration/login.html', {})

def logout_user(request):
	logout(request)
	messages.success(request, ("You Were Logged Out!"))
	return redirect('index')


def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            messages.success(request, "Registration successful!")
            return redirect('index')  # Redirect to a success or home page
        else:
            messages.error(request, "Unsuccessful registration. Invalid information.")
    else:
        form = UserCreationForm()
    return render(request, 'registration/register_user.html', {'form': form})

@login_required
def list_orders(request):
    # Fetch all pizza orders for the logged-in user
    orders = Pizza.objects.filter(user=request.user).order_by('-order_date')
    return render(request, 'list-out.html', {'orders': orders})






