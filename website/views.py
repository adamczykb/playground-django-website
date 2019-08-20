import datetime

from django.contrib.auth.decorators import login_required
from django.db import connection
from django.db.models.functions import Lower
from django.http import HttpResponse
from django.shortcuts import render
from schedule.models import Calendar
from schedule.periods import Day, Month, Week, Year
from schedule.settings import (
    CHECK_EVENT_PERM_FUNC, CHECK_OCCURRENCE_PERM_FUNC, EVENT_NAME_PLACEHOLDER,
    GET_EVENTS_FUNC, OCCURRENCE_CANCEL_REDIRECT, USE_FULLCALENDAR,
)
from django.utils import timezone

# Create your views here.
from gallery.models import Album, Image
from schedule.views import CalendarByPeriodsView

from website.models import Aktualnosci, GrupyPrzedszkolne


def error_404_view(request, exception):
    data = {"name": "ThePythonDjango.com"}
    return render(request, '404_error.html', data)


def get_top(cursor):
    # g1
    cursor.execute(
        "select e.nazwa_uzytkownika_elementu from public.website_elementy as e where e.nazwa_elementu like 'top:%' order by e.nazwa_elementu desc")
    top = cursor.fetchall()
    return top


def get_nav(cursor):
    cursor.execute(
        "select e.nazwa_uzytkownika_elementu from public.website_elementy as e where e.nazwa_elementu like 'nav:%' order by e.nazwa_elementu ")
    nav = cursor.fetchall()
    elements = dict()
    for i in range(4):
        cursor.execute(
            "select * from public.website_podelementy as e where powiazanie_z_elementem_id=" + str(
                i + 5) + " order by e.order")
        nav[i] += tuple(cursor.fetchall())
    return nav


def get_footer(cursor):
    cursor.execute(
        "select e.nazwa_uzytkownika_elementu from public.website_elementy as e where e.nazwa_elementu like 'foot:%' order by e.nazwa_elementu desc")
    footer = cursor.fetchall()
    return footer


def get_grupy(cursor):
    cursor.execute("select * from public.website_grupyprzedszkolne")
    grupy = cursor.fetchall()
    return grupy


def index(request):
    cursor = connection.cursor()
    nav = get_nav(cursor)
    top = get_top(cursor)
    footer = get_footer(cursor)
    grupy = get_grupy(cursor)
    cursor.execute(
        "select e.zdjecie from public.website_podelementy as e where e.powiazanie_z_elementem_id = (select \"ID\" from public.website_elementy where nazwa_elementu like '%slider%') order by e.order")
    slidergorny = cursor.fetchall()
    cursor.execute(
        "select e.\"ID\",e.nazwa_uzytkownika_elementu from public.website_elementy as e where e.nazwa_elementu like 'box:%' order by e.\"ID\" ")
    box = cursor.fetchall()
    for i in range(3):
        cursor.execute(
            "select e.tytul,e.link_do_strony_id from public.website_podelementy as e where e.powiazanie_z_elementem_id = " +
            str(box[i][0]) + " order by e.order")
        box[i] += tuple(cursor.fetchall())

    posts=Aktualnosci.objects.order_by('-data').filter(do_kogo=None, visible=True)[:120]
    slider = Aktualnosci.objects.order_by('-data').filter(do_kogo=None, visible=True)[:8]
    calendar=Calendar.objects.get(slug="kalendarz")
    period_class = Month
    event_list = GET_EVENTS_FUNC(request, calendar)
    local_timezone = timezone.get_current_timezone()
    date = timezone.now()
    period = period_class(event_list, date, tzinfo=local_timezone)
    mydate = datetime.datetime.now()
    miesiac=mydate.strftime("%B")
    return render(request, 'glowna/index.html',
                  {'toptel': top[0][0], 'topmail': top[1][0], 'topul': top[2][0], 'nav': nav, 'slider': slider,
                   'box': box, 'infobox': posts, 'footer': footer, 'calendar': calendar, 'grupy': grupy,'period':period,'miesiac':miesiac})


@login_required()
def panel(request):
    nav = get_nav()
    top = get_top()
    footer = get_footer()
    return render(request, '404_error.html',
                  {'toptel': top[0][0], 'topmail': top[1][0], 'topul': top[2][0], 'nav': nav, 'footer': footer})


def aktualnosci(request, nr_art):
    cursor = connection.cursor()
    nav = get_nav(cursor)
    top = get_top(cursor)
    footer = get_footer(cursor)
    grupy = get_grupy(cursor)
    cursor.execute("select * from public.website_aktualnosci where \"ID\"=" + str(nr_art))
    result = cursor.fetchall()
    if (result[0][7] != False and result[0][7] != None):
        cursor.execute(
            "select s.data from public.gallery_album_images e left join public.gallery_image s on e.image_id = s.id where album_id=" + str(
                result[0][7]))
        photos = list(cursor.fetchall())

    else:
        photos = ''

    return render(request, 'aktualnosci/aktualnosci.html',
                  {'toptel': top[0][0], 'topmail': top[1][0], 'topul': top[2][0], 'nav': nav, 'footer': footer,
                   'result': result, 'gallery': photos, 'grupy': grupy})


def site(request, nr_site):
    cursor = connection.cursor()
    nav = get_nav(cursor)
    top = get_top(cursor)
    footer = get_footer(cursor)
    grupy = get_grupy(cursor)
    cursor.execute("select * from public.website_strona where \"ID\"=" + str(nr_site))
    result = cursor.fetchall()
    if (result[0][7] != False and result[0][7] != None):
        cursor.execute(
            "select s.data from public.gallery_album_images e left join public.gallery_image s on e.image_id = s.id where album_id=" + str(
                result[0][7]))
        photos = list(cursor.fetchall())

    else:
        photos = ''

    return render(request, 'podstrony/podstrona.html',
                  {'toptel': top[0][0], 'topmail': top[1][0], 'topul': top[2][0], 'nav': nav, 'footer': footer,
                   'result': result, 'gallery': photos, 'grupy': grupy})


def grupaAktualnosci(request, grupa):
    cursor = connection.cursor()
    nav = get_nav(cursor)
    top = get_top(cursor)
    footer = get_footer(cursor)
    grupy = get_grupy(cursor)
    post = Aktualnosci.objects.filter(do_kogo=GrupyPrzedszkolne.objects.get(nazwa_grupy=grupa))
    return render(request, 'aktualnosci/aktualnosci_dla_grup.html',
                  {'toptel': top[0][0], 'topmail': top[1][0], 'topul': top[2][0], 'nav': nav, 'footer': footer,
                   'grupy': grupy,'podstrona': grupa,'post':post})


def grupaGaleria(request, grupa):
    cursor = connection.cursor()
    nav = get_nav(cursor)
    top = get_top(cursor)
    footer = get_footer(cursor)
    grupy = get_grupy(cursor)
    gal = Album.objects.filter(grupyprzedszkolne=GrupyPrzedszkolne.objects.get(nazwa_grupy=grupa))
    return render(request, 'podstrony/galeria.html',
                  {'toptel': top[0][0], 'topmail': top[1][0], 'topul': top[2][0], 'nav': nav, 'footer': footer,
                   'grupy': grupy, 'podstrona': grupa,'gal':gal})
