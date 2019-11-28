from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import RegistrationForm, AccountAuthenticationForm, AccountUpdateForm
from django.urls import reverse
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy


# Defines how navigation fields are navigated and formatted before being passed off for verification
def registration_view(request):
    context = {}
    # If the request is a POST request, set form
    if request.POST:
        form = RegistrationForm(request.POST)
        # If there's no errors in the form, proceed
        if form.is_valid():
            # form.save()
            # Makes sure regardless of how the user entered their data that it's always returned in a consistent format
            clean = form.cleaned_data

            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            first_name = form.cleaned_data.get('first_name')
            middle_name = form.cleaned_data.get('middle_name')
            last_name = form.cleaned_data.get('last_name')
            ssn = form.cleaned_data.get('ssn')
            username = form.cleaned_data.get('username')
            street = form.cleaned_data.get('street')
            city = form.cleaned_data.get('city')
            state = form.cleaned_data.get('state')
            zip_code = form.cleaned_data.get('zip_code')
            dob = form.cleaned_data.get('dob')
            citizen = form.cleaned_data.get('citizen')
            gender = form.cleaned_data.get('gender')
            disqualified = form.cleaned_data.get('disqualified')
            restored = form.cleaned_data.get('restored')
            active_mil = form.cleaned_data.get('active_mil')
            sig = form.cleaned_data.get('sig')

            # Sends all that information to account for authentication
            account = form.save()
            # account = authenticate(email=email, password=raw_password, first_name=first_name, last_name=last_name, username=username, zip_code=zip_code, dob=dob)
            # Send that information as a login request
            login(request, account, backend='django.contrib.auth.backends.ModelBackend')

            # If login is successful go to homepage
            return redirect('sffrg:home')
            # return render(request, "sffrg/home.html")
        else:
            context['registration_form'] = form
    # If it's not a POST request, it's a GET request which means they're visiting the page for the first time
    else:
        form = RegistrationForm()
        context['registration_form'] = form
        # login(request, context, backend='django.contrib.auth.backends.ModelBackend')
    return render(request, 'accounts/register2.html', context)


# Logs out user and redirects them to the home page
def logout_view(request):
    logout(request)
    return redirect('sffrg:home')


# Logs in user, checks for authentication, then either returns an error or redirects them to home page
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
        # Calls account Authentication form that will return an error if the values dont meet the requirements
        form = AccountAuthenticationForm()

    context['login_form'] = form
    return render(request, 'accounts/login.html', context)


# Shows account info
def account_view(request):
    context = {}
    # If user isn't authenticated return them to the login screen
    if not request.user.is_authenticated:
        return redirect('login')

    if request.POST:
        # Requests information of the logged in user
        form = AccountUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
    else:
        # Presents what the user's current account information is

        form = AccountUpdateForm(
            initial=
            {
                "email": request.user.email,
                "username": request.user.username,
                "street": request.user.street,
                "city": request.user.city,
                "zip_code": request.user.zip_code,
                "state": request.user.state,

                # Add other authentication information here
            }
        )
    context['account_form'] = form
    return render(request, 'accounts/account.html', context)






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