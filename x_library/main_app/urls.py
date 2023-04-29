from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name='index'),
   
   # signup
   path('accounts/signup/', views.signup, name='signup'),
]