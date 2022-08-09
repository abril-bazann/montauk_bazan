from unicodedata import name
from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('accounts/login/', login_request, name= 'login'),
    path('logout/', LogoutView.as_view(template_name="logout.html"), name= 'logout'),
]