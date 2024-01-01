from django.shortcuts import redirect
from . import forms
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


# Create your views here.


# add musicians class


@method_decorator(login_required, name="dispatch")
class AddMusicianView(CreateView):
    template_name = "add_musician.html"
    form_class = forms.MusicianForm
    success_url = reverse_lazy("homepage")

    def form_valid(self, form):
        response = super().form_valid(form)
        return response


# register a user
class RegisterView(CreateView):
    template_name = "register.html"
    form_class = forms.RegistrationForm
    success_url = reverse_lazy("user_login")

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Registered successfully")
        return response

    def form_invalid(self, form):
        response = super().form_invalid(form)
        messages.error(self.request, "Registration failed. Please check the form")
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = "Register"
        return context


# user login class
class UserLoginView(LoginView):
    template_name = "register.html"

    def get_success_url(self):
        return reverse_lazy("homepage")

    def form_valid(self, form):
        messages.success(self.request, "Login successful")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.success(self.request, "Wrong information please try again")
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = "login"
        return context


# logout view
class UserLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("user_login")
