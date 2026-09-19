

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.models import User  # to add a user through login page
from myweb.models import login as LoginModel
from django.contrib import messages  #for flash messages while registering the user in the login page. It will show a success message when the user is registered successfully.
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.hashers import check_password, make_password  # to check the password entered by the user with the hashed password stored in the database


def index(request):
    return render(request,'todo/index.html')

def login_page(request):
    if request.method == "POST":
        is_register= request.resolver_match.url_name== 'register'
        if is_register:

            username= request.POST.get('username')
            email= request.POST.get('email')
            college_id= request.POST.get('college_id')
            sem= request.POST.get('sem')
            phone= request.POST.get('phone')
            password= request.POST.get('password')
            user_record = LoginModel(username=username, email=email, college_id=college_id,sem=sem,phone=phone,password=make_password(password))
            user_record.save()
            messages.success(request, "User registered successfully!")
            return redirect('myweb:login')
        else:
            username = request.POST.get('username')
            password = request.POST.get('password')

            try:
                # Find the user record in custom login table
                user_record = LoginModel.objects.get(username=username)
        
                # Check if the entered password matches the hashed password
                if check_password(password, user_record.password):
            
                    # To make Django sessions work, get or create a dummy matching auth user, 
                    # or map it directly so session login works:
                    django_user, created = User.objects.get_or_create(username=username)
                    login(request, django_user)
            
                    messages.success(request, "Logged in successfully!")
                    return redirect("myweb:user")
                else:
                    messages.error(request, "Invalid username or password.")
                    return redirect('myweb:login')
            
            except LoginModel.DoesNotExist:
                messages.error(request, "Invalid username or password.")
                return redirect('myweb:login')
            

    return render(request, 'todo/login.html')

def user(request):
    if request.user.is_authenticated:
        return render(request, 'todo/user.html')
    else:
        return redirect('myweb:login')

def logoutuser(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect('myweb:index')

def shop(request):
    return render(request, 'todo/shop.html')

def sell(request):
    return render(request, 'todo/sell.html')

def impact(request):
    return render(request, 'todo/impact.html')

def cart(request):
    return render(request, 'todo/cart.html')


