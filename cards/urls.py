from django.urls import path
from .views import (UserRegisterView,index,UserLogin,UserLogout,CreateDeckView,
                    CreateFlashcardView,ReviewFlashcardView,UpdateFlashcardReviewView,
                    DeckListView,DeleteDeckView)
# from .import views

urlpatterns=[
    path("home/",index,name="home"),
    path("register/",UserRegisterView.as_view(),name="register"),
    path("login/",UserLogin.as_view(),name="login"),
    path("logout/",UserLogout.as_view(),name="logout"),
    path("createdeck/",CreateDeckView.as_view(),name="createdeck"),
    path("listdeck/",DeckListView.as_view(),name="listdeck"),
    path("deletedeck/<int:pk>/",DeleteDeckView.as_view(),name="deletedeck"),
    path("createflashcard/",CreateFlashcardView.as_view(),name="createflashcard"),
    path("review/",ReviewFlashcardView.as_view(),name="review"),
    path("update-review/",UpdateFlashcardReviewView.as_view(),name="update-review"),
]