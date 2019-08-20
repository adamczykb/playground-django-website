from django.shortcuts import render
from django.urls import path
from website import views
app_name = 'przedszkole'
urlpatterns = [
    path('', views.index, name="Glowna"),
    path('grupa/',views.panel,name="Panel"),
    path('aktualnosci/<int:nr_art>', views.aktualnosci, name="Posty"),
    path('site/<int:nr_site>',views.site,name="Strona"),
    path('grupy/<str:grupa>/aktualnosci/',views.grupaAktualnosci),
    path('grupy/<str:grupa>/galeria/',views.grupaGaleria),
    path('event/<str:title>/',views.event,name="eventy"),
]
