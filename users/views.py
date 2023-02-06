from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# Created this Form that inherits the django default one so I could add email to the registeration form
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
# Used to add authentication to enter urls (like profile)
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        # will try to validate data with that POST data
        form = UserRegisterForm(request.POST)
        print('after POST form')
        if form.is_valid():
            print('Valid form, will save')
            form.save()
            username = form.cleaned_data.get('username')
            # flash message- display message if form data is valid
            messages.success(
                request, f'Your account has been created for {username}!')
            return redirect('login')
    else:
        print('invalid form, default form')
        form = UserRegisterForm()  # create blank form
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    # require a user is loggedin to access profile. --> Use Django login_required decorator
    if request.method == 'POST':
        userForm = UserUpdateForm(request.POST, instance=request.user)
        profileForm = ProfileUpdateForm(
            request.POST, # the post data
            request.FILES, # the 
            instance=request.user.profile)

        if userForm.is_valid() and profileForm.is_valid():
            userForm.save()
            profileForm.save()
            messages.success(request, f'Your account has been updated!')
            # redirect causes the browser to do a GET request (usually we will see weird popup on refresh due to POST request)
            return redirect('profile')
    else:
        userForm = UserUpdateForm(instance=request.user)
        profileForm = ProfileUpdateForm(instance=request.user.profile)
        context = {  # context is like props
            "userForm": userForm,
            "profileForm": profileForm
        }
    return render(request, 'users/profile.html', context)
