from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


@login_required
def main(request):
    object = render(request, "home.html")
    return object


def register(request):
    if request.method == "GET":
        form = Register_form()
        object = render(request, "register.html", {"form": form})
        return object
    elif request.method == "POST":
        form = Register_form(request.POST)
        if form.is_valid():
            form.save()
            object = redirect("login")
            return object
        else:
            object = render(request, "register.html", {"form": form})
            return object


def dobabit(request):
    if request.method == "GET":
        form = Wish_form()
        object = render(request, "add_wish.html", {"form": form})
        return object
    elif request.method == "POST":
        form = Wish_form(request.POST, request.FILES)
        if form.is_valid():
            wish = form.save(commit=False)
            wish.uzer = request.user
            wish.save()
            object = redirect("wish_list")
            return object
        else:
            object = render(request, "add_wish.html", {"form": form})
            return object


def delete(request):
    id = request.POST["id"]
    wish = Wish.objects.get(id=id)
    wish.delete()
    object = redirect("wish_list")
    return object


def checkwish(request):
    wishes = Wish.objects.filter(uzer=request.user)
    id = request.user.id
    object = render(request, "wish_list.html", {"wishes": wishes, "id": id})
    return object


def public(request, id):
    uzer = Polbzovatelb.objects.get(id=id)
    wishes = Wish.objects.filter(uzer=uzer)
    object = render(request, "public_wish_list.html", {"wishes": wishes})
    return object


def profile(request):
    if request.method == "GET":
        form = Profile_form(instance=request.user)
        object = render(request, "profile.html", {"form": form})
        return object
    elif request.method == "POST":
        form = Profile_form(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            object = redirect("profile")
            return object
        else:
            object = render(request, "profile.html", {"form": form})
            return object


def user_login(request):
    if request.method == "GET":
        object = render(request, 'login.html')
        return object
    elif request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        chukcha = authenticate(request, username=username, password=password)
        if chukcha is not None:
            login(request, chukcha)
            return redirect('main')
        else:
            object = render(request, 'login.html')
            return object


def user_logout(request):
    logout(request)
    return redirect("login")
