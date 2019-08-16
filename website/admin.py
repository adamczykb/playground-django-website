from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
# Register your models here.
from django_summernote.admin import SummernoteModelAdmin
from .models import Aktualnosci, Strona, Elementy, PodElementy, GrupyPrzedszkolne


class MyModelForm(forms.ModelForm):
    kategorie = (

        ('Górny pasek', 'Górny pasek'), ('Pasek nawigacyjny', 'Pasek nawigacyjny'), ('Slider', 'Slider'),
        ('Boxy z informacjami', 'Boxy z informacjami'), ('Stopka', 'Stopka')
    )

    kategoria = forms.ChoiceField(choices=kategorie)


@admin.register(Elementy)
class PostAdmin(SummernoteModelAdmin):
    form = MyModelForm
    list_filter = ("kategoria",)
    list_display = ('nazwa_elementu', 'nazwa_uzytkownika_elementu', "kategoria")
    summernote_fields = '__all__'



@admin.register(Strona)
class StronyNaGl(SummernoteModelAdmin, admin.ModelAdmin):
    summernote_fields = '__all__'
    list_display = ("tytul", "data", "nazwa_podreczna")
    list_filter = ("data",)


@admin.register(GrupyPrzedszkolne)
class Grupy(admin.ModelAdmin):
    filter_horizontal = ('albumy_zdjeciowe',)
    list_display = ("skrot", "nazwa_grupy", "Liczba_rodzicow")


@admin.register(Aktualnosci)
class Aktualnosci(SummernoteModelAdmin, admin.ModelAdmin):
    summernote_fields = '__all__'
    list_display = ("tytul", "important", "visible")
    list_filter = ("important", "visible", "data")
    filter_horizontal = ('do_kogo',)


@admin.register(PodElementy)
class PodElementy(admin.ModelAdmin):
    list_display = ('powiazanie_z_elementem', 'tytul', 'link_do_strony')
    list_filter = ('powiazanie_z_elementem',)

    def link_do_strony(self, obj):
        return obj.Strona.nazwa_podreczna

    def powiazanie_z_elementem(self, obj):
        return obj.PodElementy.tytul
