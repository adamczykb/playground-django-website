from time import timezone

import gallery.models
from django.db import models
# Create your models here.
from django import forms
from django_summernote.widgets import SummernoteInplaceWidget, SummernoteWidget
from pilkit.processors import ResizeToFill
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill


class Strona(models.Model):
    def __str__(self):
        return 'strona: ' + self.tytul

    ID = models.AutoField(primary_key=True, editable=False, default=1)
    nazwa_podreczna = models.CharField(max_length=255, verbose_name="Nazwa dla listy stron")
    tytul = models.CharField(max_length=255, verbose_name="Tytul strony")
    data = models.DateTimeField(auto_now_add=True, verbose_name="Data wydania", null=True)
    tresc = models.TextField(default="")
    odnosnik_do_galerii = models.ForeignKey('gallery.Album', verbose_name="Nazwa albumu", blank=True,
                                            on_delete=models.DO_NOTHING, null=True)
    statyczna = models.BooleanField(default=False, verbose_name="Jeżeli strona jest statyczna", blank=True)
    link_statyczny = models.CharField(max_length=255, verbose_name="Link do strony statycznej", blank=True, default='')

    class Meta:
        verbose_name_plural = "Podstrony www"


class Elementy(models.Model):
    def __str__(self):
        return self.nazwa_elementu + ': ' + self.nazwa_uzytkownika_elementu

    ID = models.AutoField(primary_key=True, editable=False)
    nazwa_elementu = models.CharField(max_length=255, verbose_name="Element statyczny strony głównej "
                                                                   "!nie zmieniać!", editable=False)
    nazwa_uzytkownika_elementu = models.CharField(max_length=255, verbose_name="Napis na elemencie", blank=True)
    kategoria = models.CharField(max_length=255, verbose_name="Kategoria elementu")

    class Meta:
        verbose_name_plural = "Elementy na stronie www"


class PodElementy(models.Model):
    def __str__(self):
        return 'dodatek: ' + self.tytul

    ID_pod = models.AutoField(primary_key=True, editable=False)
    tytul = models.CharField(max_length=255, verbose_name="Napis na elemencie")
    powiazanie_z_elementem = models.ForeignKey(to=Elementy, on_delete=models.DO_NOTHING,
                                               verbose_name="Z jakim elementem wspolpracuje")
    link_do_strony = models.ForeignKey(to=Strona, on_delete=models.DO_NOTHING)
    zdjecie = models.ImageField(upload_to='images/slider/', verbose_name="Wybor zdjecia (Tylko dla slidera)",
                                blank=True)
    order = models.IntegerField(default=0, verbose_name="Kolejność")

    class Meta:
        verbose_name_plural = "Elementy użytkownika"


class GrupyPrzedszkolne(models.Model):
    def __str__(self):
        return 'grupa: ' + self.nazwa_grupy

    nazwa_grupy = models.CharField(max_length=255, verbose_name="Nazwa Grupy", null=False)
    skrot = models.CharField(max_length=20, verbose_name="Skrót nazwy", primary_key=True, unique=True, null=False)
    albumy_zdjeciowe = models.ManyToManyField('gallery.Album', blank=True,
                                              verbose_name="Nazwy albumów powiazane z grupa przedszkolna")
    zdjecie_grupy = ProcessedImageField(upload_to='images/grupy/',
                                  format='JPEG',
                                  options={'quality': 100}, null=True, blank=True)
    class Meta:
        verbose_name_plural = "Grupy w przedszkolu"

    def Liczba_rodzicow(self, ):
        return self.skrot


class Aktualnosci(models.Model):
    def __str__(self):
        return 'post: ' + self.tytul

    ID = models.AutoField(primary_key=True, editable=False)
    tytul = models.CharField(max_length=255, verbose_name="Tytul")
    data = models.DateTimeField(editable=True, verbose_name="Data wydania", null=True)
    tresc = models.TextField(default="")
    odnosnik_do_galerii = models.ForeignKey('gallery.Album', verbose_name="Nazwa albumu", blank=True,
                                            on_delete=models.DO_NOTHING, null=True)
    important = models.BooleanField(default=False, verbose_name="Komunikat")
    zdjecie = ProcessedImageField(upload_to='images/aktualnosci/',
                                  format='JPEG',
                                  options={'quality': 100}, null=True, blank=True)
    visible = models.BooleanField(default=True, verbose_name="Widoczne")
    event = models.OneToOneField(null=True, blank=True, on_delete=models.DO_NOTHING, to='schedule.Event')
    do_kogo = models.ManyToManyField(to=GrupyPrzedszkolne, blank=True,
                                     verbose_name="Gdzie ma być wyswietlana aktualność (domyslnie na głównej)")

    class Meta:
        verbose_name_plural = "Wpisy aktualności"


class Slider(models.Model):
    def __str__(self):
        return 'Górny Slider: ' + self.slug

    slug = models.CharField(max_length=200)
    zdjecie = ProcessedImageField(upload_to='images/slidergorny/',
                                  format='JPEG',
                                  options={'quality': 100}, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Slider ze zdjeciami placówki"
