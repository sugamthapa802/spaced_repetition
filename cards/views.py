from django.shortcuts import render,redirect
from django.http import request,response
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

def index(request):
    return render(request,"cards/index.html")


class UserRegisterView(CreateView):
    model=User
    form_class=UserCreationForm
    template_name="auth/user_form.html"
    success_url=reverse_lazy("index")