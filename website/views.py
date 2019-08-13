from django.contrib.auth.decorators import login_required
from django.db import connection
from django.shortcuts import render


# Create your views here.
def error_404_view(request, exception):
    data = {"name": "ThePythonDjango.com"}
    return render(request, '404_error.html', data)


def get_top():
    cursor = connection.cursor()
    # g1
    cursor.execute(
        "select e.nazwa_uzytkownika_elementu from public.website_elementy as e where e.nazwa_elementu like 'top:%' order by e.nazwa_elementu desc")
    top = cursor.fetchall()
    return top


def get_nav():
    cursor = connection.cursor()
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

def get_footer():
    cursor = connection.cursor()
    cursor.execute(
        "select e.nazwa_uzytkownika_elementu from public.website_elementy as e where e.nazwa_elementu like 'foot:%' order by e.nazwa_elementu desc")
    footer = cursor.fetchall()
    return footer

def index(request):
    nav = get_nav()
    top = get_top()
    footer = get_footer()
    cursor = connection.cursor()
    cursor.execute(
        "select e.tytul,e.zdjecie ,e.link_do_strony_id from public.website_podelementy as e where e.powiazanie_z_elementem_id = (select \"ID\" from public.website_elementy where nazwa_elementu like '%slider%') order by e.order")
    slider = cursor.fetchall()
    cursor.execute(
        "select e.\"ID\",e.nazwa_uzytkownika_elementu from public.website_elementy as e where e.nazwa_elementu like 'box:%' order by e.\"ID\" ")
    box = cursor.fetchall()
    for i in range(3):
        cursor.execute(
            "select e.tytul,e.link_do_strony_id from public.website_podelementy as e where e.powiazanie_z_elementem_id = " +
            str(box[i][0]) + " order by e.order")
        box[i] += tuple(cursor.fetchall())
    cursor.execute(
        "select * from public.website_aktualnosci as e where e.visible = TRUE order by e.data desc ")
    posts = cursor.fetchall()

    return render(request, 'glowna/index.html',
                  {'toptel': top[0][0], 'topmail': top[1][0], 'topul': top[2][0], 'nav': nav, 'slider': slider,
                   'box': box,'infobox': posts,'footer':footer, 'calendar_slug':'kalendarz'})


@login_required()
def panel(request):
    nav = get_nav()
    top = get_top()
    footer = get_footer()
    return render(request, '404_error.html',
                  {'toptel': top[0][0], 'topmail': top[1][0], 'topul': top[2][0], 'nav': nav,'footer':footer})

def aktualnosci(request, nr_art):
    nav = get_nav()
    top = get_top()
    footer = get_footer()
    cursor = connection.cursor()
    cursor.execute("select * from public.website_aktualnosci where \"ID\"="+ str(nr_art))
    result= cursor.fetchall()
    if(result[0][7] != False and result[0][7] != None):
        cursor.execute("select s.data from public.gallery_album_images e left join public.gallery_image s on e.image_id = s.id where album_id=" + str(result[0][7]))
        photos = list(cursor.fetchall())

    else:
        photos=''

    return render(request, 'aktualnosci/aktualnosci.html',
           {'toptel': top[0][0], 'topmail': top[1][0], 'topul': top[2][0], 'nav': nav, 'footer': footer,'result':result, 'gallery': photos})


def site(request,nr_site):
    nav = get_nav()
    top = get_top()
    footer = get_footer()
    cursor = connection.cursor()
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
                   'result': result, 'gallery': photos})
