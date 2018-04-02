from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,get_user_model
from ecommerce.forms import LoginForm,RegisterForm



def home_page(request):
    return render(request,"home.html",)


def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        "form" : form
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request,username=username,password=password)
        if user is not None :
            login(request,user)
            return redirect("/")
        else:
            print("error")
    
    return render(request,"auth/login.html",context)

def register_page(request):
    form = RegisterForm(request.POST or None)
    User = get_user_model()
    context = {
        'form' : form
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        email    = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        User.objects.create_user(username,email,password)
       
        

    return render(request,"auth/register.html",context)