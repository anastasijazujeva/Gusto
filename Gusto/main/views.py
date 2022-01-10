from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# main page for unauthorized users
# if user is authorized, then he is redirected to home page
def main(request):
    if not request.user.is_authenticated:
        return render(request, 'main/main.html')
    else:
        return redirect('main:home')

# home page for authorized users
@login_required(login_url="account/login")
def home(request):
    return render(request, 'main/home.html')
