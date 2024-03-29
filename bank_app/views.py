from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from  . models import Place
from  . models import Team
# Create your views here.
def demo(request):
    obj=Place.objects.all()
    obj1=Team.objects.all()
    return render(request,"index.html", {'result':obj,'results':obj1})

def register(request):
    if request.method== 'POST':
        username=request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Taken")
                return  redirect("register")
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email Taken")
                return  redirect("register")
            else:
                user=User.objects.create_user(username=username,password=password,first_name=first_name,last_name=last_name,email=email)

                user.save();
                return redirect('login')

        else:
            messages.info(request,"password not matched")
            return  redirect('register')
        return  redirect('/')


    return render(request,"index.html")