from django.urls import path
from .views import UserRegisterView,index,UserLogin,UserLogout,CreateDeckView,CreateFlashcardView,ReviewFlashcardView
# from .import views

urlpatterns=[
    path("home/",index,name="home"),
    path("register/",UserRegisterView.as_view(),name="register"),
    path("login/",UserLogin.as_view(),name="login"),
    path("logout/",UserLogout.as_view(),name="logout"),
    path("createdeck/",CreateDeckView.as_view(),name="createdeck"),
    path("createflashcard/",CreateFlashcardView.as_view(),name="createflashcard"),
    path("review/",ReviewFlashcardView.as_view(),name="review"),
]