from django.urls import path
from . import views

urlpatterns = [
    path("",views.home_prueba, name='home_prueba'),
    path("realizar_prueba/", views.realizar_prueba, name="realizar_prueba"),
]





