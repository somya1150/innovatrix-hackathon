

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

def register_user(request):
    if request.method == 'POST':
        # Grabbing data using the 'name' attributes you just added to HTML
        u_name = request.POST.get('username')
        u_email = request.POST.get('email')
        u_pass = request.POST.get('password')
        college_id = request.POST.get('college_id') # New field!
        
        # 1. Create the basic User
        if User.objects.filter(username=u_name).exists():
            messages.error(request, "Username already taken")
            return render(request, 'todo/login.html')
            
        user = User.objects.create_user(username=u_name, email=u_email, password=u_pass)
        user.save()
        
        # 2. Redirect to login after successful registration
        messages.success(request, "Account created! Please login.")
        return redirect('myweb:login')

    return render(request, 'todo/login.html')

def index(request):
    return render(request,'todo/index.html')
def login_page(request):
    return render(request, 'todo/login.html')

def shop(request):
    return render(request, 'todo/shop.html')

def sell(request):
    return render(request, 'todo/sell.html')

def impact(request):
    return render(request, 'todo/impact.html')

def cart(request):
    return render(request, 'todo/cart.html')
