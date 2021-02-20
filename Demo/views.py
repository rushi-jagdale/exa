from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages 
# Create your views here.
def home(request):
    return render(request,'home.html')

def login(request):
    if request.method == 'POST':
                              
        email = request.POST['email']
        print(email)
        password = request.POST['password']
        user = auth.authenticate( email = email)
        
        print(user)
        if user is not None:
            auth.login(request, user)   
            return redirect('/')
        else:
            messages.info(request, 'invalid username and password')
            return redirect('login')
    else:
        return render(request, 'login.html') 
               
   
   

def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
       
        if User.objects.filter(username = username).exists():
            messages.info(request, 'username already taken..')
            return redirect('register')
        elif User.objects.filter(email = email).exists():
            messages.info(request, 'Email already taken')  
            return redirect('register')
        else:
            user = User.objects.create_user(username=username, password=password, email=email)
            user.save()
            return redirect('login')

            

    return render(request, 'register.html')    