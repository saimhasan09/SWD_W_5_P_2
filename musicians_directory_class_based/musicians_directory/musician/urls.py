from django.urls import path
from . import views

urlpatterns = [
    path("add/", views.AddMusicianView.as_view(), name="add_musician"),
    path("register/", views.RegisterView.as_view(), name="register"),
    path("login/", views.UserLoginView.as_view(), name="user_login"),
    path("logout/", views.UserLogoutView.as_view(), name="user_logout"),
]
