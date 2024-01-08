from accounts.models import User
from django.shortcuts import redirect

def create_superuser(request):
    password = "testing321"
    if User.objects.filter(email='admin@mailtrace.com').exists():
        return redirect("register01")
    User.objects.create_superuser(email='admin@mailtrace.com', password=password)
    user = User.objects.get(email='admin@mailtrace.com')
    user.set_password(password)
    user.save()
    return redirect("register01")