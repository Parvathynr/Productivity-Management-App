from django.urls import path
from .import views

urlpatterns = [
    path('Signup', views.signup, name='signup'),
    path('login', views.Login, name='login'),

]