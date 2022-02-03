from django.shortcuts import render, HttpResponseRedirect
from .forms import ImageForm, SingupForm
from .models import ImageModel
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout

# Signup
def sign_up(request):
    if request.method == 'POST':
        reg_form = SingupForm(request.POST)
        if reg_form.is_valid():
            reg_form.save()
            messages.success(request,'Thank you for Registration!')
    else:
        reg_form = SingupForm()
    return render(request, 'signup.html', {'fm':reg_form})

# Login
def userlogin(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            login_form = AuthenticationForm(request=request, data=request.POST)
            if login_form.is_valid():
                uname = login_form.cleaned_data['username']
                upass = login_form.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request,'Login Successful')
    
                    return HttpResponseRedirect('/dashboard/')
        else:    
            login_form = AuthenticationForm()
        return render(request, 'login.html', {'fm':login_form})
    else:
        return HttpResponseRedirect('/dashboard/')

# Home
def home(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            print("yes")
            form = ImageForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
        else:
            return HttpResponseRedirect('/login/')
    form = ImageForm()
    img = ImageModel.objects.all()
    return render(request, 'home.html', {'form': form,'img':img, 'name':request.user})

# logout
def userlogout(request):
    logout(request)
    print(request.user)
    return HttpResponseRedirect('/login/')