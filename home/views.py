from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required


def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, "index.html")


def loginUser(request):
    if request.method == "POST":
        # authenticate user
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request=request, user=user)
            return redirect("/")
        else:
            # Login failed, return an error message
            error_message = "Invalid username or password."
            return render(request=request, template_name="login.html", context={"error_message": error_message})

    # Handle non-POST requests here if needed
    return render(request=request, template_name="login.html")


    

def logoutUser(request):
    logout(request=request)
    return redirect("/login")

