from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import UpdateProfileForm, UpdateProfileForm_Add
from products.models import Reviews

# register a user
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        # if form is filled correctly
        if form.is_valid():
            user = form.save()

            # log the user in
            login(request, user)

            return redirect('main:home')
    else:
        form = UserCreationForm()
    
    return render(request, 'users/register.html', {'form': form})

# user authentication
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)

        # if form is filled correctly 
        if form.is_valid():
            # log the user in
            user = form.get_user()
            login(request, user)

            return redirect('main:home')
    else:
        form = AuthenticationForm()
    
    return render(request, 'users/login.html', {'form': form})

# log out page is shown when user is logged out
def logout_view(request):
    logout(request)

    return render(request, 'users/logout.html')

# view my profile
@login_required(login_url="/account/login")
def view_profile(request):
    return render(request, 'users/view_profile.html')

# edit user profile page
@login_required(login_url="/account/login")
def edit_profile(request):  
    if request.method == 'POST':
        # information from User model
        form = UpdateProfileForm(data = request.POST, instance = request.user)

        # information from Profile model
        additional_form = UpdateProfileForm_Add(request.POST, request.FILES, instance = request.user.profile)
        
        # if form is filled correctly
        if form.is_valid() and additional_form.is_valid():
            form.save()
            additional_form.save()

            return redirect('users:edit_profile')
    else:
        form = UpdateProfileForm(instance = request.user)
        additional_form = UpdateProfileForm_Add(instance = request.user.profile)

    return render(request, 'users/edit_profile.html', {'form': form, 'additional_form': additional_form})

# wishlist view with all products of a user
@login_required(login_url="/account/login")
def wishlist_list(request):
    user = request.user
    wished = user.wishlist.all()

    return render(request, 'users/wishlist_list.html', {'wished': wished})

# rating list view with all products that user has rated
@login_required(login_url="/account/login")
def rating_list(request):
    rated = Reviews.objects.filter(user_id = request.user)
    
    return render(request, 'users/my_rating.html', {'rated': rated})
    