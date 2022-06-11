from django.urls import path
from Aristotle import views

urlpatterns = [
   path('', views.platon, name='Aristotle')
]
