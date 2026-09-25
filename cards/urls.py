from django.urls import path
from .views import UserRegisterView,index
# from .import views

urlpatterns=[
    path("home/",index,name="index"),
    path("register/",UserRegisterView.as_view(),name="register"),

]