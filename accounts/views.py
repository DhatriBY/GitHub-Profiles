from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .forms import RegistrationForm
from django.shortcuts import render

# Request to website and download HTML contents


class SignUpView(generic.CreateView):
    form_class = RegistrationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
class ExploreView(generic.CreateView):
    template_name = 'registration/explore.html'
    form_class=RegistrationForm
class ProfileView(generic.CreateView):
    template_name = 'registration/profile.html'
    form_class=RegistrationForm
