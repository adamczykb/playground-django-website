from django.shortcuts import render
from django.urls import path
from website import views
app_name = 'przedszkole'
urlpatterns = [
    path('', views.index, name="Glowna"),
    path('grupa/',views.panel,name="Panel"),
    path('aktualnosci/<int:nr_art>', views.aktualnosci, name="Posty")
]
