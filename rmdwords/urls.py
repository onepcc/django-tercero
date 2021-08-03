from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('ramdom_word', views.rng),
    path('reset', views.reset),
    	   
]