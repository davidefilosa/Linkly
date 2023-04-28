from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from .forms import LoginForm

urlpatterns = [
path("signup/", views.signup, name="signup" ),
path("login/", LoginView.as_view(form_class=LoginForm, template_name="accounts/login.html"), name="login" ),
path("logout/", LogoutView.as_view(), name="logout" ),
  
]
