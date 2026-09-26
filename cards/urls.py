from django.urls import path
from .views import UserRegisterView,index,UserLogin
# from .import views

urlpatterns=[
    path("home/",index,name="index"),
    path("register/",UserRegisterView.as_view(),name="register"),
    path("login/",UserLogin.as_view(),name="login"),
]