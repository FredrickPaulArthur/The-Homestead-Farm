from django.shortcuts import render, redirect
from django.contrib import messages

from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm






# Create your views here.

def HomeView(request):
    context = {
        "view": "HomeView"
    }

    return render(request, "home.html", context)



def RegisterView(request):
    if request.method == 'POST':
        u_reg_form = UserRegistrationForm(request.POST)

        if u_reg_form.is_valid():
            u_reg_form.save()
            username = u_reg_form.cleaned_data.get('username')
            messages.success(request, f"Your account has been created successfully, you have been logged in {username}.")
            return redirect("login")
    else:
        u_reg_form = UserRegistrationForm()
    
    context = {
        "view": "RegisterView",
        "u_reg_form": u_reg_form
    }
    return render(request, "registration/registration.html", context)



def password_reset_confirm(request):


    return render(request, "registration/password_reset_confirm.html")




# @login_required
def ProfileView(request):
    context = {
        "view": "ProfileView",
    }


    return render(request, "profile.html", context)



def Logout(request):

    logout(request)
    # return render(request, 'registration/logout.html')
    return render(request, 'home.html')