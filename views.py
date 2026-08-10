

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from myweb.models import login
from django.contrib import messages  #for flash messages while registering the user in the login page. It will show a success message when the user is registered successfully.



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
            user_record = login(username=username, email=email, college_id=college_id,sem=sem,phone=phone,password=password)
            user_record.save()
            messages.success(request, "User registered successfully!")
            return redirect('myweb:login')
        else:
            username= request.POST.get('username')
            password= request.POST.get('password')
            messages.error(request,"invalid username or password")
            return redirect('myweb:login')


    return render(request, 'todo/login.html')

def shop(request):
    return render(request, 'todo/shop.html')

def sell(request):
    return render(request, 'todo/sell.html')

def impact(request):
    return render(request, 'todo/impact.html')

def cart(request):
    return render(request, 'todo/cart.html')


