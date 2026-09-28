from django.shortcuts import render,redirect
from django.http import request,response
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView,LogoutView
from django.views.generic import CreateView, ListView, DetailView, DeleteView
from .forms import CustomLoginForm,DeckForm,FlashcardForm
from .models import Deck,Flashcard
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import date

def index(request):
    return render(request,"cards/home.html")


class UserRegisterView(CreateView):
    model=User
    form_class=UserCreationForm
    template_name="auth/user_form.html"

class UserLogin(LoginView):
    template_name="auth/login.html"
    form_class=CustomLoginForm

class UserLogout(LogoutView):
    pass


class CreateDeckView(LoginRequiredMixin,CreateView):
    model=Deck
    form_class=DeckForm
    template_name="cards/deck_form.html"
    success_url=reverse_lazy("home")
    def form_valid(self, form):
        form.instance.owner=self.request.user
        return super().form_valid(form)

class CreateFlashcardView(LoginRequiredMixin,CreateView):
    # login_url="login"
    model=Flashcard
    form_class=FlashcardForm
    template_name="cards/flashcard_form.html"
    success_url=reverse_lazy("home")


class ReviewFlashcardView(LoginRequiredMixin,ListView):
    template_name="cards/review.html"
    context_object_name="flashcards"
    def get_queryset(self):
        return Flashcard.objects.filter(deck__owner=self.request.user,
                                        due_date=date.today())
    
    