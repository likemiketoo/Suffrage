from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import RegistrationForm, AccountAuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy


def registration_view(request):
    context = {}
    # If the request is a POST request, set form
    if request.POST:
        form = RegistrationForm(request.POST)
        # If there's no errors in the form, proceed
        if form.is_valid():
            form.save()
            # Format for getting data from forms
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            username = form.cleaned_data.get('username')
            zip_code = form.cleaned_data.get('zip_code')
            dob = form.cleaned_data.get('dob')
            # Put all that information in account
            account = authenticate(email=email, password=raw_password, first_name=first_name, last_name=last_name, username=username, zip_code=zip_code, dob=dob)
            # Send that information as a login request
            login(request, account)
            # If login is successful go to homepage
            return redirect('sffrg:home')
        else:
            context['registration_form'] = form
    # If it's not a POST request, it's a GET request which means they're visiting the page for the first time
    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'accounts/register.html', context)


# Logs out user and redirects them to the home page
def logout_view(request):
    logout(request)
    return redirect('sffrg:home')


def login_view(request):
    context = {}
    # Requests user to see if authenticated or not
    user = request.user
    if user.is_authenticated:
        return redirect('sffrg:home')

    # If the user has tried to login in the past
    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        # Gets uer info
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                return redirect('sffrg:home')

    else:
        # Calls account Authentication form that will return an error if the values aren't satisfied
        form = AccountAuthenticationForm()

    context['login_form'] = form
    return render(request, 'accounts/login.html', context)


# def signup(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             # reverse_lazy('login')
#             return redirect('login')
#     else:
#         form = UserCreationForm()
#     return render(request, 'signup.html', {'form': form})