from django.shortcuts import render, redirect
from .models import *
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def register01(request):
    if request.method == "POST":
        check1 = False
        

        email = request.POST.get("email")
        password = request.POST.get("password")
        if User.objects.filter(email=email).exists():
            check1 = True
            messages.error(request, 'A user with that email already exists',
                        extra_tags='alert alert-warning')
            return render(request, "accounts/signup/01.html", {"existing_mail": email })
            
        else:
            user = User.objects.create(email=email, password=password)
            traceuser = TraceUser.objects.create(user=user)
            
            redirect_url = reverse('register02') + f'?user_id={user.id}'

            return redirect(redirect_url)

    return render(request, "accounts/signup/01.html")

def register02(request):
    
    user_id = request.GET.get("user_id", None)
    if request.method == "POST":
        
        user = User.objects.get(id=user_id)
        t_user = TraceUser.objects.get(user__id=user_id)
        choice = request.POST.get("choice")
        if choice == "B2B_SaaS":
            t_user.b2b_sass = True
            t_user.save()
            redirect_url = reverse('register03') + f'?user_id={user.id}'

            return redirect(redirect_url)
        else:
            t_user.ecommerce = True
            t_user.save()
            redirect_url = reverse('register03') + f'?user_id={user.id}'

            return redirect(redirect_url)
        
    return render(request, "accounts/signup/02.html")

def register03(request):
    
    if request.method == "POST":
        user_id = request.GET.get("user_id", None)
        t_user = TraceUser.objects.get(user__id=user_id)
        email = request.POST.get("connect_email")
        t_user.connect_mail = email
        t_user.save()
        redirect_url = reverse('register04') + f'?user_id={t_user.id}'

        return redirect(redirect_url)

    return render(request, "accounts/signup/03.html")

def register04(request):
    t_user_id = request.GET.get("user_id", None)
    t_user = TraceUser.objects.get(id=t_user_id)
    if request.method == "POST":
        redirect_url = reverse('register05') + f'?user_id={t_user.id}'

        return redirect(redirect_url)
    
    
    context = {
        "connect_email": t_user.connect_mail
    }
    return render(request, "accounts/signup/04.html", context)

def register05(request):
    t_user_id = request.GET.get("user_id", None)
    if request.method == "POST":
        t_user = TraceUser.objects.get(id=t_user_id)
        messages.success(request, f'Congratulations, {t_user.user.email}. Your account has been successfully created',
                            extra_tags='alert alert-success')
        redirect_url = reverse('login')
        return redirect(redirect_url)
    return render(request, "accounts/signup/05.html")

def login(request):
    return render(request, "accounts/login.html")