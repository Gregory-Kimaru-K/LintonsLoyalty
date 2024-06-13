from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def loginAdmin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('pointAdd')
    return render(request, 'loguser/login.html')


# @login_required
def pointAdd(request):
    return render(request, 'loguser/addpoints.html')

def logout_view(request):
    logout(request)
    return redirect('loginAdmin')