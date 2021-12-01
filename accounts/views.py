from django.shortcuts import render,redirect
from django.contrib.auth.models import auth,User
from django.contrib import messages
# Create your views here.

def register(request):
    if request.method=='POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password1']
        password2=request.POST['password2']
        if password==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username already exists")
                return redirect('register')
            if User.objects.filter(email=email).exists():
                messages.info(request,"email already taken by a user")
                return redirect('register')
            else:
                user=User.objects.create_user(first_name=firstname,last_name=lastname,username=username,password=password)
                user.save()
                print("new user added")
                return redirect('/')
        else:
            messages.info(request,"passwords not match")
        return redirect('register')
    else:
        return render(request,'register.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        print(username,password)
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            print('login successfull')
        else:
            messages.info(request,'invalid user')
            return redirect('login')
        return redirect('/')
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    print('successfully logged out')
    return redirect('/')
