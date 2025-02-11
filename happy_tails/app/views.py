from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .models import *
import os
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def shop_login(req):
    if 'shop' in req.session:
        return redirect(shop_home)
    if 'user' in req.session:
        return redirect(user_home)
    if req.method=='POST':
        uname=req.POST['uname']
        password=req.POST['password']
        data=authenticate(username=uname,password=password)
        if data:
            if data.is_superuser:
                login(req,data)
                req.session['shop']=uname    #--------------->creating session
                return redirect(shop_home)
            else:
                login(req,data)
                req.session['user']=uname
                return redirect(user_home)
        else:
            messages.warning(req,"Invalid username or password")
            return redirect(shop_login)
    else:
        return render(req,'login.html')
    

def shop_logout(req):
    logout(req)
    req.session.flush()      #-------------------delete session
    return redirect(shop_login)
    

def shop_home(req):
    if 'shop' in req.session:
        pet=Pets.objects.all()
        return render(req,'shop/home.html',{'pets':pet})
    else:
        return redirect(shop_login)
    
def register(req):
    if req.method=='POST':
        name=req.POST['name']
        email=req.POST['email']
        password=req.POST['password']
        try:
            data=User.objects.create_user(first_name=name,email=email,password=password,username=email)
            data.save()
            return redirect(shop_login)
        except:
            messages.warning(req,"Email Exists")
            return redirect(register)
    else:
        return render(req,'user/register.html')
    
    
# def user_home(req):
#     if 'user' in req.session:
#         data=Pets.objects.all()
#         return render(req,'user/customer_home.html',{'data':data})
#     else:
#         return redirect(shop_login)