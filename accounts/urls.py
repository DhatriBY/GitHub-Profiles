from django.urls import path

from .views import SignUpView,ExploreView,ProfileView
from . import models


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('explore/',models.explore,name='explore'),
    path('profile/',models.profile,name='profile'),
    path('profile/<int:id>',models.another,name='another')
]
